__author__ = 'Benja'

from Funciones import *
from Clases import *
from Clases2 import *
from Clases3 import *
from Clases_Vehiculos import *
from Creador_Vehiculos import *


def Obtencion_Datos():
    dic = {1: 'vehiculo', 2: 'pasajero', 3: 'carga', 4: 'viaje', 5: 'ruta'}
    n = 1
    for i in dic:
        print(n, ':  ', dic[i])
        n += 1
    print('\n')
    c = ':c'
    while c != ':)':
        try:
            num = int(input('Ingrese el número correspondiente al tipo de objeto que desea buscar: ').strip())
            if num < 1 or num > 5:
                raise ValueError
            else:
                c = ':)'
        except:
            print('Dato no valido, intente nuevamente...')

    if num == 1:
        while c != ':C':
            clave = input('Ingrese el nombre del vehiculo a buscar: ').strip()
            auto = flota.dic_flota.get(clave, False)
            if auto == False:
                print('Este vehiculo no existe, intente nuevamente...')
                continue
            else:
                return auto

    if num == 2:
        while c != ':C':
            clave = input('Ingrese el rut de la persona a buscar:   ').strip()
            pasajero = persona.personas.get(clave, False)
            if pasajero == False:
                print('Rut invalido o inexistente, intente nuevamente...')
                continue
            else:
                return pasajero

    if num == 3:
        while c != ':C':
            clave = input('Ingrese el id de la carga a buscar:  ').strip()
            cargo = carga.cargas.get(clave, False)
            if cargo == False:
                print('Id de carga invalido o inexistente, intente nuevamente...')
                continue
            else:
                return cargo

    if num == 4:
        while c != ':C':
            clave = input('Ingrese el id del viaje a buscar:    ').strip()
            v = viaje.viajes.get(clave, False)
            if v == False:
                print('Id de viaje invalido o inexistente, intente nuevamente...')
                continue
            else:
                return v

    if num == 5:
        while c != ':C':
            clave = input('Ingrese el id de la ruta a buscar:    ').strip()
            r = ruta.rutas.get(clave, False)
            if r == False:
                print('Id de ruta invalido o inexistente, intente nuevamente...')
                continue
            else:
                return r


