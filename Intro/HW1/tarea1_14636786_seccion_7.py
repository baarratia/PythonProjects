import tableroGUI

tablero = None
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = (0,) * 16
puntaje = 0


def inicia_juego():
    global a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = tablero.inicia_juego()


def actualizar_tablero():
    global a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p
    tablero.update(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, puntaje)


def esperar_presionar_tecla():
    return tablero.esperarPresionarTecla()


def aleatorio():
    return tablero.aleatorio()

# mis funciones:
import random
import math


def PhilCollins(a1, b1, c1, d1):  # Filas/Columnas
    if (((c1 == 1 and d1 == 2) or (c1 == 2 and d1 == 1)) or (c1 == d1 or d1 == 0)) and not (
        (c1 == 1 and d1 == 1) or (c1 == 2 and d1 == 2)):
        d1 = c1 + d1;
        c1 = b1;
        b1 = a1;
        a1 = 0
    elif (((b1 == 1 and c1 == 2) or (b1 == 2 and c1 == 1)) or (b1 == c1 or c1 == 0)) and not (
        (b1 == 1 and c1 == 1) or (b1 == 2 and c1 == 2)):
        c1 = b1 + c1;
        b1 = a1;
        a1 = 0
    elif (((a1 == 1 and b1 == 2) or (a1 == 2 and b1 == 1)) or (a1 == b1 or b1 == 0)) and not (
        (a1 == 1 and b1 == 1) or (a1 == 2 and b1 == 2)):
        b1 = a1 + b1;
        a1 = 0
    return a1, b1, c1, d1


def reglasletras(a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1, l1, m1, n1, o1, p1):
    a1, b1, c1, d1 = PhilCollins(a1, b1, c1, d1);
    e1, f1, g1, h1 = PhilCollins(e1, f1, g1, h1);
    i1, j1, k1, l1 = PhilCollins(i1, j1, k1, l1);
    m1, n1, o1, p1 = PhilCollins(m1, n1, o1, p1)
    return a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1, l1, m1, n1, o1, p1


def movimiento(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, contadorA, contadorB, contadorC, contadorD):
    tecla = esperar_presionar_tecla()
    if tecla == "derecha":
        a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1, l1, m1, n1, o1, p1 = a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = reglasletras(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p)
        if a1 != a or b1 != b or c1 != c or d1 != d or e1 != e or f1 != f or g1 != g or h1 != h or i1 != i or j1 != j or k1 != k or l1 != l or m1 != m or n1 != n or o1 != o or p1 != p:
            a, e, i, m = numerosalvaje(a, e, i, m);
            contadorA = 0;
            contadorB = 0;
            contadorC = 0;
            contadorD = 0
        else:
            contadorA += 1
    if tecla == "izquierda":
        d1, c1, b1, a1, h1, g1, f1, e1, l1, k1, j1, i1, p1, o1, n1, m1 = d, c, b, a, h, g, f, e, l, k, j, i, p, o, n, m
        d, c, b, a, h, g, f, e, l, k, j, i, p, o, n, m = reglasletras(d, c, b, a, h, g, f, e, l, k, j, i, p, o, n, m)
        if a1 != a or b1 != b or c1 != c or d1 != d or e1 != e or f1 != f or g1 != g or h1 != h or i1 != i or j1 != j or k1 != k or l1 != l or m1 != m or n1 != n or o1 != o or p1 != p:
            d, h, l, p = numerosalvaje(d, h, l, p);
            ontadorA = 0;
            contadorB = 0;
            contadorC = 0;
            contadorD = 0
        else:
            contadorB += 1
    if tecla == "arriba":
        m1, i1, e1, a1, n1, j1, f1, b1, o1, k1, g1, c1, p1, l1, h1, d1 = m, i, e, a, n, j, f, b, o, k, g, c, p, l, h, d
        m, i, e, a, n, j, f, b, o, k, g, c, p, l, h, d = reglasletras(m, i, e, a, n, j, f, b, o, k, g, c, p, l, h, d)
        if a1 != a or b1 != b or c1 != c or d1 != d or e1 != e or f1 != f or g1 != g or h1 != h or i1 != i or j1 != j or k1 != k or l1 != l or m1 != m or n1 != n or o1 != o or p1 != p:
            m, n, o, p = numerosalvaje(m, n, o, p);
            ontadorA = 0;
            contadorB = 0;
            contadorC = 0;
            contadorD = 0
        else:
            contadorC += 1
    if tecla == "abajo":
        a1, e1, i1, m1, b1, f1, j1, n1, c1, g1, k1, o1, d1, h1, l1, p1 = a, e, i, m, b, f, j, n, c, g, k, o, d, h, l, p
        a, e, i, m, b, f, j, n, c, g, k, o, d, h, l, p = reglasletras(a, e, i, m, b, f, j, n, c, g, k, o, d, h, l, p)
        if a1 != a or b1 != b or c1 != c or d1 != d or e1 != e or f1 != f or g1 != g or h1 != h or i1 != i or j1 != j or k1 != k or l1 != l or m1 != m or n1 != n or o1 != o or p1 != p:
            a, b, c, d = numerosalvaje(a, b, c, d);
            ontadorA = 0;
            contadorB = 0;
            contadorC = 0;
            contadorD = 0
        else:
            contadorD += 1
    return a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, contadorA, contadorB, contadorC, contadorD
    actualizar_tablero()


