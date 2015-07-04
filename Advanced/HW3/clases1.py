__author__ = 'Benja'
from collections import deque
from Armar_Reloj import Armar_reloj
import random


class tipo_cliente:
    tipos_clientes = []
    sumatoria_pesos = 0
    c = 0

    def __init__(self, tasa, line):
        self.tasa_de_ingreso = tasa
        l = line[0].split('#')
        self.nombre = (l[0]).strip()
        self.peso_aparicion = int((l[1]).strip())
        self.intervalo = (tipo_cliente.sumatoria_pesos, tipo_cliente.sumatoria_pesos + self.peso_aparicion)
        self.ui = int((l[2]).strip())
        self.oi = int((l[3]).strip())
        self.lineas_prob = {}
        self.preferencias_prob = {}
        for i in range(int((l[4]).strip())):
            y = line[i + 1].split('#')
            self.lineas_prob[Linea.lineas[y[0].strip()]] = float(y[1].strip())
        for i in range(int((l[5]).strip())):
            y = line[-1 - i].split('#')
            self.preferencias_prob[Producto.productos[y[0].strip()]] = float(y[1].strip())
        tipo_cliente.sumatoria_pesos += self.peso_aparicion
        self.productos_comprados = {}  # diccionario armado de la forma producto: cantidad comprada
        self.Tiempos = []  # Lista que guarda cada tiempo demora cada cliente de este tipo en el supermercado
        self.registro = 0
        self.gasto = 0
        tipo_cliente.tipos_clientes.append(self)
        tipo_cliente.c += 1

    def compra_producto(self, producto):
        if self.productos_comprados.get(producto, False) is False:
            self.productos_comprados[producto] = 1
        else:
            self.productos_comprados[producto] += 1

    def Maximos(self):
        maximos = []
        for i in range(10):
            try:  # Evita que el programa se caiga si la lista de productos comprados es menor que 10.
                key = max(self.productos_comprados, key=self.productos_comprados.get)
                maximos.append((key, self.productos_comprados[key]))
                del self.productos_comprados[key]
            except:
                pass
        return maximos

    def agregar_tiempo(self, tiempo):
        self.Tiempos.append(tiempo)

    def Tiempo_Promedio(self):
        SUM = 0
        for i in self.Tiempos:
            SUM += i
        return Armar_reloj(int(SUM / len(self.Tiempos)), True)

    def __repr__(self):
        return '{0}, {1}\n'.format(self.nombre, self.productos_comprados)


class Linea:
    lineas = {}

    def __init__(self, nombre, lista_productos):
        self.nombre = nombre
        self.productos = lista_productos
        for i in self.productos:
            i.Lugar = self
        Linea.lineas[self.nombre] = self

    def __repr__(self):
        return str(self.productos)


class Producto:
    productos = {}

    def __init__(self, linea, Imprimir, Eventos):
        linea = linea.split('#')
        self.nombre = linea[0].strip()
        self.cantidad = int(linea[1].strip())
        self.stock = self.cantidad  # Dato fijo para luego hacer el restock diario
        self.precio = int(linea[2].strip())
        self.R = int(linea[3].strip())
        self.PC = float(linea[4].strip())
        self.Lugar = None
        self.aviso_agotado = None
        self.Imprimir = Imprimir
        self.Eventos = Eventos
        Producto.productos[self.nombre] = self

    def __repr__(self):
        return self.nombre

    def comprar(self):
        if self.cantidad > 0:
            self.cantidad -= 1
            return True
        else:
            if self.aviso_agotado is not True:
                if self.Imprimir:
                    print('Producto {0} agotado en {1}'.format(self.nombre, self.Lugar.nombre))
                self.Eventos.write('Producto {0} agotado en {1}\n'.format(self.nombre, self.Lugar.nombre))
                self.aviso_agotado = True
            return False

    def restock(self):
        self.aviso_agotado = None
        self.cantidad = self.stock


