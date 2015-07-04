# -*- coding: utf-8 -*-
import time
import random

from PyQt4 import QtCore, QtGui


class Personaje(QtCore.QThread):
    trigger = QtCore.pyqtSignal(object)
    personajes = []
    Monedas = 0 #Contador Monedas atrapadas por personajes
    def __init__(self, parent=None):
        super(Personaje, self).__init__(parent)
        self.running = None
        self.memory = None
        self.pausa = False
        self.mempausa = None
        Personaje.personajes.append(self)

    def setup(self, pic, mapa, pacman=None, pix = None, puerta = None):
        self.pic = pic
        self.pix = pix #pix original
        self.x = pic.x()
        self.y = pic.y()
        self.x1 = self.x  #Posiciones iniciales, sirve para cuando pacman pierde una vida y los personajes vuelven
        self.y1 = self.y  #a su posicion inicial
        self.mapa = mapa
        self.dic = {'Left': 'self.mapa[self.y // 3][self.x // 3 - 1]', 'Up': 'self.mapa[self.y // 3 - 1][self.x // 3]',
                    'Right': 'self.mapa[self.y // 3][self.x // 3 + 1]',
                    'Down': 'self.mapa[self.y // 3 + 1][self.x // 3]'}
        self.pacman = pacman
        self.puerta = puerta

    def mover(self):
        if self.running == 'Left':
            if self.mapa[self.y // 3][self.x // 3 - 1] != '0':
                if self.mapa[self.y // 3][self.x // 3 - 1] == '8':
                    self.x = 227 * 3
                else:
                    self.x -= 1
        elif self.running == 'Up':
            if self.mapa[self.y // 3 - 1][self.x // 3] != '0':
                self.y -= 1
        elif self.running == 'Right':
            if self.mapa[self.y // 3][self.x // 3 + 1] != '0':
                if self.mapa[self.y // 3][self.x // 3 + 1] == '8':
                    self.x = 0
                else:
                    self.x += 1
        elif self.running == 'Down':
            if self.mapa[self.y // 3 + 1][self.x // 3] != '0':
                self.y += 1

    def pausar(self):
        if self.pausa:
            self.pausa = False
            self.running = self.mempausa
        else:
            self.pausa = True
            self.mempausa = self.running
            self.running = None

    def reiniciar_posicion(self):
        self.x = self.x1
        self.y = self.y1
        self.trigger.emit((self.x - 15, self.y - 15, self))

class Pacman(Personaje):
    def __init__(self, parent=None):
        super(Pacman, self).__init__(parent)
        self.recorrido = []
        self.puntaje = 0
        self.estado = True
        self.vidas = 3
        self.superpacman = False

    def run(self):
        while self.estado:
            if not self.pausa:
                self.mover()
                if self.mapa[self.y // 3][self.x // 3] == '2':
                    self.puntaje += 1
                    Personaje.Monedas += 1
                    self.mapa[self.y // 3][self.x // 3] = '1'
                elif self.mapa[self.y // 3][self.x // 3] == '7':
                    Personaje.Monedas += 1
                    self.puntaje += 10
                    if self.vidas < 5:
                        self.vidas += 1
                    self.SuperPacman()
                    self.mapa[self.y // 3][self.x // 3] = '1'
                self.recorrido.append((self.x, self.y))
                self.trigger.emit((self.x - 15, self.y - 15))
                time.sleep(0.008)
                self.ApagarSuperPacman()
                self.cambiar_destino()

    def SuperPacman(self):
        if not self.superpacman:
            self.superpacman = True
            self.t = time.clock()
            for i in Fantasma.fantasmas:
                i.Escapar()
        else:
            self.t += 1

    def ApagarSuperPacman(self):
        if self.superpacman:
            if time.clock() - self.t >= 10:
                self.superpacman = False
                for i in Fantasma.fantasmas:
                    i.Escapar()

    def direction(self, key):
        self.memory = None
        if key == QtCore.Qt.Key_Left:
            if self.mapa[self.y // 3][self.x // 3 - 1] != '0':
                self.running = 'Left'
            else:
                self.memory = 'Left'
        elif key == QtCore.Qt.Key_Up:
            if self.mapa[self.y // 3 - 1][self.x // 3] != '0':
                self.running = 'Up'
            else:
                self.memory = 'Up'
        elif key == QtCore.Qt.Key_Right:
            if self.mapa[self.y // 3][self.x // 3 + 1] != '0':
                self.running = 'Right'
            else:
                self.memory = 'Right'
        elif key == QtCore.Qt.Key_Down:
            if self.mapa[self.y // 3 + 1][self.x // 3] != '0':
                self.running = 'Down'
            else:
                self.memory = 'Down'

    def cambiar_destino(self):
        if self.memory is not None:
            if eval(self.dic[self.memory]) != '0':
                self.running = self.memory

class Fantasma(Personaje):
    trigg = QtCore.pyqtSignal(object)
    menosvida = QtCore.pyqtSignal(object)
    fantasmas = []

    def __init__(self, parent=None):
        super(Fantasma, self).__init__(parent)
        Fantasma.fantasmas.append(self)
        self.estado = True # si es True persigue, si es False, se escapa.
        self.muerto = False #Si es False hace todo normal, si es True, pacman lo ha atrapado, por lo que corre a la base

    def Nosedevuelve(self):  # Funcion de movimiento para fantasma tonto
        if self.running == 'Up' or self.running == 'Down':
            if (self.mapa[self.y // 3][self.x // 3 + 1] != '0') and (self.mapa[self.y // 3][self.x // 3 - 1] != '0'):
                self.running = random.choice(('Left', 'Right'))
            elif self.mapa[self.y // 3][self.x // 3 + 1] != '0':
                self.running = 'Right'
            elif self.mapa[self.y // 3][self.x // 3 - 1] != '0':
                self.running = 'Left'
        else:
            if (self.mapa[self.y // 3 + 1][self.x // 3]) != '0' and (self.mapa[self.y // 3 - 1][self.x // 3] != '0'):
                self.running = random.choice(('Up', 'Down'))
            elif self.mapa[self.y // 3 + 1][self.x // 3] != '0':
                self.running = 'Down'
            elif self.mapa[self.y // 3 - 1][self.x // 3] != '0':
                self.running = 'Up'

    def EscaparInteligente(self):
        posibilidades = {}
        if self.mapa[self.y // 3][self.x // 3 - 1] != '0' and (self.pacman.x - self.x > 0) and self.running != 'Right':
            posibilidades[abs(self.pacman.x - self.x)] = 'Left'
        if self.mapa[self.y // 3 - 1][self.x // 3] != '0' and (
                self.pacman.y - self.y > 0) and self.running != 'Down':
            posibilidades[abs(self.pacman.y - self.y)] ='Up'
        if self.mapa[self.y // 3][self.x // 3 + 1] != '0' and (self.pacman.x - self.x < 0) and self.running != 'Left':
            posibilidades[abs(self.pacman.x - self.x)] = 'Right'
        if self.mapa[self.y // 3 + 1][self.x // 3] != '0' and (self.pacman.y - self.y < 0) and self.running != 'Up':
            posibilidades[abs(self.pacman.y - self.y)] = 'Down'
        if len(posibilidades) > 0:
            self.running = posibilidades[max(posibilidades)]
        else:
            self.Nosedevuelve()

    def Atrapar(self):
        if abs(self.pacman.x - self.x) < 5 and abs(self.pacman.y - self.y) < 5:
            if self.estado:
                self.pacman.estado = False
                self.pacman.running = None
                self.running = None
                self.menosvida.emit(self)
            else:
                self.muerto = True
                self.trigg.emit(self)

    def Base(self):
        v = random.randint(7, 15)
        s = time.time()
        c = 0
        while time.time() - s < v:
            if c%2 == 0:
                self.trigger.emit((self.x, self.y - 10, self))
            else:
                self.trigger.emit((self.x, self.y + 10, self))
            time.sleep(0.009)
            c += 1
        while True:
            self.y -= 1
            self.trigger.emit((self.x - 15, self.y - 15, self))
            time.sleep(0.009)
            if self.mapa[self.y // 3][self.x // 3] != '0':
                break

    def HuirABase(self):

        if self.x - self.puerta[0]*3 > 0:
            q = 'Restar'
        else:
            q = 'Sumar'
        if self.y - self.puerta[1]*3 > 0:
            w = 'Restar'
        else:
            w = 'Sumar'
        e = 0
        rr = random.randint(-40, 40)
        while e != 2:
            if self.x != (self.puerta[0]*3 + rr):
                if q == 'Sumar':
                    self.x += 1
                if q == 'Restar':
                    self.x -= 1
            if self.y != (self.puerta[1]*3 + 40):
                if w == 'Sumar':
                    self.y += 1
                if w == 'Restar':
                    self.y -= 1
            if self.x == self.puerta[0]*3 + rr and self.y == self.puerta[1]*3 + 40:
                e = 2
            self.trigger.emit((self.x, self.y - 10, self))
            time.sleep(0.008)
        self.Base()
        self.reboot()

    def reboot(self):
        self.running = random.choice(('Left', 'Right'))
        self.muerto = False
        self.estado = True
        self.trigg.emit(self)

    def Escapar(self):
        if self.estado:
            self.estado = False
            self.trigg.emit(self)
        else:
            if not self.muerto:
                self.estado = True
                self.trigg.emit(self)

class FantasmaRojo(Fantasma):
    def __init__(self, parent=None):
        super(FantasmaRojo, self).__init__(parent)
        self.running = random.choice(('Left', 'Right'))

    def run(self):
        while self.pacman.estado:
            posibilidades = []
            for i in self.dic:
                if eval(self.dic[i]) != '0':
                    posibilidades.append('1')
                else:
                    posibilidades.append('0')
            self.mover()
            self.Atrapar()
            r = []
            for i in self.dic:
                if eval(self.dic[i]) != '0':
                    r.append('1')
                else:
                    r.append('0')
            if not self.muerto:
                if self.estado:
                    if posibilidades != r:
                        self.perseguir()
                else:
                    self.EscaparInteligente()
            else:
                self.HuirABase()
            self.trigger.emit((self.x - 15, self.y - 15, self))
            time.sleep(0.0064)

    def perseguir(self):
        posibilidades = {}
        if self.mapa[self.y // 3][self.x // 3 - 1] != '0' and (self.pacman.x - self.x < 0) and self.running != 'Right':
            posibilidades[abs(self.pacman.x - self.x)] = 'Left'
        if self.mapa[self.y // 3 - 1][self.x // 3] != '0' and (
                self.pacman.y - self.y < 0) and self.running != 'Down':
            posibilidades[abs( self.pacman.y - self.y)] = 'Up'
        if self.mapa[self.y // 3][self.x // 3 + 1] != '0' and (self.pacman.x - self.x > 0) and self.running != 'Left':
            posibilidades[abs(self.pacman.x - self.x)] = 'Right'
        if self.mapa[self.y // 3 + 1][self.x // 3] != '0' and (self.pacman.y - self.y > 0) and self.running != 'Up':
            posibilidades[abs(self.pacman.y - self.y)] = 'Down'
        if len(posibilidades) > 0:
            self.running = posibilidades[min(posibilidades)]
        else:
            self.NosedevuelveInteligente()

    def NosedevuelveInteligente(self):
        if self.running == 'Up' or self.running == 'Down':
            if (self.mapa[self.y // 3][self.x // 3 + 1] != '0') and (self.mapa[self.y // 3][self.x // 3 - 1] != '0'):
                posibilidades = {}
                posibilidades[abs(self.pacman.x - self.x)] = 'Left'
                posibilidades[abs(self.pacman.x - self.x)] = 'Right'
                self.running = posibilidades[min(posibilidades)]
            else:
                if self.mapa[self.y // 3][self.x // 3 + 1] != '0':
                    self.running = 'Right'
                elif self.mapa[self.y // 3][self.x // 3 - 1] != '0':
                    self.running = 'Left'
        else:
            if (self.mapa[self.y // 3 + 1][self.x // 3]) != '0' and (self.mapa[self.y // 3 - 1][self.x // 3] != '0'):
                posibilidades = {}
                posibilidades[abs(self.pacman.y - self.y)] = 'Down'
                posibilidades[abs(self.pacman.y - self.y)] = 'Up'
                self.running = posibilidades[min(posibilidades)]
            elif self.mapa[self.y // 3 + 1][self.x // 3] != '0':
                self.running = 'Down'
            elif self.mapa[self.y // 3 - 1][self.x // 3] != '0':
                self.running = 'Up'

class FantasmaNaranja(Fantasma):
    def __init__(self, parent=None):
        super(FantasmaNaranja, self).__init__(parent)
        self.running = random.choice(('Left', 'Right'))

    def run(self):
        self.Base()
        while self.pacman.estado:
            posibilidades = []
            for i in self.dic:
                if eval(self.dic[i]) != '0':
                    posibilidades.append('1')
                else:
                    posibilidades.append('0')
            self.mover()
            self.Atrapar()
            self.trigger.emit((self.x - 15, self.y - 15, self))
            time.sleep(0.0072)
            r = []
            for i in self.dic:
                if eval(self.dic[i]) != '0':
                    r.append('1')
                else:
                    r.append('0')
            if not self.muerto:
                if self.estado:
                    if posibilidades != r:
                        self.Nosedevuelve()
                else:
                    self.EscaparInteligente()
            else:
                self.HuirABase()