__author__ = 'Benja'
from Funciones import *
from Clases import *
from Clases2 import *
from Clases3 import *
from Clases_Vehiculos import *
from Creador_Vehiculos import *
from Fecha_y_Hora import *

def elegir_terminal():
    global ciudad
    ct = 1
    d = {}
    print('\nPaíses disponibles:\n')
    for i in ciudad.paises:
        d[ct] = ciudad.paises[i]
        print(ct, ':  ', i)
        ct += 1
    c = ':c'
    while c != ':)':
        try:
            num = int(input('Ingrese el número correspondiente al país de la ciudad de origen:  ').strip())
            if num < 1 or num > ct:
                raise ValueError
            else:
                c = ':)'
        except:
            print('Dato no valido, intente nuevamente...')
    b = 1
    pais = d[num]
    dic = {}
    print('\nCiudades disponibles:\n')
    for i in pais:
        dic[b] = i
        print(b, ':  ', i.name)
        b += 1
    c = ':c'
    while c != ':)':
        try:
            num = int(input('Ingrese el número correspondiente a la ciudad de origen:   ').strip())
            if num < 1 or num > b:
                raise ValueError
            else:
                c = ':)'
        except:
            print('Dato no valido, intente nuevamente...')
    ciudad = dic[num]
    b = 1
    dic = {}
    print('\nTipos de terminales disponibles:\n')
    for i in ciudad.lista_terminales:
        dic[b] = ciudad.lista_terminales[i]
        print(b, ':  ', i)
        b += 1
    c = ':c'
    while c != ':)':
        try:
            num = int(input('Ingrese el número correspondiente al tipo terminal de origen:  ').strip())
            if num < 1 or num > b:
                raise ValueError
            else:
                c = ':)'
        except:
            print('Dato no valido, intente nuevamente...')
    terminales = dic[num]
    b = 1
    print('\nTerminales disponibles y destino:\n')
    for i in terminales:
        print(b, 'Terminal:  ', i)
        for j in terminales[b - 1].city.rutas[i.type]:
            if ciudad.name != j.city1.name:
                print('   Destino: ', j.city1.name)
            else:
                print('   Destino: ', j.city2.name)
        b += 1
    c = ':c'
    while c != ':)':
        try:
            num = int(input('Ingrese el número correspondiente al terminal de origen:   ').strip())
            if num < 1 or num > b:
                raise ValueError
            else:
                c = ':)'
        except:
            print('Dato no valido, intente nuevamente...')
    return terminales[num - 1], ciudad