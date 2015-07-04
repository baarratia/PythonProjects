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


def Solo_Preferenciales():
    for i in tipo_cliente.tipos_clientes:
        if i.nombre == 'PREFERENCIAL':
            lis = [i]
    tipo_cliente.tipos_clientes = lis


def anuncio(objeto, texto):
    if objeto.Imprimir:
        print('{0} en {1}'.format(texto, Armar_reloj(int(objeto.env.now))))
    objeto.Eventos.write('{0} en {1}\n'.format(texto, Armar_reloj(int(objeto.env.now))))


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
            persona.Evento.write(
                '{0} Ingresa a la cola de la caja {1}. \nCarro de compra: {2}\n'.format(persona.nombre,
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
    if objeto.abierto:
        y = cliente(objeto.Imprimir,
                    objeto.Eventos,
                    objeto.indicador)  # Llega un nuevo cliente (Arreglar la impresion que hace al llegar...)
        objeto.anuncio('')
        with objeto.Estacionamiento.request(
                priority=random.uniform(0, 3)) as req:  # Busca algun lugar donde estacionarse
            yield req
        yield objeto.env.timeout(round(random.expovariate(1 / 300) + 0.5))  # Se estaciona
        objeto.anuncio('{} se estaciona, ingresa al SuperMercado y comienza a recorrer'.format(y.nombre))
        objeto.publico_recorriendo.append(y)  # Entra al SuperMercado y Comienza a Recorrer (tratar de simpear esto)
        t = y.recorrer()
        yield objeto.env.timeout(t)
        objeto.anuncio('{} termina de recorrer y se dirige a las cajas'.format(y.nombre))
        y.elegir_caja = elegir_caja_simpy
        y.elegir_caja(y)
        with y.caja_actual.Resource.request() as req:
            yield req
            for u in Caja.cajas:
                if u != y.caja_actual:
                    if u.cambiar_caja():
                        objeto.anuncio('')
            y.caja_actual.cola.append(y)
            objeto.publico_recorriendo.remove(y)
            objeto.publico_caja.append(y)
            y.comprar_productos_caja()
            tiempo_hasta_atasco = random.gauss(600, 120)
            tiempo_demora_caja = len(y.carro) * 3 + random.gauss(90, 0)
            if tiempo_demora_caja < tiempo_hasta_atasco:
                yield objeto.env.timeout(tiempo_demora_caja)
            else:
                yield objeto.env.timeout(tiempo_demora_caja + random.uniform(240, 360))
            objeto.anuncio(
                '{0}, es atendido en {1}, pagando ${2}, y sale del SuperMercado'.format(y.nombre, y.caja_actual.nombre,
                                                                                        y.gasto_actual))
            objeto.ganancias += y.gasto_actual
            objeto.Num_clientes += 1
            y.tipo.agregar_tiempo(y.tiempo_recorriendo)
            objeto.publico_caja.remove(y)
            y.caja_actual.cola.remove(y)


def Manejo_Cajas(objeto):
    largos = []
    for i in Caja.cajas:
        if len(i.cola) < 4:
            return False  # Ver si esto es lo más apropiado...
        else:
            objeto.anuncio('Se deberia agregar una caja')
            x = open(objeto.archivo_cajas, 'r')
            primera_linea = (x.readline()).split('#')
            productos = x.readlines()
            lista = []
            for i in range(int(primera_linea[1].strip())):
                lista.append(Producto(productos[i], objeto.Imprimir, objeto.Eventos))
            nueva = Caja(lista, objeto.Imprimir, objeto.Eventos)
            objeto.anuncio('Se abre {}'.format(nueva.nombre))
            nueva.Resource = simpy.Resource(objeto.env)
            yield objeto.env.timeout(180)
            for j in Caja.cajas:
                if j.nombre != nueva.nombre:
                    if len(j.cola) < 3:
                        nueva.abierta = False
                        objeto.anuncio(
                            'Se da aviso de que la {} cerrará tras atender a los clientes actualmente en cola'.format(
                                nueva.nombre))
                        yield objeto.env.timeout(1)
                        if len(nueva.cola) == 0:
                            Caja.cajas.remove(nueva)
                            objeto.anuncio('Se cierra {0}'.format(nueva.nombre))
                            break

def Proceso(objeto):
    while True:
        if objeto.abierto:
            yield objeto.env.timeout(round(random.expovariate(1 / 120) + 0.5))
            objeto.env.process(objeto.Preferencial())
        objeto.env.process(objeto.Manejo_Cajas())
        if objeto.env.now >= 43200:
            if objeto.abierto is True:
                objeto.abierto = False
                objeto.anuncio('SuperMercado Cierra sus puertas')
                break


def Crear_SimpyMercado(archivo_clientes, archivo_cajas, archivo_productos, Imprimir, Eventos, Recuento_Clientes,
                       indicador,
                       capacidad):
    envi = simpy.Environment()
    Estacionamiento = simpy.PriorityResource(envi, capacity=capacidad)
    SimpyMercado = type("SimpyMercado", (SuperMercado,),
                        {"env": envi, 'Estacionamiento': Estacionamiento, 'Preferencial': Preferencial,
                         'Manejo_Cajas': Manejo_Cajas, 'Proceso': Proceso,
                         '__repr__': repr, 'anuncio': anuncio})
    return SimpyMercado(archivo_clientes, archivo_cajas, archivo_productos, Imprimir, Eventos, Recuento_Clientes,
                        indicador)


def Simpy(archivo_clientes, archivo_cajas, archivo_productos, Imprimir,
          indicador,
          capacidad, dias):
    Evento = open('Eventos.csv', 'w')
    Recuento_Clientes = open('Recuento_Clientes.csv', 'w')
    ganancias = 0
    contador_clientes = 0
    for i in range(dias):
        if Imprimir:
            print('\n\nDia {}\n\n'.format(i))
        Evento.write('\n\nDia {}\n\n'.format(i))
        SimpyMercado = Crear_SimpyMercado(archivo_clientes, archivo_cajas, archivo_productos, Imprimir, Evento,
                                          Recuento_Clientes, indicador,
                                          capacidad)
        SimpyMercado.ganancias = 0
        SimpyMercado.Num_clientes = 0
        convertir_cajas(SimpyMercado)
        Solo_Preferenciales()
        SimpyMercado.env.process(Proceso(SimpyMercado))
        SimpyMercado.env.run()
        ganancias += SimpyMercado.ganancias
        contador_clientes += SimpyMercado.Num_clientes
        SimpyMercado.reiniciar()
        if Imprimir:
            print('Fin dia {}'.format(i))
        Evento.write('Fin dia {}\n'.format(i))
    for i in tipo_cliente.tipos_clientes:
        Recuento_Clientes.write('{}\n'.format(i))
    Recuento_Clientes.close()
    Reporte = open('Reporte.csv', 'w')
    Reporte.write('Total Ganado por el SuperMercado: ${}\n\n'.format(ganancias))
    Reporte.write('Gasto Promedio por Cliente: ${}\n\n'.format(ganancias / contador_clientes))
    Reporte.write('TOP 10 productos mas comprados por tipo de cliente:\n')
    for i in tipo_cliente.tipos_clientes:
        Reporte.write('\t{0} : {1}\n'.format(i.nombre, i.Maximos()))
    Reporte.write('\nTiempo Promedio dentro del SuperMercado, por tipo de cliente:\n')
    for i in tipo_cliente.tipos_clientes:
        Reporte.write('\t{0} : {1}\n'.format(i.nombre, i.Tiempo_Promedio()))
    '''Reporte.write(
        '\nPromedio de personas en cola con {0} cajas: {1}'.format(len(self.SuperMercado.cajas),
                                                                   self.Promedio_Final()))'''
    Reporte.close()
    print('Fin de la simulacion')