# -*- coding: utf-8 -*-
import random

# Funciones  del juego:

def AsignarValor():
    x = random.randint(0, 20)
    if x >= 1 and x < 10:
        return ["-", x, "-"]
    elif x == 10:
        return ["-", "*", "-"]
    elif x == 0:
        return ["*", "-", 1]
    elif x == 20:
        return [1, "*", "-"]
    else:
        y = x - 10
        z = x - 9
        x = "-"
        if y == 10:
            y = "*"
        if z == 10:
            z = "*"
        return [y, x, z]


def GiroRodillo():
    col1 = AsignarValor()
    col2 = AsignarValor()
    col3 = AsignarValor()
    print('\n')
    for i in range(3):
        if i == 1:
            print('---->|  ' + str(col1[i]) + '  |  ' + str(col2[i]) + '  |  ' + str(col3[i]) + '  |<----')
            resultado = [col1[i], col2[i], col3[i]]
        else:
            print('     |  ' + str(col1[i]) + '  |  ' + str(col2[i]) + '  |  ' + str(col3[i]) + '  |')
    return resultado


def Puntaje(resultado):
    com = resultado.count("*")
    if com == 3:
        return 100
    elif com == 2:
        return 5
    elif com == 1:
        return 1
    else:
        for i in range(1, 10):
            n = resultado.count(i)
            if n == 3:
                return 50
            if com == 2 and n == 1:
                return 25
            if com == 1 and n == 2:
                return 10
            if n == 2:
                return 3
    return 0


def Juego(B):  # B = Bolsillo
    GiroRodillo()
    while True:
        c = 0
        if c < 2:
            A = int(input("Ingresa tu apuesta (Minimo $10 y maximo $500): "))  # A= Apuesta
            if A >= 10 and A <= 500:
                R = GiroRodillo()  # Resultado
                G = Puntaje(R) * A  # Ganancia
                B = (B - A) + G
                print('-Bolsillo: {0}\n-Ganancia: {1}\n-Perdida: {2}'.format(B, G, A))
                if B < 10:
                    print('No cumple con monto mínimo de $10')
                    break
            else:
                print("La apuesta debe ser entre $10 y $500, intenta nuevamente")
                c += 1
        else:
            pregunta = str(input("Desea continuar?: "))
            if (pregunta == "No" or pregunta == 'no' or pregunta == 'NO'):
                break


def Main():
    c = 0
    print('''*******************************************************\n***             Bienvenido al TRAGAMONEDAS          ***\n*******************************************************
\n\n  Este es un tragamonedas virtual con tres rodillos
  de juego, y 10 simbolos por rodillo. La apuesta
  maxima es $500, y debes tener al menos $500
  para poder comenzar a jugar.
  La apuesta mínima es $10.\n''')

    while c != 2:
        B = int(input('¿Cuanto dinero estas dispuesto a jugar hoy?: '))
        if B >= 500:
            print('Que comience el juego! Mucha suerte!')
            Juego(B)
            print('Fin del juego')
            break
        else:
            c += 1
            print('Monto mínimo para participar: $500...')
    print('Vuelve pronto!')

# Aquí se ejecuta el juego:
Main()
