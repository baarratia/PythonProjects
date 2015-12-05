import math

from Automata import angulo, distancia


class Robot:
    def __init__(self, enemigo):
        self.x = ''
        self.y = ''
        self.x2 = ''
        self.y2 = ''
        self.a1 = ''
        self.px = ''
        self.py = ''
        self.arco = []
        self.arco_enemigo = []
        self.pelota = False
        self.goles = 0
        self.modo = 'Balon'
        self.enemigo = enemigo

    def set_inicio(self, arco, arco_enemigo):
        self.arcox = (arco[0][0] + arco[1][0]) / 2
        self.arcoy = (arco[0][1] + arco[1][1]) / 2
        self.arco_enemigox =  (arco_enemigo[0][0] + arco_enemigo[1][0]) / 2
        self.arco_enemigoy = (arco_enemigo[0][1] + arco_enemigo[1][1])/ 2

    def actualizar(self, x, y, x2, y2, px, py):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.angulo()
        self.tenerpelota(px, py)
        if self.pelota is False:
            if self.enemigo.pelota is False:
                self.modo = 'Balon'
                a=math.radians(angulo(px,py,self.arco_enemigox,self.arco_enemigoy))
                puntoairx=px-math.cos(a)*50
                puntoairy=py-math.sin(a)*50
                if distancia(self.x, self.y, puntoairx,  puntoairy) > 20:
                    data = self.ir(puntoairx, puntoairy)
                else:
                    data = self.ir(px, py)

            else:
                self.modo = 'Defender'
                if distancia(self.x, self.y, self.arcox, self.arcoy) > 60:
                    data = self.ir(self.arcox, self.arcoy)
            else:
                data = self.orientar(px, py)
        else:
            self.modo = 'Atacar'



    def tenerpelota(self, px, py):
        a = math.radians(self.a1)
        dis = 30
        pointx = self.x2 + math.cos(a) * dis
        pointy = self.y2 + math.sin(a) * dis

        if distancia(pointx, pointy, px, py) < 15:
            self.pelota = True
        else:
            self.pelota = False

    def set_pelota(self, b):
        self.pelota = b

    def set_modo(self, modo):
        self.modo = modo

    def gol(self):
        self.gol += 1

    def angulo(self):
        self.a1 = angulo(self.x, self.y, self.x2, self.y2)

    def orientar(self, p1, p2):
        a2 = angulo(self.x, self.y, p1, p2)
        amplitud = 25
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
                return 100, 100, 0
            else:
                return 0, 0, 0
        elif -(a2 - self.a1) > amplitud:
            print(self.a1, a2)
            return pg, pg, 2

        elif a2 - self.a1 > amplitud:
            print(self.a1, a2)
            return pg, pg, 3
