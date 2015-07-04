__author__ = 'Benja'


def Lector(archivo):
    arch = open(archivo, 'r', encoding="utf8")
    lista = arch.readlines()
    lista = (lista[1:-1])[0]
    listeilor = []
    c = 0
    for i in lista:
        if i == '[':
            x = ''
            c += 1
        if i == ']':
            listeilor.append(x.split(', '))
            c -= 1
            if c == 0:
                break
        if i != '[' and i != ']':
            x += i
    return listeilor
