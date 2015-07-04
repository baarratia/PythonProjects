__author__ = 'Benja'
from Funciones import *
from Clases_Vehiculos import *
from Clases import *
from Clases2 import *


class viaje:
    viajes = {}
    viajes_origen = {}

    def __init__(self, linea):
        self.id = linea[0]
        self.origin = terminal.terminales[linea[1]]
        self.destination = terminal.terminales[linea[2]]
        self.route = ruta.rutas[linea[3]]
        self.departure = linea[4]
        self.vehicle = flota.dic_flota[linea[5].strip()]
        self.vehicle.viajes[self.departure] = self
        if viaje.viajes_origen.get(self.origin.code, 'No') == 'No':
            viaje.viajes_origen[self.origin.code] = [self]
        else:
            viaje.viajes_origen[self.origin.code].append(self)
        viaje.viajes[self.id] = self


    def __str__(self):
        return 'id: {0}, origen: {1}, destino: {2}\n ruta: {3}, fecha: {4}\n vehiculo: {5}'.format(self.id,
                                                                                                   self.origin.code,
                                                                                                   self.destination.code,
                                                                                                   self.route.id,
                                                                                                   self.departure,
                                                                                                   self.vehicle.name)


class itinerario:
    itinerarios = []

    def __init__(self, linea):
        self.object_id = linea[0]
        self.trip_id = {}
        for i in linea[1].split(' '):
            self.trip_id[viaje.viajes[i.strip()].id] = viaje.viajes[i.strip()]
        itinerario.itinerarios.append(self)

    def vincular(self):
        if len(self.object_id) == 5:
            cargo = carga.cargas[self.object_id]
            cargo.viajes = self.trip_id
        else:
            pers = persona.personas[self.object_id]
            pers.viajes = self.trip_id

    def __str__(self):
        return 'object_id: {0}, trip_id: {1}'.format(self.object_id, self.trip_id)

