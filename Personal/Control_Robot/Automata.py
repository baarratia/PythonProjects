import math


def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y2) ** 2)


def vector(x1, y1, x2, y2):
    d = distancia(x1, y1, x2, y2)
    if d != 0:
        return (x2 - x1) / d, (y2 - y1) / d
    else:
        return 0, 0


def seguir(x1, y1, x2, y2, x3, y3):  # pelota
    v1 = vector(x1, y1, x2, y2)
    v2 = vector(x1, y1, x3, y3)
    if abs(v1[0] - v2[0]) < 5 and abs(v1[1] - v2[1]) < 5 and abs(v1[2] - v2[2]):
        d = distancia(x1, y1, x3, y3)
        if d >= 5:  # evaluar que rango funciona mejor
            return 100, 100, 0  # return valores para que el robot avance (100,100,0)
        else:
            return 0, 0, 0
    else:
        while True:
            v1 = vector(x1, y1, x2, y2)
            if abs(v1[0] - v2[0]) < 5 and abs(v1[1] - v2[1]) < 5 and abs(v1[2] - v2[2]):
                return 0, 0, 0
            else:
                return 100, 100, 2
        ''''
        if x3 - x1 > 0:
            if y3 - y1 < 0:
                #girar en sentido antihorario
                pass
            else:'''''