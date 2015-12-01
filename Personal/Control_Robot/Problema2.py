# -*- coding: utf-8 -*-
__author__ = 'Fabián Retamal'


class Rectangulo:  # Clase que modela cada rectangulo de una seccion, con sus atributos respectivos
    Seccion = []  # Lista que almacena en orden los rectangulos que van siendo creados para posteriormente
    #  poder acceder a ella y obtener los datos necesarios ordenadamente

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.Area = base * altura
        self.centroide = (altura / 2) + len(
            Rectangulo.Seccion) * altura  # Se aprovecha el que todos los rectangulos tienen igual seccion
        # para calcular el centroide respecto al punto de referencia inicial, multiplicando la altura de cada
        # rectangulo, por el numero de rectangulos en la lista, para asi, tras sumar la mitad de la altura del
        #  mismo, poder obtener la altura en la que estara el centroide de este rectangulo en especifico
        self.I = (base * altura ** 3) / 12
        Rectangulo.Seccion.append(self)  # Cuando el rectangulo ha finalizado de crearse, se agrega a la lista Seccion


def Rutina(b,
           H):  # Rutina que recibe el vector (lista) b con los anchos de cad rectangulo, y la altura de la seccion total
    altura = H / len(b)
    for i in range(len(b)):  # Se crean tantos rectangulos como anchos de estos hay en el vector
        Rectangulo(int(b[i]), altura)
    Area_total = 0
    for i in Rectangulo.Seccion:  # Se calcula el area total sumando el area de cada rectangulo creado anteriormente
        Area_total += i.Area
    Centroides = 0
    for i in Rectangulo.Seccion:
        Centroides += i.Area * i.centroide
    Centroide_Total = Centroides / Area_total
    Inercia_total = 0
    for i in Rectangulo.Seccion:
        Inercia_total += i.I + i.Area * ((Centroide_Total - i.centroide) ** 2)
    # Tras los calculos, se procede a imprimir los resultados obtenidos
    print('Area de la sección: {0}\nPosicion centro de gravedad: {1}\nMomento de Inercia:{2}'.format(Area_total,
                                                                                                     Centroide_Total,
                                                                                                     Inercia_total))


def main():  # En el main el usuario interactua con una simple interfaz de ingreso de datos
    while True:
        b = (input('Ingrese los anchos de los rectangulos de la sección, entre comas: ')).split(',')
        H = int(input('Ingrese la altura total de la sección: '))
        Rutina(b, H)
        Y = input('Ingrese la letra "Y" para continuar, cualquier otra letra terminará con el programa: ').strip()
        if Y == 'Y' or Y == 'y':
            Rectangulo.Seccion = []
            continue
        break


main()  # Se ejecuta el main y comienza el programa
