__author__ = 'Benja'
from Funciones import *
from Clases import *
from Clases2 import *
from Clases3 import *
from Clases_Vehiculos import *
from Creador_Vehiculos import *


def add_persona():
    g = 0
    while g == 0:
        try:
            rut = input('RUT con guion: ').strip()
            disponible = persona.personas.get(rut, 'disponible')
            if (len((rut.split('-'))[1]) != 1) or (disponible != 'disponible'):
                print(':D')
                raise ValueError
            else:
                g = 1
        except:
            print('Este rut ya existe en la lista, o no es valido.\nIntente Nuevamente...')
    nombre = input('Nombre: ').strip()
    apellido = input('Apellido: ').strip()
    persona([nombre, apellido, rut])
    arch = open('passengers.txt', 'a')
    arch.write('\n' + nombre + '\t' + apellido + '\t' + rut)
    arch.close()
    print('\nPersona añadida correctamente :D\n')


def add_carga():
    g = 0
    while g == 0:
        try:
            id = (input('ID de 5 digitos: ')).strip()
            disponible = carga.cargas.get(id, 'disponible')
            if (len(id) != 5) or (disponible != 'disponible'):
                raise ValueError
            else:
                g = 1
        except:
            print('Esta id ya existe en la lista, o no es valida.\nIntente Nuevamente...')
    nombre = input('Nombre: ').strip()
    while g == 1:
        try:
            peso = float(input('Peso: ').strip())
            g = 2
        except:
            print('Ingrese un peso válido...\n')
            continue
    while g == 2:
        try:
            volumen = float(input('Volumen: ').strip())
            g = 3
        except:
            print('Ingrese un volumen válido...\n')
            continue
    while g == 3:
        try:
            num = int(input(
                '\n1:\tNormal\n2:\tDelicado\n3:\tPeligroso\n\nIngrese el número correspondiente al tipo de la carga que desea agregar:  ').strip())
            if num<1 or num>3:
                raise ValueError
            else:
                g = 4
        except:
            print('Opción no valida. Intente Nuevamente...\n')
            continue
    d = {1: 'Normal', 2: 'Delicate', 3: 'Dangerous'}
    tipo = d[num]
    carga([id, nombre,peso, volumen, tipo])  #################
    arch = open('cargo.txt', 'a')
    arch.write('\n' + id + '\t' + nombre + '\t' + str(peso) + '\t' + str(volumen) + '\t' + tipo)
    arch.close()
    print('\nPaquete añadido correctamente :D\n')