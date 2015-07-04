__author__ = 'Benja'
from Funciones import *
from Clases import *
from Clases2 import *
from Clases3 import *
from Clases_Vehiculos import *
from Creador_Vehiculos import *
from elegir_terminal import *


def elegir_vehiculo(tipo, porte, fecha):
    print('p')
    d = {}
    ct = 1
    if tipo == 'Aerial':
        for i in flota.aerial:
            if (flota.aerial[i].type.num_size <= porte) and (flota.aerial[i].itinerario.get(fecha, 'No') == 'No'):
                d[ct] = flota.aerial[i]
                print(ct, ': ', flota.aerial[i])
                ct += 1
    if tipo == 'Terrestrial':
        for i in flota.terrestrial:
            if (flota.terrestrial[i].type.num_size <= porte) and (flota.terrestrial[i].itinerario.get(fecha, 'No') == 'No'):
                d[ct] = flota.terrestrial[i]
                print(ct, ': ', flota.terrestrial[i])
                ct += 1
    if tipo == 'Aquatic':
        for i in flota.aquatic:
            if (flota.aquatic[i].type.num_size <= porte) and (flota.aquatic[i].itinerario.get(fecha, 'No') == 'No'):
                d[ct] = flota.aquatic[i]
                print(ct, ': ', flota.aquatic[i])
                ct += 1
    c = ':c'
    while c != ':)':
        try:
            num = int(input('Ingrese el número correspondiente al vehiculo que desea utilizar:  ').strip())
            if num < 1 or num > ct:
                raise ValueError
            else:
                c = ':)'
        except:
            print('Dato no valido, intente nuevamente...')
    return d[num] #vehiculo
