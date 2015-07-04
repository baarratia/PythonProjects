__author__ = 'Benja'
from Funciones import *
from Clases import *
from Clases2 import *
from Clases3 import *
from Clases_Vehiculos import *
from Creador_Vehiculos import *
from Fecha_y_Hora import *
from elegir_terminal import *

def agendar():
    print('\n(1)    Pasajero\n(2)    Carga\n')
    c = ':c'
    while c != ':)':
        try:
            num = int(input(
                'Ingrese el número correspondiente al tipo de \nobjeto al que desea agendar un nuevo viaje:  ').strip())
            if num < 1 or num > 2:
                raise ValueError
            else:
                c = ':)'
        except:
            print('Dato no valido, intente nuevamente...\n')
    if num == 1:
        agendar_pasajero()
    if num == 2:
        print('En desarrollo...')
        pass


def agendar_pasajero():
    c = ''
    while c != ':C':
        clave = input('\nIngrese el rut de la persona a la que desea agendar un viaje:   ').strip()
        pasajero = persona.personas.get(clave, False)
        if pasajero == False:
            print('Rut invalido o inexistente, intente nuevamente...')
            continue
        else:
            print('Pasajero {0} encontrado!\n'.format((pasajero.name + ' ' + pasajero.lastname)))
            c = ':C'
    print('Viajes actualmente agendados:\n')
    for i in pasajero.viajes:
        print(pasajero.viajes[i], '\n')
    esperar()
    c = ''
    while c != ':C':
        print('Ingrese lugar de origen')
        terminal, ciudad = elegir_terminal()
        try:
            d = {}
            b = 1
            for i in viaje.viajes_origen[terminal.code]:
                d[b] = i
                print(b,':  ',i, '\n')
                b +=1
            c = ':C'
        except:
            print('Viajes no disponibles, intente nuevamente...')
            esperar()
    c = ':c'
    while c != ':)':
        try:
            num = int(input('Ingrese el número correspondiente al viaje escogido:   ').strip())
            if num < 1 or num > b:
                raise ValueError
            else:
                c = ':)'
        except:
            print('Dato no valido, intente nuevamente...')
    via = d[num]
    pasajero.viajes[via.id] = via
    arch = open('itineraries.txt', 'r')
    a = []
    for i in arch:
        a.append(i)
    c = 0
    while c != (len(a)):
        s = a[c].split('\t')
        if s[0] == pasajero.rut:
            e = s[1].split(' ')
            z = 0
            p = []
            while z != (len(e)):
                p.append(e[z].strip())
                z+=1
            p.append(via.id)
            p = ' '.join(p)
            a[c] = pasajero.rut+'\t'+p
        c+=1
    arch.close()
    ar= open('itineraries.txt', 'w')
    for i in a:
        ar.write(i)
    print('viaje agregado!')

