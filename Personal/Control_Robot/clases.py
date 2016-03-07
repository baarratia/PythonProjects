__author__ = 'Benja'
import math
from Comunicador import Comunicador_Robot
import time
from Automata import angulo, distancia
comunicacion = Comunicador_Robot()

class Robot:
    def __init__(self, enemigo=None, activo=False):
        self.enemigo = enemigo
        self.x = 0
        self.y = 0
        self.x2 = 0
        self.y2 = 0
        self.a1 = 0
        self.px = 0
        self.py = 0
        self.arco = []
        self.arco_enemigo = []
        self.arcox = 98
        self.arcoy = 221
        self.arco_enemigox = 627
        self.arco_enemigoy = 192
        self.activo = activo
        self.pausa = True
        self.pelota = False
        self.goles = 0
        self.modo = 'Balon'
        self.llego = False
        #self.
        '''
        self.enemigo = enemigo
        self.TCP_IP = '192.168.0.139'  # Conexi�n IP del modulo WiFly al cual se conectar�
        self.TCP_PORT = 2000  # Puerto al cual se enviar� la informaci�n
        self.BUFFER_SIZE = 20  # Tama�o del buffer que almacena la informaci�n enviada
        self.MESSAGE = "Listo"
        self.PASS = b"G02"  # Password de su modulo inal�mbrico
        self.CONNECTED = False
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.TCP_IP, self.TCP_PORT))
        self.conectar()

    def conectar(self):
        while True:
            data = self.s.recv(self.BUFFER_SIZE)
            #data = data.decode('utf-8')
            print("received data:", data)
            if data == "PASS?":
                self.s.send(self.PASS)

            elif data == "AOK":
                self.CONNECTED = True
                break

            else:
                self.CONNECTED = False
                break

    def escuchar_enviar(self, data):
        data = str(data)
        if self.CONNECTED:
            MESSAGE = data.encode('utf-8')
            self.s.send(MESSAGE)
            print(data)'''

    def set_inicio(self, arco, arco_enemigo):
        self.arcox = (arco[0][0] + arco[1][0]) / 2
        self.arcoy = (arco[0][1] + arco[1][1]) / 2
        self.arco_enemigox = (arco_enemigo[0][0] + arco_enemigo[1][0]) / 2
        self.arco_enemigoy = (arco_enemigo[0][1] + arco_enemigo[1][1]) / 2
        print('arcos!!')

    def actualizar(self, x, y, x2, y2, px, py):
        if self.pausa is False:
            print('hola')
            self.x = x
            self.y = y
            self.x2 = x2
            self.y2 = y2
            self.px = px
            self.py = py
            self.angulo()
            self.tenerpelota(px, py)
            if self.activo is True and self.pelota is False:
                if self.enemigo.pelota is False:
                    dist1 = 80
                    dist2 = 80
                    self.modo = 'Balon'
                    if 90 <= angulo(self.x2, self.y2, px, py) <= 270:
                        a = math.radians(angulo(self.px, py, self.arco_enemigox, self.arco_enemigoy))
                        puntoairx = px - math.cos(a) * dist2
                        puntoairy = py - math.sin(a) * dist2
                        if distancia(self.x, self.y, puntoairx, puntoairy) > 20 and self.llego is False:
                            data = self.ir(puntoairx, puntoairy)
                            comunicacion.escuchar_enviar(data)
                        else:
                            self.llego = True
                        if self.llego is True:
                            if distancia(self.x2, self.y2, self.px, self.py) > 20:
                                data = self.ir(px, py)
                                comunicacion.escuchar_enviar(data)
                                self.tenerpelota(px, py)
                            else:
                                self.llego = False
                                data = 200, 200, 0
                                comunicacion.escuchar_enviar(data)
                                time.sleep(2)
                                data = 0, 0 , 0
                                comunicacion.escuchar_enviar(data)
                                self.modo = 'Atacar'
                    else:
                        a = math.radians(angulo(self.px, self.py, self.arco_enemigox, self.arco_enemigoy))
                        if self.py <= 250:
                            print(a)
                            puntoairx = self.px - math.cos(a) * dist1
                            puntoairy = self.py + math.sin(a) * dist1
                            data = self.ir(puntoairx, puntoairy)
                            comunicacion.escuchar_enviar(data)
                            #puntoairx2 = self.px + math.cos(a - math.radians(90)) * dist2
                            #puntoairy2 = self.py - math.sin(a - math.radians(90)) * dist2
                            #hacer que compruebe cuando llega al punto a ir x,y para que pase a ir al punto
                            # de atras de la pelota.

                        else:
                            print(a)
                            puntoairx = self.px - math.cos(a) * dist1
                            puntoairy = self.py + math.sin(a) * dist1
                            data = self.ir(puntoairx, puntoairy)
                            #puntoairx2 = self.px + math.cos(a + math.radians(90)) * dist2
                            #puntoairy2 = self.py3 - math.sin(a + math.radians(90)) * dist2
                            comunicacion.escuchar_enviar(data)


                else:
                    self.modo = 'Defender'
                    if distancia(self.x, self.y, self.arcox, self.arcoy) > 60:
                        data = self.ir(self.arcox, self.arcoy)
                    else:
                        #if  self.a < 15 or self.a > 345:
                            #self.orientar(self.x, self.y + 50)
                        #else:
                            #if self.y - self.py > 0:
                                #data = 100, 100, 1
                            #else:
                                #data = 100, 100, 0
                        data = self.orientar(px, py)
                        comunicacion.escuchar_enviar(data)
            else:
                if self.pelota is True:
                    self.modo = 'Atacar'
                    if distancia(self.x, self.y, self.arco_enemigox, self.arco_enemigoy) > 150:
                        data = self.ir(self.arco_enemigox, self.arco_enemigoy)
                    else:
                        '''data = 200, 200, 0
                        comunicacion.escuchar_enviar(data)
                        time.sleep(2)
                        data = 0, 0 , 0
                        comunicacion.escuchar_enviar(data)

                        '''
                        data = self.orientar(self.px, self.py)
                        comunicacion.escuchar_enviar(data)
                        if abs(self.a1 - angulo(self.x2, self.y2, self.px, self.py)) < 7:
                            data = 0, 0, 0
                            comunicacion.escuchar_enviar(data)
                            data = self.orientar(self.px, self.py)
                            comunicacion.escuchar_enviar(data)
                            if abs(self.a1 - angulo(self.x2, self.y2, self.px, self.py)) < 6:
                                data = 200, 200, 0
                                comunicacion.escuchar_enviar(data)
                                time.sleep(3)
                                data = 0, 0, 0
                                comunicacion.escuchar_enviar(data)
                        else:
                            data = self.orientar(self.px, self.py)
                            comunicacion.escuchar_enviar(data)

            print(self.modo)

    def tenerpelota(self, px, py):
        a = math.radians(self.a1)
        dis = 30
        pointx = self.x2 + math.cos(a) * dis
        pointy = self.y2 + math.sin(a) * dis

        if distancia(pointx, pointy, px, py) < 15:
            self.pelota = True
            self.modo = 'Balon'
        else:
            self.pelota = False
            self.modo = 'Balon'

    def Pausa(self):
        if self.pausa is True:
            self.pausa = False
        else:
            self.pausa = True

    def gol(self):
        self.gol += 1

    def angulo(self):
        self.a1 = angulo(self.x, self.y, self.x2, self.y2)

    def orientar(self, p1, p2):
        a2 = angulo(self.x, self.y, p1, p2)
        amplitud = 5
        pg = 85
        if abs(a2 - self.a1) <= amplitud:
            return 0, 0, 0

        elif -(a2 - self.a1) > amplitud:
            print(self.a1, a2)
            return pg, pg, 2

        elif a2 - self.a1 > amplitud:
            print(self.a1, a2)
            return pg, pg, 3

    def ir(self, x3, y3):
        a2 = angulo(self.x, self.y, x3, y3)
        print(self.a1, a2)
        amplitud = 10
        pg = 85

        d = distancia(self.x, self.y, x3, y3)
        if abs(a2 - self.a1) <= amplitud:
            if d > 30:
                return 150, 150, 0
            else:
                data = self.orientar(self.px, self.py)
                comunicacion.escuchar_enviar(data)
                if abs(self.a1 - angulo(self.x, self.y, self.px, self.py)) < 15:
                    data = 200, 200, 0
                    comunicacion.escuchar_enviar(data)
                    time.sleep(3)
                    data = 0, 0, 0
                    comunicacion.escuchar_enviar(data)
                else:
                    data = self.orientar(self.px, self.py)
                    comunicacion.escuchar_enviar(data)
                    #time.sleep(0.3)
                #return 0, 0, 0
        elif -(a2 - self.a1) > amplitud:
            print(self.a1, a2)
            return pg, pg, 2

        elif a2 - self.a1 > amplitud:
            print(self.a1, a2)
            return pg, pg, 3
