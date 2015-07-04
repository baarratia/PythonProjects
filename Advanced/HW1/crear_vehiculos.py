__author__ = 'Benja'
from Funciones import *
from Clases import *
from Clases2 import *
from Clases3 import *
from Clases_Vehiculos import *
from Creador_Vehiculos import *


def add_vehiculo():  # A la flota
    dic = {1: 'avion', 2: 'barco', 3: 'crucero', 4: 'bus', 5: 'camion'}
    n = 1
    for i in dic:
        print(n, ':  ', dic[i])
        n += 1
    print('\n')
    c = ':c'
    while c != ':)':
        try:
            num = int(input('Ingrese el número correspondiente al tipo de vehiculo que desea crear: ').strip())
            if num < 1 or num > 5:
                raise ValueError
            else:
                c = ':)'
        except:
            print('Dato no valido, intente nuevamente...')
    if num == 1:
        add_subvehiculo('Avion', avion.aviones)
    if num == 2:
        add_subvehiculo('Barco', barco.barcos)
    if num == 3:
        add_subvehiculo('Crucero', crucero.cruceros)
    if num == 4:
        add_subvehiculo('Bus', bus.buses)
    if num == 5:
        add_subvehiculo('Camion', camion.camiones)


def add_subvehiculo(tipo, diccionario):
    ct = 1
    print('\nDisponibles:\n')
    d = {}
    for i in diccionario:
        d[ct] = diccionario[i]
        print(ct, ':  ', diccionario[i])
        ct += 1
    c = ':c'
    while c != ':)':
        try:
            num = int(input('Ingrese el número correspondiente al {0} que desea agregar: '.format(tipo)).strip())
            if num < 1 or num > ct:
                raise ValueError
            else:
                c = ':)'
        except:
            print('Dato no valido, intente nuevamente...')
    g = 0
    while g == 0:
        try:
            nombre = (input('Nombre del {0}:  '.format(tipo))).strip()
            disponible = flota.dic_flota.get(nombre, 'disponible')  # Comprueba si el nombre se repite o no
            if disponible != 'disponible':
                raise ValueError
            else:
                g = 1
        except:
            print('Este nombre ya existe en la lista, o no es valido.\nIntente Nuevamente...')
    flota([d[num].model, nombre])
    arch = open('fleet.txt', 'a')
    arch.write('\n' + d[num].model + '\t' + nombre)
    arch.close()
    print('\n{0} añadido correctamente :D\n'.format(tipo))