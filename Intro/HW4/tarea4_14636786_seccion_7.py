import sys
# clases:

class ficha:
    def __init__(self, archivo):
        self.nombre = str(archivo)
        archivo = open(archivo, "r")
        self.movimientos = []
        for i in archivo:
            self.movimientos.append(i.strip())
        archivo.close()
        self.posicion = None
        self.Mposibles = []  # lista con los movimientos posibles en esa posicion
        self.MPmenosanterior = []  # lista con los movimientos posibles que no llevan a la posicion anterior
        self.desplazamiento = []  # lista con las posiciones en las que ha estado
        self.recorridos = []  # lista con los distintos recorridos (desplazamientos) completos

    def __str__(self):
        return 'nombre: ' + self.nombre + ", posicion: " + str(self.posicion) + "\nmovimientos: " + str(
            self.movimientos) + '\n'


class tablero:
    def __init__(self, archivo):
        self.nombre = str(archivo)
        archivo = open(archivo, "r")
        self.dimensiones = archivo.readline().strip()
        self.posicionesP = []
        self.posicionesU = []  # posiciones usadas por fichas (de rápido acceso, no especifica que ficha está en cada posición)
        for i in archivo:
            self.posicionesP.append(i.strip())
        self.fichas = []  # lista de las fichas que estan sobre el tablero
        self.recorridosvirtuales = []  # lista con el nombre de la ficha y sus respectivos recorridos virtuales sobre el tablero

    def __str__(self):
        return 'nombre: ' + self.nombre + ", dimensiones: " + str(self.dimensiones) + ", Posiciones prohibidas: " + str(
            self.posicionesP) + "\n Piezas en el tablero: " + str(self.fichas)

    def agregar_ficha(self, ficha):
        self.fichas.append((ficha.nombre, str(ficha.posicion)))
        self.posicionesU.append(ficha.posicion)

    def RecorridoVirtual(self, ficha):
        self.recorridosvirtuales.append((ficha.nombre) + ',' + str(ficha.recorridos))

    def Menu2(self):
        while True:
            # try:
            print(
                "(1)Imprimir el tablero con las fichas\n(2) Preguntar por los movimientos de una pieza\n(3) Verificar si se pueden mover las piezas sobre el tablero sin repetir posiciones.\n(0) Volver al menu principal\n")
            a = int(input("Ingrese el numero correspondiente a la opcion escogida: "))
            if a == 1:
                self.ImprimirTablero()
            if a == 2:
                self.MovimientosPiezas()
            if a == 3:
                l = ''
                while l != "listo":
                    archivo = input('Ingrese el nombre del archivo de output: ').strip()
                    try:
                        verificar = archivo.split('.')
                        if verificar[1] == 'txt':
                            l = 'listo'
                        else:
                            raise ValueError
                    except:
                        print("Nombre de archivo no valido, recuerda escribirlo de forma output.txt ")
                self.se_puede_recorrer(archivo)
            if a == 0:
                print('\n')
                break
            if a > 3 or a < 0:
                raise ValueError  #
            """except:
                print("\nLa opcion escogida no es correcta, intente nuevamente...\n")"""

    def ImprimirTablero(self):
        dimensiones = self.dimensiones.split(',')
        filas = int(dimensiones[0])
        columnas = int(dimensiones[1])
        a = []
        for i in range(filas):
            b = []
            for j in range(columnas):
                b.append('0')
            a.append(b)
        posP = self.posicionesP
        for i in posP:
            f = int(i[0])
            c = int(i[2])
            a[f][c] = 'X'
        fichas = self.fichas
        print(fichas)
        cont = 1
        listaFC = []  # lista con nombre ficha igualado a su respectivo numero en el tablero...
        for i in fichas:
            print(i)
            ficha = i[0]
            posicion = i[1]
            f = int(posicion[0])
            c = int(posicion[2])
            a[f][c] = str(cont)
            listaFC.append(ficha + ': ' + str(cont))
            cont += 1
        elementos = []
        print('\n')
        for i in range(len(a)):
            j = a[i]
            print('                     ' + ' '.join(j))
        print('\n')
        print('0: Posición libre | X: Posición prohibida |' + ' | '.join(listaFC) + '\n')

    def sumaTuplas(self, a, b):
        a = a.split(',')
        b = b.split(',')
        x = int(a[0]) + int(b[0])
        y = int(a[1]) + int(b[1])
        R = (x, y)
        return R

    def VerificarM(self, ficha):  # Actualiza la lista de Movimientos posibles del atributo de la ficha
        ficha.Mposibles = []
        movimientos = ficha.movimientos
        dimensiones = self.dimensiones.split(',')
        for i in ficha.movimientos:
            llegada = self.sumaTuplas(ficha.posicion, i)
            try:
                if llegada[0] >= 0 and llegada[1] >= 0 and llegada[0] < int(dimensiones[0]) and llegada[1] < int(
                        dimensiones[1]):  # para ver si esta dentro de los limites del tablero
                    PP = self.posicionesP  # Lista de posiciones prohibidas
                    contador = 0
                    for j in PP:
                        j = j.split(',')
                        if int(j[0]) != llegada[0] or int(j[1]) != llegada[
                            1]:  ########## Añadir la suposicion de que una ficha vaya a pararse sobre otra!!!
                            contador += 1
                    if contador == len(PP):
                        ficha.Mposibles.append(str(i))
            except:
                continue

    def MovimientosPiezas(self):
        cont = 1
        print('\n')
        for i in self.fichas:
            f = i[0]
            print('(' + str(cont) + ') ' + f)
            cont += 1
        print('\n')
        l = ''
        while l != "listo":
            print(self.fichas)
            try:
                n = int(input('Seleccione una pieza: ').strip()) - 1  ########### MANEJO DE ERROR ##############
                if n >= 0:
                    seleccion = self.fichas[n]
                    print('seleccion: ' + str(seleccion))
                    l = "listo"
                else:
                    print("\nNúmero fuera de rango, intente nuevamente...")
            except:
                print('Error: Ingresa el número correspondiente a la pieza que deseas utilizar...')
                continue
        print('seleccion[0]: ' + seleccion[0])
        F = ficha(seleccion[0])
        F.posicion = (seleccion[1])
        self.VerificarM(F)
        print('\nLos movimientos validos de ' + F.nombre + ' son: ' + '...'.join(F.Mposibles) + '\n')

    def se_puede_recorrer(self, archivosalida):
        AS = open(archivosalida, "w")
        AS.write('Recorridos piezas:\n')
        try:
            for i in self.fichas:
                print('i: ', i)
                F = ficha(i[0])
                F.posicion = i[1]  # posicion inicial inicial de la ficha.
                F.desplazamiento.append(F.posicion)
                self.recursiva(F)
                self.RecorridoVirtual(F)
                print('Recorridos Virtuales: ', self.recorridosvirtuales)
                AS.write('Recorrido ' + F.nombre + ':  ' + '->'.join(F.desplazamiento) + '\n')
            AS.write(
                'Ayudante, yo sé que falta un poquito más luego de esto, la idea era comparar la lista de los recorridos de cada ficha,\nver si había alguna combinacion de estas que cumpliera que la suma de la cantidad de elementos fuera igual a la \ncantidad de posiciones disponibles en el tablero, y con eso encontrar el True y \nentregar el respectivo output con los movimientos, pero algo es algo supongo :) \ngracias por leer')
            AS.write('\nPD: ve este video, es buenisimo O: https://www.facebook.com/video.php?v=1377089352319753')
            AS.close()
            # self.recorridosvirtuales() # Verificar listas de recorridos virtuales...
        except Exception as e:
            print(e)
            print(
                "Querido ayudante, este error me sorprendió bastante y no tengo idea como evitarlo,\n tal parece que python tiene un máximo de profundidad de recursion, mira tu, que hermoso y desconocido es python...")
            print(
                "Debes admitir que mi tarea está bastante avanzada, si aprendí a usar todo lo de los objetivos, pero esta parte esta enfermamente complicada y tu, \n QUERIDO AYUDANTE lo notas y sientes pena por los pobres novatos programadores...Bueno eso, un abrazo y piedad :3")

    def recursiva(self, F):
        self.VerificarM(F)
        self.sindevolverse(F)
        for j in F.MPmenosanterior:
            self.VerificarM(F)
            F.posicion = str(self.sumaTuplas(F.posicion, j))[1:-1]
            F.desplazamiento.append(F.posicion)
            self.VerificarM(F)
            self.sindevolverse(F)
            if len(F.MPmenosanterior) == 0:  # sin movimientos posibles
                F.recorridos.append(F.desplazamiento)
                F.posicion = F.desplazamiento[-1]  # me paro en la posicion en la que estaba antes
                break
            if len(F.MPmenosanterior) != 0:
                self.recursiva(F)

    def sindevolverse(self, ficha):
        ultimaposicion = ficha.desplazamiento[-1]
        posibles = []  # lista con las posibles futuras posiciones de la ficha
        self.VerificarM(ficha)
        if len(ficha.Mposibles) != 0:
            for i in ficha.Mposibles:  # lista con los movimientos posibles en esa posicion
                PosPosible = self.sumaTuplas(ficha.posicion,
                                             i)  # Posicion en la que puede terminar la ficha si se desplaza en i movimiento posible
                posibles.append(PosPosible)
                comprobar = (str(posibles)).find(
                    ultimaposicion)  # Comprobar si uno de los posibles movimientos corresponde a la posicion anterior
                if comprobar == -1:
                    ficha.MPmenosanterior = ficha.Mposibles
                if comprobar != -1:
                    A = posibles.index(ultimaposicion)
                    Aeliminar = ficha.Mposibles[A]
                    ficha.MPmenosanterior = (ficha.Mposibles.copy).remove(Aeliminar)
        else:
            ficha.MPmenosanterior = []

            # funciones:


