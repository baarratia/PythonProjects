# -*- coding: utf-8 -*-
import random


def CorrerRodillo():
    a1 = (random.randint(0, 20))
    a2 = (random.randint(0, 20))
    a3 = (random.randint(0, 20))

    # a1
    if a1 >= 1 and a1 < 10:
        b1 = "-"
        c1 = "-"
    elif a1 == 10:
        b1 = "-"
        c1 = "-"
        a1 = "*"
    elif a1 == 0:
        b1 = "*"
        c1 = 1
        a1 = "-"
    elif a1 == 20:
        b1 = "*"
        c1 = 1
        a1 = "-"
    else:
        b1 = a1 - 10
        c1 = a1 - 9
        a1 = "-"
        if b1 == 10:
            b1 = "*"
        if c1 == 10:
            c1 = "*"

    # a2
    if a2 >= 1 and a2 < 10:
        b2 = "-"
        c2 = "-"
    elif a2 == 20:
        b2 = "*"
        c2 = 1
        a2 = "-"
    elif a2 == 10:
        b2 = "-"
        c2 = "-"
        a2 = "*"
    elif a2 == 0:
        b2 = "*"
        c2 = 1
        a2 = "-"
    else:
        b2 = a2 - 10
        c2 = a2 - 9
        a2 = "-"
        if b2 == 10:
            b2 = "*"
        if c2 == 10:
            c2 = "*"

    # a3
    if a3 >= 1 and a3 < 10:
        b3 = "-"
        c3 = "-"
    elif a3 == 20:
        b3 = "*"
        c3 = 1
        a3 = "-"
    elif a3 == 10:
        b3 = "-"
        c3 = "-"
        a3 = "*"
    elif a3 == 0:
        b3 = "*"
        c3 = 1
        a3 = "-"
    else:
        b3 = a3 - 10
        c3 = a3 - 9
        a3 = "-"
        if b3 == 10:
            b3 = "*"
        if c3 == 10:
            c3 = "*"

    print("   |", b1, "|", b2, "|", b3, "| \n-->|", a1, "|", a2, "|", a3, "| \n   |", c1, "|", c2, "|", c3, "|\n")
    resultado = [a1, a2, a3]
    return resultado


def AsignacionPuntaje():
    res = CorrerRodillo()
    comodin = res.count("*")
    linea = res.count("-")
    for i in range(1, 10):
        nro = (res.count(i))
        if comodin == 3:
            print("Obtuviste tres comodines!!")
            return 100
        elif nro == 3:
            print("Obtuviste tres numeros iguales!!")
            return 50
        elif comodin == 2:
            if linea == 1:
                print("Obtuviste dos comodines!!")
                return 5
            else:
                print("Obtuviste dos comodines y un numero!!")
                return 25
        elif nro == 2:
            if comodin == 1:
                print("Obtuviste dos numeros y un comodin!!")
                return 10
            else:
                print("Obtuviste dos numeros!!")
                return 3

        elif comodin == 1:
                print("Obtuviste un comodin!!")
                return 1
    return 0


def juego(bols):
    print("Estado actual de rodillo")
    print(CorrerRodillo())
    while True:
        c = 0
        if c < 2:
            apuesta = int(input("Cuanto quieres apostar (Minimo $10 y maximo $500)?: "))
            if apuesta >= 10 and apuesta <= 500:
                puntaje = AsignacionPuntaje()
                ganancia = apuesta*puntaje
                bols = (bols-apuesta)+ganancia
                print("Tienes $", bols, "en tu bolsillo")
                if bols <10:
                    print('Fin del juego. (No cumple con el monto mínimo de $10 en el bolsillo')
                    return "fin"
            else:
                print("La cantidad ingresada es invalida, recuerda que el Minimo es $10 y el maximo $500)")
                c += 1
        else:
            pregunta = str(input("Quieres seguir jugando?(responde si o no): "))
            if pregunta == "no":
                print("Gracias por jugar! \nHasta luego")
                return "fin"


def MenuPrincipal():
    contador = 0
    while contador < 2:
        bols = int(input("Cuanto dinero dispones para gastar?: "))
        if bols >= 500:
            print("Que comience el juego!")
            estado = juego(bols)
            if estado == "fin":
                break
        else:
            contador += 1
            print("La cantidad ingresada es invalida, debes contar con más de 500 para comenzar")


MenuPrincipal()
