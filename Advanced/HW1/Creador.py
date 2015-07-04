__author__ = 'Benja'
from crear import *
from crear2 import *
from crear_vehiculos import *

def creador():
    dic = {1: 'vehiculo', 2: 'pasajero', 3: 'carga', 4: 'viaje'}
    n = 1
    for i in dic:
        print(n, ':  ', dic[i])
        n += 1
    c = ':c'
    print('\n')
    while c != ':)':
        try:
            num = int(input('Ingrese el número correspondiente al tipo de objeto que desea crear: ').strip())
            if num < 1 or num > 4:
                raise ValueError
            else:
                c = ':)'
        except:
            print('Dato no valido, intente nuevamente...')
    print('\n')
    if num == 1:
        add_vehiculo()

    if num == 2:
        add_persona()

    if num == 3:
        add_carga()

    if num == 4:
        add_viaje()
