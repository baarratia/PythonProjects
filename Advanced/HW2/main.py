from struct import pack

__author__ = 'Benja'

from clases import *
from interfaz import Interfaz
from clase_Tarea import Tarea
from lector import Lector

if __name__ == '__main__':
    continentes = Lector('continentes.txt')
    paises = Lector('paises.txt')
    ciudades = Lector('ciudades.txt')
    comunas = Lector('comunas.txt')
    calles = Lector('calles.txt')
    tipos = Lector('tipos.txt')
    for x in range(len(calles)):
        for y in range(len(calles[x])):
            ubicacion(x, y, continentes, paises, ciudades, comunas, calles, tipos)
    map = Mapa(tipos)
    tarea = Tarea(map)
    funciones = [tarea.consulta1, tarea.consulta2,
                 tarea.consulta3, tarea.consulta4, tarea.consulta5]
    interfaz = Interfaz(
        tarea.func_zoom, tarea.func_move, tarea.lista, funciones)
    interfaz.run()