class Caja:
    cajas = []
    c = 0

    def __init__(self, lista_productos, Imprimir, Evento):
        self.nombre = 'caja_' + str(Caja.c)
        Caja.c += 1
        self.productos = lista_productos
        for i in self.productos:
            i.Lugar = self
        self.cola = deque()
        self.tiempo_atencion_actual = 0
        self.tiempo = 0
        self.Imprimir = Imprimir
        self.Evento = Evento
        self.abierta = True  # Sirve para la segunda simulacion
        Caja.cajas.append(self)

    def __repr__(self):
        return 'Nombre: {0}'.format(self.nombre)

    def tiempo_atencion(self):
        if len(self.cola) != 0:
            persona = self.cola[0]
            self.tiempo_atencion_actual = len(persona.carro) * 3 + random.normalvariate(0, 90)
            return self.tiempo_atencion_actual

    def atender(self):
        if len(self.cola) != 0:
            persona = self.cola.popleft()
            if self.Imprimir:
                print(
                    '{0}, es atendido en {1}, pagando ${2}, y sale del SuperMercado'.format(persona.nombre, self.nombre,
                                                                                            persona.gasto_actual))
            self.Evento.write(
                '{0}, es atendido en {1}, pagando ${2}, y sale del SuperMercado\n'.format(persona.nombre, self.nombre,
                                                                                          persona.gasto_actual))
            self.cambiar_caja()
            for i in self.cola:
                i.tiempo_en_fila += self.tiempo_atencion_actual
            persona.tiempo_recorriendo += len(persona.carro) * 3 + random.uniform(0, 90)
            persona.tipo.agregar_tiempo(persona.tiempo_recorriendo)
            persona.tipo.gasto += persona.gasto_actual
            return persona.tiempo_recorriendo, persona.gasto_actual

    def cambiar_caja(self):
        if len(self.cola) != 0:
            persona = self.cola[-1]
            largos_colas = {}
            for i in Caja.cajas:
                if i.nombre != self.nombre:
                    largos_colas[len(i.cola)] = i
            caja_menos_cola = largos_colas[min(largos_colas)]
            if len(caja_menos_cola.cola) < len(self.cola):
                persona.caja_actual = caja_menos_cola
                caja_menos_cola.cola.append(self.cola.pop())
                persona.tiempo_recorriendo += random.uniform(20, 30)
                if self.Imprimir:
                    print('{0} se cambia de {1} a {2}'.format(persona.nombre, self.nombre, caja_menos_cola.nombre))
                self.Evento.write(
                    '{0} se cambia de {1} a {2}\n'.format(persona.nombre, self.nombre, caja_menos_cola.nombre))
                return True


