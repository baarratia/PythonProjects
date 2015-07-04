__author__ = 'Benja'
import simpy
import random
from clases2 import SuperMercado
from clases1 import Caja, tipo_cliente, cliente, Producto
from Armar_Reloj import Armar_reloj


def repr(objeto):
    return '{0}, {1}'.format(objeto.cajas, objeto.cajas[0].cola)


def convertir_cajas(objeto):
    for i in objeto.cajas:
        i.Resource = simpy.Resource(objeto.env)
        i.cola = i.Resource.queue


def Solo_Preferenciales():
    for i in tipo_cliente.tipos_clientes:
        if i.nombre == 'PREFERENCIAL':
            lis = [i]
    tipo_cliente.tipos_clientes = lis


def elegir_caja_simpy(persona):
    C = 0
    Cajas_disponibles = []
    for i in Caja.cajas:
        if i.abierta is True:
            Cajas_disponibles.append(i)
    Caja.cajas = Cajas_disponibles
    for i in Caja.cajas:
        C += len(i.cola)
    for i in Caja.cajas:
        for j in Caja.cajas:
            SUM = 0
            if j.nombre != i.nombre:
                SUM += len(j.cola)
        if SUM == 0:
            caja_al_azar = random.choice(Caja.cajas)
            persona.caja_actual = caja_al_azar
            persona.comprar_productos_caja()
            if persona.Imprimir:
                print('{0} Ingresa a la cola de la caja {1}. \nCarro de compra: {2}'.format(persona.nombre,
                                                                                            caja_al_azar.nombre,
                                                                                            persona.carro))
            persona.Evento.write('{0} Ingresa a la cola de la caja {1}. \nCarro de compra: {2}\n'.format(persona.nombre,
                                                                                                         caja_al_azar.nombre,
                                                                                                         persona.carro))
            break
    else:
        i.probabilidad = (C - len(i.cola)) / SUM
        contador = 0
        for i in Caja.cajas:
            i.intervalo = (contador, Caja.cajas[i].probabilidad)
            contador += i.probabilidad

        x = random.uniform(0, contador)
        for i in Caja.cajas:
            if i.intervalo[0] <= x < i.intervalo[1]:
                persona.caja_actual = i
                if persona.Imprimir:
                    print('{0} Ingresa a la cola de la caja {1}. \nCarro de compra: {2}'.format(persona.nombre,
                                                                                                i.nombre,
                                                                                                persona.carro))
                persona.Evento.write(
                    '{0} Ingresa a la cola de la caja {1}. \nCarro de compra: {2}\n'.format(persona.nombre,
                                                                                            persona.nombre,
                                                                                            persona.carro))
                break


def Preferencial(objeto):  # Proceso de entrada al supermercado por cliente (Meterlo como metodo del SimpyMercado)
    y = cliente(objeto.Imprimir,
                objeto.Eventos,
                objeto.indicador)  # Llega un nuevo cliente (Arreglar la impresion que hace al llegar...)
    print(Armar_reloj(int(objeto.env.now)))
    with objeto.Estacionamiento.request(
            priority=random.uniform(0, 3)) as req:  # Busca algun lugar donde estacionarse
        yield req
    yield objeto.env.timeout(round(random.expovariate(1 / 300) + 0.5))  # Se estaciona
    print('{} se estaciona, ingresa al SuperMercado y comienza a recorrer'.format(y.nombre))
    print(Armar_reloj(int(objeto.env.now)))
    objeto.publico_recorriendo.append(y)  # Entra al SuperMercado y Comienza a Recorrer (tratar de simpear esto)
    t = y.recorrer()
    yield objeto.env.timeout(t)
    print('{} termina de recorrer y se dirige a las cajas'.format(y.nombre))
    print(Armar_reloj(int(objeto.env.now)))
    y.elegir_caja = elegir_caja_simpy
    y.elegir_caja(y)
    with y.caja_actual.Resource.request() as req:
        yield req
        objeto.publico_recorriendo.remove(y)
        y.comprar_productos_caja()
        tiempo_hasta_atasco = random.gauss(600, 120)
        tiempo_demora_caja = len(y.carro) * 3 + random.gauss(90, 0)
        if tiempo_demora_caja < tiempo_hasta_atasco:
            yield objeto.env.timeout(tiempo_demora_caja)
        else:
            yield objeto.env.timeout(tiempo_demora_caja + random.uniform(240, 360))
        print('{0}, es atendido en {1}, pagando ${2}, y sale del SuperMercado'.format(y.nombre, y.caja_actual.nombre,
                                                                                      y.gasto_actual))
        print(Armar_reloj(int(objeto.env.now)))


def Manejo_Cajas(objeto):
    largos = []
    for i in Caja.cajas:
        if len(i.cola) < 4:
            return False  # Ver si esto es lo más apropiado...
        else:
            print('Se deberia agregar una caja')
            x = open(objeto.archivo_cajas, 'r')
            primera_linea = (x.readline()).split('#')
            productos = x.readlines()
            lista = []
            for i in range(int(primera_linea[1].strip())):
                lista.append(Producto(productos[i], objeto.Imprimir, objeto.Eventos))
            nueva = Caja(lista, objeto.Imprimir, objeto.Eventos)
            print('Se abre {}'.format(nueva.nombre))
            print(Armar_reloj(int(objeto.env.now)))
            nueva.Resource = simpy.Resource(objeto.env)
            nueva.cola = nueva.Resource.queue
            yield objeto.env.timeout(180)
            for j in Caja.cajas:
                if j.nombre != nueva.nombre:
                    if len(j.cola) < 3:
                        nueva.abierta = False
                        print('Se da aviso de que la {} cerrará tras atender a los clientes actualmente en cola'.format(
                            nueva.nombre))
                        print(Armar_reloj(int(objeto.env.now)))
                        yield objeto.env.timeout(1)
                        if len(nueva.cola) == 0:
                            Caja.cajas.remove(nueva)
                            print('Se cierra {}'.format(nueva.nombre))
                            print(Armar_reloj(int(objeto.env.now)))
                            break




def Proceso(objeto):
    while True:
        if objeto.abierto:
            yield objeto.env.timeout(round(random.expovariate(1 / 120) + 0.5))
            objeto.env.process(objeto.Preferencial())
        objeto.env.process(objeto.Manejo_Cajas())
        if objeto.env.now >= 43200:
            objeto.abierto = False


def Crear_SimpyMercado(archivo_clientes, archivo_cajas, archivo_productos, Imprimir, Eventos, Recuento_Clientes,
                       indicador,
                       capacidad):
    envi = simpy.Environment()
    Estacionamiento = simpy.PriorityResource(envi, capacity=capacidad)
    SimpyMercado = type("SimpyMercado", (SuperMercado,),
                        {"env": envi, 'Estacionamiento': Estacionamiento, 'Preferencial': Preferencial,
                         'Manejo_Cajas': Manejo_Cajas, 'Proceso': Proceso,
                         '__repr__': repr})
    return SimpyMercado(archivo_clientes, archivo_cajas, archivo_productos, Imprimir, Eventos, Recuento_Clientes,
                        indicador)


Eventos = open('Evento.csv', 'w')
Recuento_Clientes = open('RC.csv', 'w')
SimpyMercado = Crear_SimpyMercado('clientes.txt', 'cajas.txt', 'productos.txt', True, Eventos, Recuento_Clientes, 2,
                                  100)
convertir_cajas(SimpyMercado)
Solo_Preferenciales()
SimpyMercado.env.process(Proceso(SimpyMercado))
SimpyMercado.env.run()