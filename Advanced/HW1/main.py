__author__ = 'Benja'

from Funciones import *
from Clases import *
from Clases2 import *
from Clases3 import *
from Clases_Vehiculos import *
from Creador_Vehiculos import *
from Obtencion_Datos import *
from Creador import *
from crear import *
from crear2 import *
from crear_vehiculos import *
from menu_principal import *
from Fecha_y_Hora import *

print('Cargando datos...')
crear_objetos(persona, 'passengers.txt')
crear_objetos(carga, 'cargo.txt')
crear_objetos(ciudad, 'cities.txt')
crear_objetos(terminal, 'hubs.txt')
crear_objetos(ruta, 'routes.txt')
crear_vehiculo('vehicle_models.txt', avion, barco, crucero, bus, camion)
crear_objetos(flota, 'fleet.txt')
crear_objetos(viaje, 'trips.txt')
crear_objetos(itinerario, 'itineraries.txt')
for i in itinerario.itinerarios:
    i.vincular()
for i in flota.dic_flota:
    fecha_hora(flota.dic_flota[i])
Menu1()