class cliente:
    c = 0
    clientes = {}

    def __init__(self, imprimir, evento, indicador):
        self.nombre = 'Cliente_' + str(cliente.c)
        cliente.c += 1
        if indicador == 1:
            x = random.uniform(0, tipo_cliente.sumatoria_pesos)
            for i in tipo_cliente.tipos_clientes:
                if i.intervalo[0] <= x < i.intervalo[1]:
                    self.tipo = i
                    i.registro += 1
        if indicador == 2:
            self.tipo = tipo_cliente.tipos_clientes[0]
        self.max_gasto = random.gauss(self.tipo.ui, self.tipo.oi)
        self.gasto_actual = 0
        self.carro = []
        self.caja_actual = None
        self.tiempo_recorriendo = 0  # tiempo
        self.tiempo_en_fila = 0  # Aporta en la "tentacion" por comprarse un producto presente en la caja...
        cliente.clientes[self.nombre] = self
        self.Imprimir = imprimir
        self.Evento = evento
        if indicador == 1:
            if self.Imprimir:
                print('{0}, del tipo {1}, entra al Super Mercado y comienza a recorrer...'.format(self.nombre,
                                                                                                  self.tipo.nombre))
            self.Evento.write(
                '{0}, del tipo {1}, entra al Super Mercado y comienza a recorrer...\n'.format(self.nombre,
                                                                                              self.tipo.nombre))
        if indicador == 2:
            if self.Imprimir:
                print(
                    '{0}, del tipo {1}, entra al estacionamiento del Super Mercado y comienza a buscar donde estacionarse...'.format(
                        self.nombre,
                        self.tipo.nombre))
            self.Evento.write(
                '{0}, del tipo {1}, entra al estacionamiento del  Super Mercado y comienza a buscar donde estacionarse...\n'.format(
                    self.nombre,
                    self.tipo.nombre))

    def __repr__(self):
        return 'Nombre: {0}, Tipo: {1}'.format(self.nombre, self.tipo)

    def recorrer(self):  # Cliente recorre las lineas de su preferencia y decide sobre que productos compra
        if len(self.carro) == 0:
            for i in self.tipo.lineas_prob:
                if self.tipo.lineas_prob[i] >= random.random():  # ver si ingresa a la linea
                    for j in i.productos:
                        if self.tipo.preferencias_prob.get(j, 'NO') != 'NO':
                            if self.tipo.preferencias_prob[j] >= random.random():
                                cantidad = random.randint(1, j.R)
                                if self.gasto_actual + j.precio * cantidad <= self.max_gasto:
                                    for k in range(cantidad):
                                        if j.comprar() is True:
                                            self.tipo.compra_producto(j)
                                            self.carro.append(j)
                                            self.gasto_actual += j.precio
                        else:
                            if j.PC >= random.random():
                                cantidad = random.randint(1, j.R)
                                if self.gasto_actual + j.precio * cantidad <= self.max_gasto:
                                    for k in range(cantidad):
                                        if j.comprar() is True:
                                            self.tipo.compra_producto(j)
                                            self.carro.append(j)
                                            self.gasto_actual += j.precio
            for i in range(len(self.carro)):
                self.tiempo_recorriendo += random.randint(5, 10)
        return self.tiempo_recorriendo + self.tiempo_en_fila

    def elegir_caja(self):
        C = 0
        for i in Caja.cajas:
            C += len(i.cola)
        for i in Caja.cajas:
            for j in Caja.cajas:
                SUM = 0
                if j.nombre != i.nombre:
                    SUM += len(j.cola)
            if SUM == 0:
                caja_al_azar = random.choice(Caja.cajas)
                self.caja_actual = caja_al_azar
                caja_al_azar.cola.append(self)
                if self.Imprimir:
                    print('{0} Ingresa a la cola de la caja {1}. \nCarro de compra: {2}'.format(self.nombre,
                                                                                                caja_al_azar.nombre,
                                                                                                self.carro))
                self.Evento.write('{0} Ingresa a la cola de la caja {1}. \nCarro de compra: {2}\n'.format(self.nombre,
                                                                                                          caja_al_azar.nombre,
                                                                                                          self.carro))
                return None
            else:
                i.probabilidad = (C - len(i.cola)) / SUM
        contador = 0
        for i in Caja.cajas:
            i.intervalo = (contador, Caja.cajas[i].probabilidad)
            contador += i.probabilidad

        x = random.uniform(0, contador)
        for i in Caja.cajas:
            if i.intervalo[0] <= x < i.intervalo[1]:
                self.caja_actual = i
                i.cola.append(self)
                if self.Imprimir:
                    print('{0} Ingresa a la cola de la caja {1}. \nCarro de compra: {2}'.format(self.nombre, i.nombre,
                                                                                                self.carro))
                self.Evento.write(
                    '{0} Ingresa a la cola de la caja {1}. \nCarro de compra: {2}\n'.format(self.nombre, i.nombre,
                                                                                            self.carro))
                return None

    def comprar_productos_caja(self):
        if self.gasto_actual < self.max_gasto:
            for j in self.caja_actual.productos:
                if self.tipo.preferencias_prob.get(j, 'NO') != 'NO':
                    if self.tipo.preferencias_prob[j] * (100 + self.tiempo_en_fila) / 100 >= random.random():
                        cantidad = random.randint(1, j.R)
                        if self.gasto_actual + j.precio * cantidad <= self.max_gasto:
                            for k in range(cantidad):
                                if j.comprar() is True:
                                    self.carro.append(j)
                                    self.gasto_actual += j.precio
                                    if self.Imprimir:
                                        print('{0} compra {1} en {2}'.format(self.nombre, j.nombre,
                                                                             self.caja_actual.nombre))
                                    self.Evento.write(
                                        '{0} compra {1} en {2}\n'.format(self.nombre, j.nombre, self.caja_actual.nombre))
                                    return True

                else:
                    if j.PC * (100 + self.tiempo_en_fila) / 100 >= random.random():
                        cantidad = random.randint(1, j.R)
                        if self.gasto_actual + j.precio * cantidad <= self.max_gasto:
                            for k in range(cantidad):
                                if j.comprar() is True:
                                    self.carro.append(j)
                                    self.gasto_actual += j.precio
                                    if self.Imprimir:
                                        print('{0} compra {1} en {2}'.format(self.nombre, j.nombre,
                                                                             self.caja_actual.nombre))
                                    self.Evento.write(
                                        '{0} compra {1} en {2}\n'.format(self.nombre, j.nombre, self.caja_actual.nombre))
                                    return True





