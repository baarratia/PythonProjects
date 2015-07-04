from tkinter import Menu

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
from agendar_viajes import *


def Menu1():
    while True:
        print('\n             Bienvenidos a la Tarea 1 de Programación Avanzada :D\n'
              '\n(1)    Obtención de Datos\n(2)    '
              'Creación de Objetos\n(3)    Agendar Viajes\n(4)    '
              'Cancelar Pasajes\n(5)    Consultas\n(6)    Cálculos\n\n'
              '(0)    Salir\n')
        c = ':c'
        while c != ':)':
            try:
                num = int(input('Ingrese el número correspondiente a lo que desea hacer:  ').strip())
                if num < 0 or num > 6:
                    raise ValueError
                else:
                    c = ':)'
            except:
                print('Dato no valido, intente nuevamente...\n')
        if num == 0:
            print('\nHasta pronto!!!')
            break
        print('\n')
        if num == 1:
            print(Obtencion_Datos())
            esperar()
            continue
        if num == 2:
            creador()
            esperar()
            continue
        if num == 3:
            print('Agendar Viajes')
            agendar()
            esperar()
            continue
        if num == 4:
            print('Cancelar Pasajes: proximamente....')
            esperar()
            continue
        if num == 5:
            print('Consultas: proximamente...')
            esperar()
            continue
        if num == 6:
            print('Cálculos: proximamente...')
            esperar()
            continue
