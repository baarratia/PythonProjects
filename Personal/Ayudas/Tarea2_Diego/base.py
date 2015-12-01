from poker import Tablero, Baraja
from poker import compararJugadas, obtenerApuestaRobot


class Jugador:
    cartas = []
    dinero = 10000
    apuesta = 0

    def __init__(self, cartas=[], dinero=10000, apuesta=0):
        self.cartas = cartas
        self.dinero = dinero
        self.apuesta = apuesta

    def definir_apuesta(self):
        d = 's'
        while d == 's':
            apuesta = int(input('¿Cuánto quieres apostar?  '))
            if apuesta > self.dinero:
                d = 's'
            else:
                d = 'n'
        self.apuesta += apuesta
        return apuesta

    def entregar_dinero(self, controlador, dinero):
        self.dinero = int(self.dinero - dinero)
        controlador.apuesta_mesa += dinero

    def recibir_dinero(self, controlador):
        self.dinero = int(self.dinero + controlador.apuesta_mesa)
        controlador.apuesta_mesa = 0

    def mostrar_cartas(self):
        return self.cartas


class ControlarJuego:
    cartas_mesa = []
    apuesta_mesa = 0

    def __init__(self, cartas_mesa=[], apuesta_mesa=0):
        self.cartas_mesa = cartas_mesa
        self.apuesta_mesa = apuesta_mesa

    def repartir_cartas(self, jugador1, jugador2, baraja):
        for i in range(2):
            carta_nueva_1 = baraja.obtenerCarta()
            jugador1.cartas.append(carta_nueva_1)
        for i in range(2):
            jugador2.cartas.append(baraja.obtenerCarta())

    def repartir_cartas_mesa(self, baraja):
        self.cartas_mesa.append(baraja.obtenerCarta())

    def mostrar_juego(self, tablero, humano, robot, apuesta_robot, apuesta_humano):
        tablero.borrarTablero()
        xi = 10
        yi = 2
        x = xi
        for carta in self.cartas_mesa:
            tablero.dibujarCarta(carta, x, yi)
            x += 10

        tablero.dibujarBorde(xi - 2, yi - 1, 10 * 7 + 1, 8)
        tablero.escribirMensaje("Texas Hold'em", xi + 22, yi - 1)
        tablero.escribirMensaje('Pozo:', xi + 50, yi + 1)
        tablero.escribirMensaje(str(float(self.apuesta_mesa)), xi + 50, yi + 3)

        xi = 10
        yi = 11
        x = xi
        for carta in humano.cartas:
            tablero.dibujarCarta(carta, x, yi)
            x += 10
        tablero.dibujarBorde(xi - 2, yi - 1, 10 * 3 + 5, 8)
        tablero.escribirMensaje(nombre, xi + 2, yi - 1)
        tablero.escribirMensaje('Dinero:' + str(float(humano.dinero)), xi + 19, yi + 2)
        tablero.escribirMensaje('Para igualar: ', xi + 19, yi + 4)
        tablero.escribirMensaje(str(float(robot.apuesta - yo.apuesta)), xi + 19, yi + 5)

        xi = 46
        yi = 11
        x = xi
        for carta in robot.cartas:
            tablero.dibujarCarta(carta, x, yi)
            x += 10
        tablero.dibujarBorde(xi - 2, yi - 1, 10 * 3 + 5, 8)
        tablero.escribirMensaje('Robot', xi + 2, yi - 1)
        tablero.escribirMensaje('Dinero:' + str(float(robot.dinero)), xi + 19, yi + 2)

        return print(tablero)

####
####

# COMIENZA EL JUEGO

####
####

print('Instrucciones: ')
k = ' '
nombre = input('¿Cuál es tu nombre?  ')
while k != '':
    k = input('Presiona <ENTER> para jugar.  ')
yo = Jugador()
robot = Jugador()
tablero = Tablero()
baraja = Baraja()
controlador = ControlarJuego()

jugar = 'si'

