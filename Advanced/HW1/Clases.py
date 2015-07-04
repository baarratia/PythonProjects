from math import radians

__author__ = 'Benja'
from Funciones import *
from Clases_Vehiculos import *


class persona:
    personas = {}
    def __init__(self, linea):
        self.name = linea[0]
        self.lastname = linea[1]
        self.rut = linea[2].strip()
        self.viajes = []
        persona.personas[self.rut] = self

    def __str__(self):
        return 'name: {0}, lastname:{1}, rut: {2}\nviajes: {3}'.format(self.name, self.lastname, self.rut, self.viajes)


class carga:
    cargas = {}

    def __init__(self, linea):
        self.id = linea[0]
        self.name = linea[1]
        self.weight = float(linea[2])
        self.volume = float(linea[3])
        self.type = linea[4].strip()
        self.viajes = []
        carga.cargas[self.id] = self

    def __str__(self):
        return 'id: {0},name:{1}, weight: {2}, volume: {3}, type: {4}\n'.format(self.id, self.name, self.weight,
                                                                                self.volume, self.type)


class ciudad:
    ciudades = {}
    paises = {}

    def __init__(self, linea):
        self.name = linea[0]
        self.country = linea[1].strip()
        self.rutas = {} #{Tipo de ruta: ruta}
        self.lista_terminales = {} #{Tipo de terminal: terminal}
        ciudad.ciudades[self.name] = self
        if ciudad.paises.get(self.country, 'no') == 'no':
            ciudad.paises[self.country] = [self]
        else:
            ciudad.paises[self.country].append(self)

    def __str__(self):
        return 'name: {0}, country:{1}\n'.format(self.name, self.country)




