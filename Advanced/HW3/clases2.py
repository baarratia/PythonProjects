__author__ = 'Benja'
from clases1 import *
from Funciones_creadoras import *
from Armar_Reloj import Armar_reloj


class SuperMercado:
    def __init__(self, archivo_clientes, archivo_cajas, archivo_productos, Imprimir, Eventos, Recuento_Clientes,
                 indicador):
        self.Eventos = Eventos
        self.Recuento_Clientes = Recuento_Clientes
        self.Imprimir = Imprimir
        self.archivo_cajas = archivo_cajas
        creador_cajas(self.archivo_cajas, self.Imprimir, self.Eventos)
        creador_lineas(archivo_productos, Imprimir, Eventos)
        creador_tipo_clientes(archivo_clientes)
        self.cajas = Caja.cajas
        self.lineas = Linea.lineas
        self.publico_recorriendo = []
        self.publico_caja = []
        self.abierto = True
        self.indicador = indicador

    def tiempo_llegada(self):
        if self.abierto:
            return round(random.expovariate(1 / 120) + 0.5)

    def cliente_entra(self):
        if self.abierto:
            y = cliente(self.Imprimir, self.Eventos, self.indicador)
            self.publico_recorriendo.append(y)
            return y.recorrer()

    def cliente_entra_caja(self, cliente):
        self.publico_recorriendo.remove(cliente)
        self.publico_caja.append(cliente)

    def cliente_sale(self, cliente):
        self.publico_caja.remove(cliente)

    def reiniciar(self):
        self.abierto = True
        for i in Producto.productos:
            Producto.productos[i].restock()


