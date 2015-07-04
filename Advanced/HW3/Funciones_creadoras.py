__author__ = 'Benja'
from clases1 import *

def creador_tipo_clientes(archivo):
    x = open(archivo, 'r')
    tasa_de_ingreso = x.readline()
    clientes = x.readlines()
    while len(clientes) > 0:
        try:
            c = clientes.index('$\n')
        except:
            c = len(clientes)
        t = clientes[:c]  # entregar esto para crear cada tipo de cliente.
        x = tipo_cliente(tasa_de_ingreso, t)
        clientes = clientes[c + 1:]


def creador_cajas(archivo, Imprimir, Eventos):
    x = open(archivo, 'r')
    primera_linea = (x.readline()).split('#')
    productos = x.readlines()
    lista = []
    for i in range(int(primera_linea[1].strip())):
        lista.append(Producto(productos[i], Imprimir, Eventos))
    for i in range(int(primera_linea[0].strip())):
        Caja(lista, Imprimir, Eventos)


def creador_lineas(archivo, Imprimir, Eventos):
    x = open(archivo, 'r')
    lista = x.readlines()
    while len(lista) > 0:
        try:
            c = lista.index('$\n')
        except:
            c = len(lista)
        t = lista[:c]
        l = t[0].split('#')
        lista_productos = []
        productos = t[1:]
        for i in range(len(productos)):
            lista_productos.append(Producto(productos[i], Imprimir, Eventos))
        x = Linea(l[0].strip(), lista_productos)
        lista = lista[c + 1:]

