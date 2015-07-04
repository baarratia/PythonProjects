__author__ = 'Benja'


def crear_objetos(objeto, archivo):
    arch = open(archivo, 'r')
    arch.readline()  # Para comenzar a leer desde la segunda linea
    for i in arch:
        linea = i.split('\t')
        if len(linea) == 1:
            pass
        else:
            objeto(linea)
    arch.close()


def esperar():
    input('\nPresione enter para continuar')
    print('\n\n')