class Simulacion:
    def __init__(self, archivo_clientes, archivo_cajas, archivo_productos, dias, Imprimir, eventos, recuento_clientes,
                 indicador):
        self.archivo_clientes = archivo_clientes
        self.archivo_cajas = archivo_cajas
        self.archivo_productos = archivo_productos
        self.Eventos = eventos
        self.Recuento_Clientes = recuento_clientes
        self.Imprimir = Imprimir
        self.indicador = indicador
        self.SuperMercado = SuperMercado(self.archivo_clientes, self.archivo_cajas,
                                         self.archivo_productos, self.Imprimir, self.Eventos, self.Recuento_Clientes,
                                         self.indicador)
        self.dias = dias
        self.dia_actual = 0
        self.tiempo_maximo = 43200
        self.current_time = 0
        self.tiempo_total = 0
        self.contador_clientes = 0
        self.ganancias = 0
        self.promedio_colas = []

    def reloj(self):
        if self.current_time < 0:
            self.current_time = 0
        self.tiempo_total += self.current_time
        if self.Imprimir:
            print('Dia {0} a las {1}'.format(self.dia_actual, Armar_reloj(self.tiempo_total)))
        self.Eventos.write('Dia {0} a las {1}\n'.format(self.dia_actual, Armar_reloj(self.tiempo_total)))

    def cambiar_dia(self):
        if self.dia_actual + 1 < self.dias:
            self.dia_actual += 1
            self.SuperMercado.reiniciar()
            self.current_time = 0
            self.tiempo_total = 0
            if self.Imprimir:
                print('Inicio del día {}'.format(self.dia_actual))
            self.Eventos.write('Inicio del dia {}\n'.format(self.dia_actual))
            return True
        else:
            return False

    def productos_cajas(self):
        for i in self.SuperMercado.cajas:
            for j in i.cola:
                if j.comprar_productos_caja() is True:
                    self.reloj()

    def Colas_promedio(self):
        Sumatoria = 0
        for i in self.SuperMercado.cajas:
            Sumatoria += len(i.cola)
        self.promedio_colas.append(Sumatoria / len(self.SuperMercado.cajas))

    def Promedio_Final(self):
        Sumatoria = 0
        for i in self.promedio_colas:
            Sumatoria += i
        return Sumatoria / len(self.promedio_colas)

    def run(self):
        x = True
        while x is True:
            self.tiempo_total = self.SuperMercado.tiempo_llegada()
            self.SuperMercado.cliente_entra()
            self.contador_clientes += 1
            self.reloj()
            tiempo_llegada = self.SuperMercado.tiempo_llegada()
            while True:

                if len(self.SuperMercado.publico_recorriendo) == 0 and len(self.SuperMercado.publico_caja) == 0:
                    if tiempo_llegada is not None:
                        self.current_time = tiempo_llegada
                    else:
                        if self.Imprimir:
                            print('El SuperMercado cierra por hoy...')
                        self.Eventos.write('El SuperMercado cierra por hoy...\n')
                        break

                elif len(self.SuperMercado.publico_recorriendo) == 0 or len(self.SuperMercado.publico_caja) == 0:
                    if len(self.SuperMercado.publico_recorriendo) == 0:
                        tiempos_atencion = {}
                        for i in self.SuperMercado.cajas:
                            if i.tiempo_atencion() is not None:
                                tiempos_atencion[i.tiempo_atencion()] = i
                        minimo_tiempo_atencion = min(tiempos_atencion)
                        if tiempo_llegada is not None:
                            self.current_time = min(tiempo_llegada, minimo_tiempo_atencion)
                        else:
                            self.current_time = minimo_tiempo_atencion
                    else:
                        tiempos_recorrido = {}
                        for i in self.SuperMercado.publico_recorriendo:
                            tiempos_recorrido[i.recorrer()] = i
                        minimo_tiempo_recorrido = min(tiempos_recorrido)
                        if tiempo_llegada is not None:
                            self.current_time = min(tiempo_llegada, minimo_tiempo_recorrido)
                            minimo_tiempo_atencion = None
                        else:
                            self.current_time = minimo_tiempo_recorrido
                            minimo_tiempo_atencion = None

                else:
                    tiempos_atencion = {}
                    for i in self.SuperMercado.cajas:
                        if i.tiempo_atencion() is not None:
                            tiempos_atencion[i.tiempo_atencion()] = i
                    minimo_tiempo_atencion = min(tiempos_atencion)
                    tiempos_recorrido = {}
                    for i in self.SuperMercado.publico_recorriendo:
                        tiempos_recorrido[i.recorrer()] = i
                    minimo_tiempo_recorrido = min(tiempos_recorrido)
                    if tiempo_llegada is not None:
                        self.current_time = min(tiempo_llegada, minimo_tiempo_recorrido, minimo_tiempo_atencion)
                    else:
                        self.current_time = min(minimo_tiempo_recorrido, minimo_tiempo_atencion)
                marcador = 0
                if self.current_time == tiempo_llegada:
                    self.SuperMercado.cliente_entra()
                    self.contador_clientes += 1
                    self.reloj()
                    marcador = 1

                elif self.current_time == minimo_tiempo_recorrido:
                    tiempos_recorrido[
                        minimo_tiempo_recorrido].elegir_caja()
                    self.SuperMercado.cliente_entra_caja(tiempos_recorrido[minimo_tiempo_recorrido])
                    self.reloj()

                elif self.current_time == minimo_tiempo_atencion:
                    persona = tiempos_atencion[minimo_tiempo_atencion].cola[0]
                    self.current_time, paga = tiempos_atencion[minimo_tiempo_atencion].atender()
                    self.ganancias += paga
                    self.SuperMercado.cliente_sale(persona)
                    self.reloj()

                self.productos_cajas()
                self.Colas_promedio()  # Agrega el promedio de clientes por caja en este intervalo de tiempo

                if self.tiempo_total >= self.tiempo_maximo:
                    if self.SuperMercado.abierto:
                        if self.Imprimir:
                            print('El SuperMercado cierra sus puertas...')
                        self.Eventos.write('El SuperMercado cierra sus puertas...\n')
                        self.SuperMercado.abierto = False

                if self.tiempo_total >= self.tiempo_maximo and len(self.SuperMercado.publico_recorriendo) == 0 and len(
                        self.SuperMercado.publico_caja) == 0:
                    if self.Imprimir:
                        print('El SuperMercado cierra por hoy...')
                    self.Eventos.write('El SuperMercado cierra por hoy...\n')
                    break

                if tiempo_llegada is not None:
                    tiempo_llegada -= self.current_time

                if marcador == 1:
                    tiempo_llegada = self.SuperMercado.tiempo_llegada()

                try:
                    for i in tiempos_recorrido:
                        i -= self.current_time
                except:
                    pass

                try:
                    for j in tiempos_atencion:
                        if not not j:
                            j -= self.current_time
                except:
                    pass

            x = self.cambiar_dia()
        self.Eventos.close()
        for i in tipo_cliente.tipos_clientes:
            self.Recuento_Clientes.write('{}\n'.format(i))
        self.Recuento_Clientes.close()
        Reporte = open('Reporte.csv', 'w')
        Reporte.write('Total Ganado por el SuperMercado: ${}\n\n'.format(self.ganancias))
        Reporte.write('\nTOP 10 productos mas comprados por tipo de cliente:\n')
        for i in tipo_cliente.tipos_clientes:
            Reporte.write('\t{0} : {1}\n'.format(i.nombre, i.Maximos()))
        Reporte.write('Gasto Promedio por tipo de cliente\n')
        for i in tipo_cliente.tipos_clientes:
            Reporte.write('\t{0} : {1}\n'.format(i.nombre, i.gasto / i.registro))
        Reporte.write('\nTiempo Promedio dentro del SuperMercado con {} cajas, por tipo de cliente:\n'.format(
            len(self.SuperMercado.cajas)))
        for i in tipo_cliente.tipos_clientes:
            Reporte.write('\t{0} : {1}\n'.format(i.nombre, i.Tiempo_Promedio()))
        Reporte.write(
            '\nPromedio de personas en cola con {0} cajas: {1}'.format(len(self.SuperMercado.cajas),
                                                                       self.Promedio_Final()))
        Reporte.close()
        print('Fin de la simulacion')