while jugar == 'si':
    apostar = True
    while apostar:
        gana = ''
        baraja.barajar()
        yo.cartas = []
        yo.apuesta = 0
        robot.cartas = []
        robot.apuesta = 0
        controlador.cartas_mesa = []
        controlador.repartir_cartas(yo, robot, baraja)
        for i in range(0, 2):
            robot.cartas[i].definirEstado('oculto')

        ##Primera ronda de apuestas  #################################################################
        print('                        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('                        $                             $')
        print('                        $ ¡PRIMERA RONDA DE APUESTAS! $')
        print('                        $                             $')
        print('                        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        while True:
            apuesta_yo = 0
            apuesta_robot = 0
            controlador.mostrar_juego(tablero, yo, robot, robot.apuesta, yo.apuesta)
            while True:
                if robot.apuesta > yo.apuesta:
                    while True:
                        pregunta = input('¿Quieres apostar o retirarte? (apostar/retirarme) ')
                        if pregunta == 'apostar' or pregunta == 'retirarme':
                            break
                        else:
                            print('Solo puedes apostar o retirarte')
                else:
                    pregunta = input('¿Quieres apostar, pasar o retirarte? (apostar/pasar/retirarme) ')
                if pregunta == 'apostar' or pregunta == 'pasar' or pregunta == 'retirarme':
                    break
                print('Debes reponder "apostar", "pasar" o "retirarme"')
            if pregunta == 'apostar':
                while True:
                    apuesta_yo = yo.definir_apuesta()
                    if apuesta_yo > 0:
                        break
                yo.entregar_dinero(controlador, apuesta_yo)
                if yo.apuesta == robot.apuesta:
                    break
                apuesta_robot = obtenerApuestaRobot(robot.cartas, controlador.cartas_mesa, robot.dinero, apuesta_robot,
                                                    apuesta_yo)
                if apuesta_robot > robot.dinero:
                    apuesta_robot = robot.dinero
                if apuesta_robot == apuesta_yo:
                    robot.entregar_dinero(controlador, apuesta_robot)
                    robot.apuesta += apuesta_robot
                    break
                elif apuesta_robot > apuesta_yo:
                    robot.entregar_dinero(controlador, apuesta_robot)
                    robot.apuesta += apuesta_robot
                elif apuesta_robot == 0:
                    gana = 'humano'
                    yo.recibir_dinero(controlador)
                    print('Ganaste esta ronda!')
                    break

            elif pregunta == 'pasar':
                apuesta_robot = obtenerApuestaRobot(robot.cartas, controlador.cartas_mesa, robot.dinero, apuesta_robot,
                                                    apuesta_yo)
                if apuesta_robot > robot.dinero:
                    apuesta_robot = robot.dinero
                if apuesta_robot == apuesta_yo:
                    robot.entregar_dinero(controlador, apuesta_robot)
                    robot.apuesta += apuesta_robot
                    break
                elif apuesta_robot > apuesta_yo:
                    robot.entregar_dinero(controlador, apuesta_robot)
                    robot.apuesta += apuesta_robot
                elif apuesta_robot == 0:
                    gana = 'humano'
                    yo.recibir_dinero(controlador)
                    print('Ganaste esta ronda!')
                    break

            elif pregunta == 'retirarme':
                print('Perdiste esta ronda! :( ')
                gana = 'robot'
                robot.recibir_dinero(controlador)
                break
        if gana == 'humano' or gana == 'robot':
            while True:
                jugar = input('¿Quieres volver a jugar?(si/no) ')
                if jugar == 'no' or jugar == 'si':
                    break
            if jugar == 'no':
                print('Adios!')
            break

        ### SEGUNDA RONDA DE APUESTAS - MOSTRAR 3 CARTAS #################################################################

        print('                        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('                        $                             $')
        print('                        $ ¡SEGUNDA RONDA DE APUESTAS! $')
        print('                        $                             $')
        print('                        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        for i in range(3):
            controlador.repartir_cartas_mesa(baraja)
        while True:
            apuesta_yo = 0
            apuesta_robot = 0
            controlador.mostrar_juego(tablero, yo, robot, robot.apuesta, yo.apuesta)
            while True:
                if robot.apuesta > yo.apuesta:
                    while True:
                        pregunta = input('¿Quieres apostar o retirarte? (apostar/retirarme) ')
                        if pregunta == 'apostar' or pregunta == 'retirarme':
                            break
                        else:
                            print('Solo puedes apostar o retirarte')
                else:
                    pregunta = input('¿Quieres apostar, pasar o retirarte? (apostar/pasar/retirarme) ')
                if pregunta == 'apostar' or pregunta == 'pasar' or pregunta == 'retirarme':
                    break
                print('Debes reponder "apostar", "pasar" o "retirarme"')
            if pregunta == 'apostar':
                while True:
                    apuesta_yo = yo.definir_apuesta()
                    if apuesta_yo > 0:
                        break
                yo.entregar_dinero(controlador, apuesta_yo)
                if yo.apuesta == robot.apuesta:
                    break
                apuesta_robot = obtenerApuestaRobot(robot.cartas, controlador.cartas_mesa, robot.dinero, apuesta_robot,
                                                    apuesta_yo)
                if apuesta_robot > robot.dinero:
                    apuesta_robot = robot.dinero
                if apuesta_robot == apuesta_yo:
                    robot.entregar_dinero(controlador, apuesta_robot)
                    robot.apuesta += apuesta_robot
                    break
                elif apuesta_robot > apuesta_yo:
                    robot.entregar_dinero(controlador, apuesta_robot)
                    robot.apuesta += apuesta_robot
                elif apuesta_robot == 0:
                    gana = 'humano'
                    yo.recibir_dinero(controlador)
                    print('Ganaste esta ronda!')
                    break

            elif pregunta == 'pasar':
                apuesta_robot = obtenerApuestaRobot(robot.cartas, controlador.cartas_mesa, robot.dinero, apuesta_robot,
                                                    apuesta_yo)
                if apuesta_robot > robot.dinero:
                    apuesta_robot = robot.dinero
                if apuesta_robot == apuesta_yo:
                    robot.entregar_dinero(controlador, apuesta_robot)
                    robot.apuesta += apuesta_robot
                    break
                elif apuesta_robot > apuesta_yo:
                    robot.entregar_dinero(controlador, apuesta_robot)
                    robot.apuesta += apuesta_robot
                elif apuesta_robot == 0:
                    gana = 'humano'
                    yo.recibir_dinero(controlador)
                    print('Ganaste esta ronda!')
                    break

            elif pregunta == 'retirarme':
                print('Perdiste esta ronda! :( ')
                gana = 'robot'
                robot.recibir_dinero(controlador)
                break
        if gana == 'humano' or gana == 'robot':
            while True:
                jugar = input('¿Quieres volver a jugar?(si/no) ')
                if jugar == 'no' or jugar == 'si':
                    break
            if jugar == 'no':
                print('Adios!')
            break


        ### TERCERA RONDA DE APUESTAS - MOSTRAR 4 CARTAS #################################################################


        print('                        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('                        $                             $')
        print('                        $ ¡TERCERA RONDA DE APUESTAS! $')
        print('                        $                             $')
        print('                        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        controlador.repartir_cartas_mesa(baraja)
        while True:
            apuesta_yo = 0
            apuesta_robot = 0
            controlador.mostrar_juego(tablero, yo, robot, robot.apuesta, yo.apuesta)
            while True:
                if robot.apuesta > yo.apuesta:
                    while True:
                        pregunta = input('¿Quieres apostar o retirarte? (apostar/retirarme) ')
                        if pregunta == 'apostar' or pregunta == 'retirarme':
                            break
                        else:
                            print('Solo puedes apostar o retirarte')
                else:
                    pregunta = input('¿Quieres apostar, pasar o retirarte? (apostar/pasar/retirarme) ')
                if pregunta == 'apostar' or pregunta == 'pasar' or pregunta == 'retirarme':
                    break
                print('Debes reponder "apostar", "pasar" o "retirarme"')
            if pregunta == 'apostar':
                while True:
                    apuesta_yo = yo.definir_apuesta()
                    if apuesta_yo > 0:
                        break
                yo.entregar_dinero(controlador, apuesta_yo)
                if yo.apuesta == robot.apuesta:
                    break
                apuesta_robot = obtenerApuestaRobot(robot.cartas, controlador.cartas_mesa, robot.dinero, apuesta_robot,
                                                    apuesta_yo)
                if apuesta_robot > robot.dinero:
                    apuesta_robot = robot.dinero
                if apuesta_robot == apuesta_yo:
                    robot.entregar_dinero(controlador, apuesta_robot)
                    robot.apuesta += apuesta_robot
                    break
                elif apuesta_robot > apuesta_yo:
                    robot.entregar_dinero(controlador, apuesta_robot)
                    robot.apuesta += apuesta_robot
                elif apuesta_robot == 0:
                    gana = 'humano'
                    yo.recibir_dinero(controlador)
                    print('Ganaste esta ronda!')
                    break

            elif pregunta == 'pasar':
                apuesta_robot = obtenerApuestaRobot(robot.cartas, controlador.cartas_mesa, robot.dinero, apuesta_robot,
                                                    apuesta_yo)
                if apuesta_robot > robot.dinero:
                    apuesta_robot = robot.dinero
                if apuesta_robot == apuesta_yo:
                    robot.entregar_dinero(controlador, apuesta_robot)
                    robot.apuesta += apuesta_robot
                    break
                elif apuesta_robot > apuesta_yo:
                    robot.entregar_dinero(controlador, apuesta_robot)
                    robot.apuesta += apuesta_robot
                elif apuesta_robot == 0:
                    gana = 'humano'
                    yo.recibir_dinero(controlador)
                    print('Ganaste esta ronda!')
                    break

            elif pregunta == 'retirarme':
                print('Perdiste esta ronda! :( ')
                gana = 'robot'
                robot.recibir_dinero(controlador)
                break
        if gana == 'humano' or gana == 'robot':
            while True:
                jugar = input('¿Quieres volver a jugar?(si/no) ')
                if jugar == 'no' or jugar == 'si':
                    break
            if jugar == 'no':
                print('Adios!')
            break

            ### CUARTA RONDA DE APUESTAS - MOSTRAR 5 CARTAS #################################################################

        print('                        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        print('                        $                              $')
        print('                        $  ¡CUARTA RONDA DE APUESTAS!  $')
        print('                        $                              $')
        print('                        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
        controlador.repartir_cartas_mesa(baraja)
        while True:
            apuesta_yo = 0
            apuesta_robot = 0
            controlador.mostrar_juego(tablero, yo, robot, robot.apuesta, yo.apuesta)
            while True:
                if robot.apuesta > yo.apuesta:
                    while True:
                        pregunta = input('¿Quieres apostar o retirarte? (apostar/retirarme) ')
                        if pregunta == 'apostar' or pregunta == 'retirarme':
                            break
                        else:
                            print('Solo puedes apostar o retirarte')
                else:
                    pregunta = input('¿Quieres apostar, pasar o retirarte? (apostar/pasar/retirarme) ')
                if pregunta == 'apostar' or pregunta == 'pasar' or pregunta == 'retirarme':
                    break
                print('Debes reponder "apostar", "pasar" o "retirarme"')
            if pregunta == 'apostar':
                while True:
                    apuesta_yo = yo.definir_apuesta()
                    if apuesta_yo > 0:
                        break
                yo.entregar_dinero(controlador, apuesta_yo)
                if yo.apuesta == robot.apuesta:
                    break
                apuesta_robot = obtenerApuestaRobot(robot.cartas, controlador.cartas_mesa, robot.dinero, apuesta_robot,
                                                    apuesta_yo)
                if apuesta_robot > robot.dinero:
                    apuesta_robot = robot.dinero
                if apuesta_robot == apuesta_yo:
                    robot.entregar_dinero(controlador, apuesta_robot)
                    robot.apuesta += apuesta_robot
                    break
                elif apuesta_robot > apuesta_yo:
                    robot.entregar_dinero(controlador, apuesta_robot)
                    robot.apuesta += apuesta_robot
                elif apuesta_robot == 0:
                    gana = 'humano'
                    yo.recibir_dinero(controlador)
                    print('Ganaste esta ronda!')
                    break

            elif pregunta == 'pasar':
                apuesta_robot = obtenerApuestaRobot(robot.cartas, controlador.cartas_mesa, robot.dinero, apuesta_robot,
                                                    apuesta_yo)
                if apuesta_robot > robot.dinero:
                    apuesta_robot = robot.dinero
                if apuesta_robot == apuesta_yo:
                    robot.entregar_dinero(controlador, apuesta_robot)
                    robot.apuesta += apuesta_robot
                    break
                elif apuesta_robot > apuesta_yo:
                    robot.entregar_dinero(controlador, apuesta_robot)
                    robot.apuesta += apuesta_robot
                elif apuesta_robot == 0:
                    gana = 'humano'
                    yo.recibir_dinero(controlador)
                    print('Ganaste esta ronda!')
                    break

            elif pregunta == 'retirarme':
                print('Perdiste esta ronda! :( ')
                gana = 'robot'
                robot.recibir_dinero(controlador)
                break
        if gana == 'humano' or gana == 'robot':
            while True:
                jugar = input('¿Quieres volver a jugar?(si/no) ')
                if jugar == 'no' or jugar == 'si':
                    break
            if jugar == 'no':
                print('Adios!')
            break
        resultado = compararJugadas(yo.cartas, robot.cartas, controlador.cartas_mesa)
        if resultado == 'empate':
            print('Empate')
            robot.dinero += (controlador.apuesta_mesa) / 2
            yo.dinero += (controlador.apuesta_mesa) / 2
            controlador.apuesta_mesa = 0
        elif resultado == 'gana_humano':
            print('Ganaste!!')
            yo.dinero += controlador.apuesta_mesa
            controlador.apuesta_mesa = 0
        elif resultado == 'gana_robot':
            print('Perdiste :( ')
            robot.dinero += controlador.apuesta_mesa
            controlador.apuesta_mesa = 0
        for i in range(0, 2):
            robot.cartas[i].definirEstado('visible')
        controlador.mostrar_juego(tablero, yo, robot, robot.apuesta, yo.apuesta)
        while True:
            jugar = input('¿Quieres volver a jugar? (si/no)  ')
            if jugar == 'si' or jugar == 'no':
                break
        if jugar == 'no':
            print('Adiós!')
        break