def puntajeL(x):
    if x == 0 or x == 1 or x == 2:
        puntajeL = 0
    else:
        I = (math.log(x / 3)) / (math.log(2));
        puntajeL = 3 ** (I + 1)
    return puntajeL


def puntaje_total(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
    q = puntajeL(a) + puntajeL(b) + puntajeL(c) + puntajeL(d) + puntajeL(e) + puntajeL(f) + puntajeL(g) + puntajeL(h)
    w = puntajeL(i) + puntajeL(j) + puntajeL(k) + puntajeL(l) + puntajeL(m) + puntajeL(n) + puntajeL(o) + puntajeL(p)
    Spuntaje = q + w
    return Spuntaje


hola = 35


def numerosalvaje(a, e, i, m):  # pony salvaje aaah aaah aaaah (8)
    hola = 35
    while hola == 35:
        Rn = random.randint(1, 4)
        if Rn == 1:
            if a == 0:
                a = aleatorio();
                hola = 33  # todo calza D:
            else:
                continue
        if Rn == 2:
            if e == 0:
                e = aleatorio();
                hola = 33  # todo calza D:
            else:
                continue
        if Rn == 3:
            if i == 0:
                i = aleatorio();
                hola = 33  # todo calza D:
            else:
                continue
        if Rn == 4:
            if m == 0:
                m = aleatorio();
                hola = 33  # todo calza D:
            else:
                continue
        return a, e, i, m
        actualizar_tablero()


contadorA, contadorB, contadorC, contadorD = 0, 0, 0, 0


def tarea(tablero):
    global puntaje, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p
    # Aqui empieza tu tarea
    print("Bienvenidos a ThreesUC!, recuerda siempre comprobar si aún quedan movimientos al final del juego...")
    inicia_juego()
    actualizar_tablero()
    contadorA, contadorB, contadorC, contadorD = 0, 0, 0, 0
    while True:
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, contadorA, contadorB, contadorC, contadorD = movimiento(a, b, c,
                                                                                                                d, e, f,
                                                                                                                g, h, i,
                                                                                                                j, k, l,
                                                                                                                m, n, o,
                                                                                                                p,
                                                                                                                contadorA,
                                                                                                                contadorB,
                                                                                                                contadorC,
                                                                                                                contadorD)
        puntaje = int(puntaje_total(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p))
        actualizar_tablero()
        if contadorA >= 1 and contadorB >= 1 and contadorC >= 1 and contadorD >= 1:  # los contadores permiten detectar cuando ya no hay movimientos, si es así, finalizan el juego con un clásico GAME OVER
            a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = 0, 0, 0, 0, "G", "A", "M", "E", "O", "V", "E", "R", 0, 0, 0, 0
            actualizar_tablero()
            print("Gracias por jugar! alcanzaste: %s puntos :)" % (puntaje))
            break

# Aqui termina tu tarea
tablero = tableroGUI.Application("tarea")
tablero.title('DCC - Threes')
tablero.loadProgram(tarea)
tablero.start()
