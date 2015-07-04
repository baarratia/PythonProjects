__author__ = 'Benja'
from Funciones import *
from Clases_Vehiculos import *
from Clases import *


class terminal:
    terminales = {}

    def __init__(self, linea):
        self.code = linea[0]
        self.city = ciudad.ciudades[linea[1]]
        self.type = linea[2]
        if len(ciudad.ciudades[linea[1]].lista_terminales) == 0 or ciudad.ciudades[linea[1]].lista_terminales.get(
                self.type, 'No') == 'No':
            ciudad.ciudades[linea[1]].lista_terminales[self.type] = [self]
        else:
            ciudad.ciudades[linea[1]].lista_terminales[self.type].append(self)
        self.size = linea[3].strip()
        if self.size == 'Big': # num_size facilitará las cosas al momento de ver donde que entrar
            self.num_size = 3
        if self.size == 'Medium':
            self.num_size = 2
        if self.size == 'Small':
            self.num_size = 1
        terminal.terminales[self.code] = self

    def __str__(self):
        return 'code: {0}, city:{1}, type: {2}, size:{3}\n'.format(self.code, self.city.name, self.type, self.size)


class ruta:
    rutas = {}

    def __init__(self, linea):
        self.id = linea[0]
        self.city1 = ciudad.ciudades[linea[1]]
        self.city2 = ciudad.ciudades[linea[2]]
        self.type = linea[3]
        self.length = linea[4]
        self.size = linea[5]
        self.cost = linea[6].strip()
        if self.city1.rutas.get(self, 'No') == 'No':
            self.city1.rutas[self.type] = [self]
        else:
            self.city1.rutas[self.type].append(self)
        if self.city2.rutas.get(self.type, 'No') == 'No':
            self.city2.rutas[self.type] = [self]
        else:
            self.city2.rutas[self.type].append(self)
        ruta.rutas[self.id] = self

    def __str__(self):
        return 'id: {0},city1:{1}\n, city2: {2}\n, type: {3}, length: {4}, size: {5}, cost: {6}\n'.format(self.id,
                                                                                                          self.city1,
                                                                                                          self.city2,
                                                                                                          self.type,
                                                                                                          self.length,
                                                                                                          self.size,
                                                                                                          self.cost)


class flota:
    dic_flota = {}
    aerial = {}
    aquatic = {}
    terrestrial = {}
    def __init__(self, linea):
        self.name = linea[1].strip()
        self.type = vehiculo.vehiculos[linea[0]]
        self.mensaje = self.type.mensaje
        self.viajes = {} # {fecha&hora : viaje}
        if self.mensaje == 'avion':
            flota.aerial[self.name] = self
        if self.mensaje == 'barco' or self.mensaje == 'crucero':
            flota.aquatic[self.name] = self
        if self.mensaje == 'bus' or self.mensaje == 'camion':
            flota.terrestrial [self.name] = self
        self.itinerario = {}
        self.horas_llegada = []
        flota.dic_flota[self.name] = self

    def __str__(self):
        return 'Nombre: {0}\nEspecificaciones:\n{1}'.format(self.name, self.type)

    def calcular(self):
        self.type.speed
        for i in self.viajes:
            pass