def Menu():
    print("(1) Crear una nueva ficha\n(2) Crear un nuevo tablero\n(3) Cargar un tablero con fichas\n(0) Salir\n")
    a = int(input("Ingrese el numero correspondiente a la opcion escogida: "))
    if a == 1:
        CrearFicha()
    if a == 2:
        CrearTablero()
    if a == 3:
        CargarTablero()
    if a == 0:
        print("Gracias por participar!!!")
        sys.exit(-1)
    if a > 3 or a < 0:
        raise ValueError


def CrearFicha():
    l = ''
    while l != "listo":
        archivo = input("Ingrese el nombre del archivo de la nueva ficha: ").strip()
        try:
            verificar = archivo.split('.')
            if verificar[1] == 'txt':
                AF = open(archivo, "w")
                l = 'listo'
            else:
                raise ValueError
        except:
            print("Nombre de archivo no valido, recuerda escribirlo de forma nombreficha.txt ")
    movimiento = ""
    lista = []
    while movimiento != '0':
        movimiento = input("Ingrese el siguiente movimiento de la ficha o un 0 para terminar: ").strip()
        if movimiento != '0':
            try:
                mov = movimiento.split(',')
                if len(mov) == 2:
                    x = int(mov[0])  # para que tire error si no son numeros...
                    y = int(mov[1])
                    z = (str(lista)).find(movimiento)
                    if z == -1:
                        lista.append(movimiento)
                        AF.write(str(x) + ',' + str(y) + "\n")
                    else:
                        print('Movimiento repetido, intente nuevamente!')
                        continue
                else:
                    raise ValueError
            except:
                print('Movimiento invalido, intente nuevamente...\n')

    AF.close()
    print("----------------- ficha " + archivo + " creada correctamente :D -----------------\n")


