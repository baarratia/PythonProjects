__author__ = 'Benja'
from Funciones import *
from Clases import *
from Clases2 import *
from Clases3 import *
from Clases_Vehiculos import *
from Creador_Vehiculos import *
from elegir_terminal import *
from Elegir_Vehiculo import *
from Fecha_y_Hora import *


def add_viaje():
    g = 0
    while g == 0:
        try:
            id = (input('Ingrese un ID de 6 digitos para el nuevo viaje: ')).strip()
            disponible = viaje.viajes.get(id, 'disponible')
            if (len(id) != 6) or (disponible != 'disponible'):
                raise ValueError
            else:
                g = 1
        except:
            print('Esta id ya existe en la lista, o no es valida.\nIntente Nuevamente...')
    terminal_origen, ciudad_origen = elegir_terminal(ciudad)
    tipo = terminal_origen.type
    for i in terminal_origen.city.rutas[tipo]:
        if ciudad_origen.name != i.city1.name:
            ciudad_destino = i.city1
        else:
            ciudad_destino = i.city2
    for i in ciudad_destino.lista_terminales[tipo]:
        print(i)
    ct = 1
    d = {}
    print('\nTerminal de destino:\n')
    for i in ciudad_destino.lista_terminales[tipo]:
        d[ct] = i
        print(ct, ':  ', i)
        ct += 1
    c = ':c'
    while c != ':)':
        try:
            num = int(input('Ingrese el número correspondiente al terminal de destino:  ').strip())
            if num < 1 or num > ct:
                raise ValueError
            else:
                c = ':)'
        except:
            print('Dato no valido, intente nuevamente...')
    terminal_destino = d[num]
    for i in ruta.rutas:
        if (((ruta.rutas[i].city1.name == ciudad_origen.name) and (ruta.rutas[i].city2.name == ciudad_destino.name)) or
                ((ruta.rutas[i].city2.name == ciudad_origen.name) and (
                            ruta.rutas[i].city1.name == ciudad_destino.name))) and (
                    ruta.rutas[i].type == tipo):
            route = ruta.rutas[i]
    porte = min(terminal_origen.num_size, terminal_destino.num_size)
    fech = ingresar_fecha()
    veh = elegir_vehiculo(route.type, porte, fech)
    viaje([id, terminal_origen.code, terminal_destino.code, route.id, fech, veh.name])
    arch = open('trips.txt', 'a')
    arch.write(
        '\n' + id + '\t' + terminal_origen.code + '\t' + terminal_destino.code + '\t' + route.id + '\t' + fech + '\t' + veh.name)
    arch.close()
    print('\nViaje añadido correctamente :D\n')


