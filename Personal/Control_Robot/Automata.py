import math


def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def vector(x1, y1, x2, y2):
    d = distancia(x1, y1, x2, y2)
    if d != 0:
        return (x2 - x1) / d, (y2 - y1) / d
    else:
        return 0, 0


def angulo(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    base = math.degrees(math.atan2(b, a))
    if abs(a) < 0.5 and b >= 0:
        return 270
    elif abs(a) < 0.5 and b < 0:
        return 90
    elif base > 0 and a != 0:
        return 360 - base
    elif base < 0 and a != 0:
        return abs(base)
    else:
        return 0


"""
def angulo(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    if a == 0 and b >= 0:
        return 90
    elif a == 0 and b < 0:
        return 270

    base = abs(math.degrees(math.atan(b / a)))
    if a > 0 and b >= 0:
        return base
    elif a < 0 and b < 0:
        return base + 270
    elif a > 0 and b < 0:
        return base + 180
    elif a < 0 and b > 0:
        return base
    elif a > 0 and b == 0:
        return 0
    elif a < 0 and b == 0:
        return 180
"""


def orientar(x1, y1, x2, y2, p1, p2):
    a1 = angulo(x1, y1, x2, y2)
    a2 = angulo(x1, y1, p1, p2)
    amplitud = 35
    pg = 75

    if abs(a2 - a1) <= amplitud:
        return 0, 0, 0
    elif -(a2 - a1) > amplitud:
        print(a1, a2)
        return pg, pg, 2

    elif a2 - a1 > amplitud:
        print(a1, a2)
        return pg, pg, 3


def ir(x1, y1, x2, y2, x3, y3):
    # v1 = vector(x1, y1, x2, y2)
    # v2 = vector(x1, y1, x3, y3)
    a1 = angulo(x1, y1, x2, y2)
    a2 = angulo(x1, y1, x3, y3)
    print(a1);
    print(a2)
    amplitud = 10
    pg = 80

    d = distancia(x2, y2, x3, y3)
    if abs(a2 - a1) <= amplitud:
        if d > 30:
            return 100, 100, 0
        else:
            return 0, 0, 0
    elif -(a2 - a1) > amplitud:
        print(a1);
        print(a2)
        return pg, pg, 2

    elif a2 - a1 > amplitud:
        print(a1)
        print(a2)
        return pg, pg, 3