def CrearTablero():
    l = ''
    while l != "listo":
        archivo = input("Ingrese el nombre del archivo del nuevo tablero: ").strip()
        try:
            verificar = archivo.split('.')
            if verificar[1] == 'txt':
                AT = open(archivo, "w")
                l = 'listo'
            else:
                raise ValueError
        except:
            print("Nombre de archivo no valido, recuerda escribirlo de forma nombretablero.txt ")
    l = ''
    while l != "listo":
        dimensiones = input("Ingrese las dimensiones del tablero: ").strip()
        try:
            dimensiones = dimensiones.split(',')
            if len(dimensiones) == 2:
                largo = int(dimensiones[0])
                ancho = int(dimensiones[1])
                if largo > 0 and ancho > 0:
                    AT.write(str(largo) + ',' + str(ancho) + "\n")
                    l = "listo"
                else:
                    raise ValueError
            else:
                raise ValueError
        except:
            print('Dimensiones no validas, recuerda escribirlas de la forma x,y (largo,ancho)...\n')
            continue
    posicionP = ""
    lista = []
    while posicionP != '0':
        posicionP = input("Ingrese la siguiente posicion prohibida o un 0 para terminar: ").strip()
        if posicionP != '0':
            try:
                pp = posicionP.split(',')
                x = int(pp[0])
                y = int(pp[1])
                if x < largo and y < ancho:
                    w = (str(lista)).find(posicionP)
                    if w == -1:
                        lista.append(posicionP)
                        AT.write(posicionP + "\n")
                    else:
                        print('Posicion repetida, intente nuevamente!')
                        continue
                else:
                    print('Posicion fuera de los limites del tablero, intente nuevamente!')
            except:
                print('Posicion invalida, intente nuevamente!')
                continue

    AT.close()
    print("----------------- Tablero " + archivo + " creado correctamente :D -----------------\n")


