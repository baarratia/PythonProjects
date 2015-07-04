from math import *
from copy import *

from instaintro_gui import *


# mis funciones
def ByN(a):
    lista1 = []
    for i in range(len(a)):
        fila = a[i]
        lista2 = []
        for j in range(len(fila)):
            pixel = fila[j]
            pixel = list(pixel)
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            promedio = (r + g + b) / 3
            pixel[0] = promedio
            pixel[1] = promedio
            pixel[2] = promedio
            pixel = tuple(pixel)
            lista2.append(pixel)
        lista1.append(lista2)
    return lista1


def convolucion(A, B):
    lista1 = []
    for i in range(len(A)):
        fila = A[i]
        lista2 = []
        for j in range(len(fila)):
            r = 0
            g = 0
            b = 0
            for k in range(3):
                for l in range(3):
                    if (i + k - 1) <= (len(A) - 1) and (j + l - 1) <= (len(fila) - 1):
                        r += B[k][l] * A[i + k - 1][j + l - 1][0]
                        g += B[k][l] * A[i + k - 1][j + l - 1][1]
                        b += B[k][l] * A[i + k - 1][j + l - 1][2]
                        pixel = (r, g, b)
            lista2.append(pixel)
        lista1.append(lista2)
    return lista1


def completar(A):  # Hacer que A tenga filas y columnas multiplos de 5
    A1 = copy(A)
    if ((len(A1)) % 5) != 0:
        FF = A[len(A1) - 1]
        for i in range(5 - (len(A1)) % 5):
            A1.append(FF)
    A2 = copy(A1)
    for i in range(len(A2)):
        if ((len(A2[i])) % 5) != 0:
            FF = A1[i][(len(A1[i])) - 1]
            T = (len(A2[i]) % 5)
            for j in range(5 - T):
                A2[i].append(FF)
    return A2


def SyO_mosaicos(A, B):  # seleccionar y ordenar mosaicos
    M = []
    for h in range(int(len(A) / 5)):
        for e in range(int(len(A[h]) / 5)):
            lista = []
            for g in range(len(B)):
                mos = B[g]
                diff = 0
                for i in range(5):
                    for j in range(5):
                        I = 5 * h + i
                        J = 5 * e + j
                        rM = mos[i][j][0]
                        gM = mos[i][j][1]
                        bM = mos[i][j][2]
                        r = A[I][J][0]
                        g = A[I][J][1]
                        b = A[I][J][2]
                        diff += (rM - r) ** 2 + (gM - g) ** 2 + (bM - b) ** 2
                lista.append(diff)
            pms = lista.index(min(lista))
            S = B[pms]
            M.append(S)
    return M


def ordenar(A, M):
    IM = []
    for i in range(int(len(A) / 5)):
        for j in range(5):
            lista = []
            n = 0
            for h in range(int(len(A[0]) / 5)):
                fila = M[i * (int(len(A[0]) / 5)) + h][j]
                lista += fila
            IM.append(lista)
    return IM


def acuoso(A):
    Ag = ByN(A)
    lista1 = []
    for i in range(len(Ag)):
        lista2 = []
        for j in range(len(Ag[i])):
            n = 0
            if i != 0 or j != 0 or i != (len(A) - 1) or j != (len(A[i]) - 1):
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if k < len(Ag) and l < len(Ag[0]):
                            n += Ag[k][l][0]
                n = n / 9
                pix = (0, n, n)
            else:
                pix = A[i][j]
            lista2.append(pix)
        lista1.append(lista2)
    return lista1


def tarea():  # Aqui empieza tu tarea
    while True:
        click = esperar_click()
        if click == "gris":
            a = obtener_pixeles()
            gris = ByN(a)
            actualizar_imagen(gris)
        if click == "girar":
            a = obtener_pixeles()
            lista1 = []
            c = 0
            while c <= (len(a[0]) - 1):
                lista2 = []
                for i in range(len(a)):
                    pixel = a[-i][c]
                    lista2.append(pixel)
                lista1.append(lista2)
                c += 1
            actualizar_imagen(lista1)
        if click == "bordes":  # Ayudante, paciencia, se demora un poco
            a = obtener_pixeles()
            A = ByN(a)
            Bx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
            By = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
            Gx = convolucion(A, Bx)
            Gy = convolucion(A, By)
            lista1 = []
            for i in range(len(A)):
                lista2 = []
                for j in range(len(A[0])):
                    r1 = Gx[i][j][0]
                    g1 = Gx[i][j][1]
                    b1 = Gx[i][j][2]
                    r2 = Gy[i][j][0]
                    g2 = Gy[i][j][1]
                    b2 = Gy[i][j][2]
                    r = sqrt((r1 ** 2) + (r2 ** 2))
                    g = sqrt((g1 ** 2) + (g2 ** 2))
                    b = sqrt((b1 ** 2) + (b2 ** 2))
                    pixel = (r, g, b)
                    lista2.append(pixel)
                lista1.append(lista2)
            G = lista1
            actualizar_imagen(G)
        if click == "mosaico":  # Ayudante, paciencia, se demora harto
            A = obtener_pixeles()
            B = obtener_imagenes_mosaico()
            AC = completar(A)
            LM = SyO_mosaicos(AC, B)  # lista de los mosaicos seleccionados y ordenados.
            IM = ordenar(AC, LM)  # pasar la lista de mosaicos para que forme la imagen buscada 1313
            actualizar_imagen(IM)

        if click == "salir":
            A = obtener_pixeles()
            IM = acuoso(A)
            actualizar_imagen(IM)
            # salir()


app = Application("tarea")
app.title('InstaIntro')
app.loadProgram(tarea)
app.start()
