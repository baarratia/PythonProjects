# -*- coding: utf-8 -*-
__author__ = 'Benja'
# sudoku = [[0, 2, 0], [3, 1, 0], [0, 3, 0]]
sudoku = [[3, 0, 0], [0, 1, 0], [1, 0, 0]]


def Recursiva(sudoku, x=0, y=0):
    print(x,y)
    listaQ = []  # Comienza comprobando el caso base, si el sudoku está completo, retorna el sudoku
    for i in sudoku:
        for j in i:
            if j == 0:
                listaQ.append(0)  # Usa listaQ para agregar un 0 cada vez que encuentre un elemento vacio en el sudoku
    if len(listaQ) == 0:  # Si la lista está vacia, no hay elementos vacios en el sudoku, por lo tanto está completo.
        return sudoku
    # Si el sudoku no está completo, entonces se comprueba que elemento está en la posición
    # dada, si es 0, entonces tendremos que intentar colocar un número.
    if sudoku[x][y] == 0:
        lista = []
        lista2 = []
        for j in range(len(sudoku[0])):
            if j != y:
                lista.append(sudoku[x][j])  # agrega los elementos que están en la misma fila sin incluir al mismo

        for j in range(len(sudoku)):
            if j != x:
                lista2.append(sudoku[j][y])  # agrega los elementos que están en la misma columna sin incluir al mismo
        vecinos = []
        for i in lista:
            if i != 0:
                vecinos.append(i)  # todo numero que entregue información es agregado a la lista vecinos
        for i in lista2:
            if i != 0 and i not in vecinos:  # todo numero que entregue información es agregado a la lista vecinos
                vecinos.append(i)
        if len(vecinos) == 2:  # si hay suficiente información se procede a insertar el número correspondiente
            if 1 not in vecinos:
                sudoku[x][y] = 1
            elif 2 not in vecinos:
                sudoku[x][y] = 2
            else:
                sudoku[x][y] = 3
    if x + 1 == len(sudoku):  # se avanza en las posiciones, si x supera el máximo, se baja una columna y se hace x=0
        x = 0
        if y + 1 == len(sudoku[0]):
            y = 0
        else:
            y += 1
    else:
        x += 1
    try:
        return Recursiva(sudoku, x,
                     y)  # Se llama de nuevo a la función para comprobar si está termindo y si no seguir desarrollandolo
    except:
        return 'Sudoku imposible'

print(sudoku)
'''
sudoku = []
for i in range(3):
    fila = (input('ingrese fila {}: '.format(i))).split(',')
    for i in range(len(fila)):
        fila[i] = int(fila[i])
    sudoku.append(fila)
'''
sudoku = Recursiva(sudoku)
print(sudoku)