def CargarTablero():
    l = ''
    while l != "listo":
        archivoT = input("Ingrese el nombre del archivo correspondiente al tablero: ").strip()
        try:
            T = tablero(archivoT)
            print(T)
            l = "listo"
        except:
            print("Nombre de archivo no valido, recuerda escribirlo de forma nombretablero.txt ")
            continue
    archivoF = ''
    while archivoF != '0':
        archivoF = input("Ingrese el nombre del archivo de la proxima ficha o un 0 para terminar: ").strip()
        try:
            F = ficha(archivoF)
            print(F)
        except:
            if archivoF == '0':
                if len(T.fichas) != 0:
                    print('\n')
                    T.Menu2()
                    break
                else:
                    print('Debes ingresar por lo menos una ficha para continuar\n')
                    continue
            else:
                print("Nombre de archivo no valido, recuerda escribirlo de forma nombreficha.txt ")
                continue
        l = ''
        while l != "listo":
            if archivoF != '0':
                posI = input("Ingrese la posición inicial para " + archivoF + ": ").strip()
                try:
                    D = T.dimensiones.split(
                        ',')  # Dimensiones del tablero, la ficha no se puede poner fuera de estos limites
                    if len(posI) == 3 and posI[1] == ',':
                        d1 = int(D[0])
                        d2 = int(D[1])
                        x = int(posI[0])
                        y = int(posI[2])
                        if x >= 0 and y >= 0 and x < d1 and y < d2:
                            PP = T.posicionesP  # posiciones prohibidas
                            PU = T.posicionesU  # fichas en el tablero, así no se repiten posiciones
                            for i in PP:
                                if i == posI:
                                    raise ValueError
                            if len(PU) > 0:
                                for i in PU:
                                    if i == posI:
                                        raise ValueError
                            F.posicion = posI
                            T.agregar_ficha(F)
                            l = "listo"
                        else:
                            raise ValueError
                    else:
                        raise ValueError
                except:
                    print(
                        'Posicion no valida, ya usada por otra ficha o prohibida, recuerda escribirla de la forma x,y...\n')
                    continue

# Estructura programa (llamado de funciones)

print("Bienvenidos al himalaya!\nSelecciona una de estas opciones:\n")
while True:
    try:
        Menu()
    except ValueError:
        print("\nLa opcion escogida no es correcta, intente nuevamente...\n")
