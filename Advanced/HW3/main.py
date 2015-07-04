__author__ = 'Benja'
from clases2 import *
from Simulacion2 import Simpy


def Menu():
    while True:
        print('\n             Bienvenidos al Simulador del SuperMercado :D\n'
              '\n(1)    Correr Simulacion 1 \n(2)    Correr Simulacion 2 (con Simpy)\n(0)    Salir y generar outputs\n')
        c = ':c'
        while c != ':)':
            try:
                num = int(input('Ingrese el número correspondiente a lo que desea hacer:  ').strip())
                if num < 0 or num > 2:
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
            dias = numero_dias()
            Imprimir = Imprimir_en_consola()
            Eventos = open('Eventos.csv', 'w')
            Recuento_Clientes = open('Recuento_Clientes.csv', 'w')
            simulacion = Simulacion('clientes.txt', 'cajas.txt', 'productos.txt', dias, Imprimir, Eventos,
                                    Recuento_Clientes, 1)
            simulacion.run()
            continue
        if num == 2:
            dias = numero_dias()
            capacidad = capacidad_estacionamiento()
            Imprimir = Imprimir_en_consola()
            Simpy('clientes.txt', 'cajas.txt', 'productos.txt', Imprimir,
                  2,
                  capacidad, dias)
            continue


def Imprimir_en_consola():
    print('\n             Desea que se muestren los eventos en tiempo real en consola?\n'
          '\n(1)    SI\n(2)    NO\n')
    c = ':c'
    while c != ':)':
        try:
            num = int(input('Ingrese el número correspondiente a lo que desea hacer:  ').strip())
            if num < 1 or num > 2:
                raise ValueError
            else:
                c = ':)'
        except:
            print('Dato no valido, intente nuevamente...\n')
    if num == 1:
        return True
    if num == 2:
        return False


def numero_dias():
    c = ':c'
    while c != ':)':
        try:
            dias = int(input('Ingrese el número de días que debe durar la simulación:    ').strip())
            if dias < 0:
                raise ValueError
            else:
                return dias
        except:
            print('Dato no valido, intente nuevamente...\n')

def capacidad_estacionamiento():
    c = ':c'
    while c != ':)':
        try:
            capacidad = int(input('Ingrese la capacidad del estacionamiento:    ').strip())
            if capacidad < 0:
                raise ValueError
            else:
                return capacidad
        except:
            print('Dato no valido, intente nuevamente...\n')

Menu()