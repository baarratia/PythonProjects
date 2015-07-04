# -*- coding: utf-8 -*-
__author__ = 'Benja'
import os
import sys
from Personajes import *
from PauseMenu import *
from SaveAs import *
from Serializar import *
from Reloj import *
import subprocess

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Pocmon(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.pausa = False

    def setupUi(self, Pocmon):
        self.Pausa = PauseMenu()
        self.SaveAs = SaveAs()
        self.Pausa.conectar(self)
        Pocmon.setObjectName(_fromUtf8("Pocmon"))
        Pocmon.resize(680, 770)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Pocmon)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkRed)
        self.setPalette(p)
        self.retranslateUi(Pocmon)
        QtCore.QMetaObject.connectSlotsByName(Pocmon)
        self.setgraphics()
        self.barra = QtGui.QLabel(self)
        self.font = QtGui.QFont()
        self.font.setFamily(_fromUtf8("Fixedsys"))
        self.font.setPointSize(14)
        self.font.setBold(True)
        self.font.setWeight(75)
        self.barra.setFont(self.font)
        self.barra.resize(680, 30)
        self.record = str(EncontrarRecord())
        self.barra.setText('  Puntaje: {0:4s} Record: {1:4s} Vidas:{2:2s}  Tiempo Restante: {3:4s}'.format('0', self.record, '3',
                                                                                             '04:00'))
        self.barra.setStyleSheet('QLabel {background-color: #F6F285; color: #3366FF;}')
        self.start_threads()
        self.cont = 0
        self.c = 0
        time.process_time()

    def retranslateUi(self, Pocmon):
        Pocmon.setWindowTitle(_translate("Pocmon", "Poc-Mon", None))

    def setgraphics(self):
        with open(os.getcwd() + '\Laberintos\maze1.txt', 'r') as archivo:
            self.map = archivo.readlines()
        self.mapa = []
        c = 0
        for i in range(len(self.map)):
            lis = []
            for j in range(len(self.map[0])):
                if self.map[i][j] != '0':
                    if j == len(self.map[0]) - 2 or j == 0:
                        if self.map[i][j] != '0':
                            lis.append('8')
                    else:
                        if self.map[i][j] == '5':
                            y = i
                            x = j
                            lis.append('5')
                        elif self.map[i][j] == '4':
                            y1 = i #Posiciones claves para que los fantasmas reingresen a la base
                            x1 = j
                            self.puerta = (x1,y1)
                            lis.append('1')
                        elif self.map[i][j] == '3':
                            y2 = i
                            x2 = j
                            lis.append('3')
                        elif self.map[i][j] == '6':
                            y3 = i
                            x3 = j
                            lis.append('6')
                        elif self.map[i][j] == '9':
                            y4 = i
                            x4 = j
                            lis.append('9')
                        else:
                            if c % 5 == 0:
                                r = random.random()
                                if r < 0.03:
                                    lis.append('7')
                                else:
                                    lis.append('2')
                            else:
                                lis.append('1')

                else:
                    lis.append('0')
                c += 1
            self.mapa.append(lis)
        self.picman = QtGui.QLabel(self)
        self.f1 = QtGui.QLabel(self)
        self.f2 = QtGui.QLabel(self)
        self.f3 = QtGui.QLabel(self)
        self.f4 = QtGui.QLabel(self)
        self.myPixmap = QtGui.QPixmap(os.getcwd() + "/Imágenes/pocmon.png")
        self.myPixmap2 = QtGui.QPixmap(os.getcwd() + "/Imágenes/pocmon2.png")
        self.myPixmapizq = QtGui.QPixmap(os.getcwd() + "/Imágenes/pocmonizq.png")
        self.myPixmap2izq = QtGui.QPixmap(os.getcwd() + "/Imágenes/pocmon2izq.png")
        self.pixf1 = QtGui.QPixmap(os.getcwd() + "/Imágenes/mrpatiwi.png")
        self.pixf2 = QtGui.QPixmap(os.getcwd() + "/Imágenes/jaimiwi.png")
        self.pixf3 = QtGui.QPixmap(os.getcwd() + "/Imágenes/marquiwi.png")
        self.pixf4 = QtGui.QPixmap(os.getcwd() + "/Imágenes/belenciwi.png")
        self.Blue = QtGui.QPixmap(os.getcwd() + "/Imágenes/Blue.png")
        self.Muerto = QtGui.QPixmap(os.getcwd() + "/Imágenes/Muerto.png")
        self.myScaledPixmap = self.myPixmap.scaled(self.picman.size(), QtCore.Qt.KeepAspectRatio)
        self.picman.setPixmap(self.myScaledPixmap)
        self.myScaledf1 = self.pixf1.scaled(self.f1.size(), QtCore.Qt.KeepAspectRatio)
        self.myScaledf2 = self.pixf2.scaled(self.f2.size(), QtCore.Qt.KeepAspectRatio)
        self.myScaledf3 = self.pixf3.scaled(self.f3.size(), QtCore.Qt.KeepAspectRatio)
        self.myScaledf4 = self.pixf4.scaled(self.f4.size(), QtCore.Qt.KeepAspectRatio)
        self.myScaledAzul = self.Blue.scaled(self.f1.size(), QtCore.Qt.KeepAspectRatio)
        self.myScaledMuerto = self.Muerto.scaled(self.f1.size(), QtCore.Qt.KeepAspectRatio)
        self.f1.setPixmap(self.myScaledf1)
        self.f2.setPixmap(self.myScaledf2)
        self.f3.setPixmap(self.myScaledf3)
        self.f4.setPixmap(self.myScaledf4)
        self.picman.move(x * 3, y * 3)
        self.f1.move(x1 * 3, y1 * 3)
        self.f2.move(x2 * 3, y2 * 3)
        self.f3.move(x3 * 3, y3 * 3)
        self.f4.move(x4 * 3, y4 * 3)

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawlines(qp)
        qp.end()

    def drawlines(self, qp):
        pen = QtGui.QPen(QtCore.Qt.black, 35, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        for i in range(len(self.mapa) - 1):
            for j in range(len(self.mapa[0]) - 1):
                if self.mapa[i][j] not in ('0', '4', '3', '6', '9'):
                    qp.drawPoint(j * 3, i * 3)
        pen = QtGui.QPen(QtCore.Qt.yellow, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        for i in range(len(self.mapa) - 1):
            for j in range(len(self.mapa[0]) - 1):
                if self.mapa[i][j] not in ('0', '4', '3', '6', '9'):
                    if self.mapa[i][j] == '7':
                        pen = QtGui.QPen(QtCore.Qt.red, 5, QtCore.Qt.SolidLine)
                        qp.setPen(pen)
                        qp.drawPoint(j * 3, i * 3)
                        pen = QtGui.QPen(QtCore.Qt.yellow, 2, QtCore.Qt.SolidLine)
                        qp.setPen(pen)
                    elif self.mapa[i][j] == '2':
                        qp.drawPoint(j * 3, i * 3)

    def start_threads(self):
        self.pocmon = Pacman(self)
        self.pocmon.trigger.connect(self.correr)
        self.pocmon.setup(self.picman, self.mapa)
        self.pocmon.start()
        self.MrPatiwi = FantasmaRojo(self)
        self.MrPatiwi.setup(self.f1, self.mapa, self.pocmon, self.myScaledf1, self.puerta)
        self.Marquiwi = FantasmaNaranja(self)
        self.Marquiwi.setup(self.f3, self.mapa, self.pocmon, self.myScaledf3, self.puerta)
        self.Belenciwi = FantasmaNaranja(self)
        self.Belenciwi.setup(self.f4, self.mapa, self.pocmon, self.myScaledf4, self.puerta)
        self.Jaimiwi = FantasmaNaranja(self)
        self.Jaimiwi.setup(self.f2, self.mapa, self.pocmon, self.myScaledf2, self.puerta)
        for f in Fantasma.fantasmas:
            f.trigger.connect(self.correrFantasmas)
            f.trigg.connect(self.Azul)
            f.menosvida.connect(self.PacmanAtrapado)
            f.start()
        self.Reloj = Reloj()
        self.Reloj.trigger.connect(self.actualizarBarra) #ver si es realmente necesario
        self.Reloj.start()

    def PacmanAtrapado(self):
        self.Reloj.pausa()
        self.pocmon.vidas -= 1
        if self.pocmon.vidas == 0:
            self.GameOver()
        else:
            self.pocmon.estado = True
            for i in Fantasma.fantasmas:
               i.reboot()
            for i in Personaje.personajes:
                i.terminate()
                i.reiniciar_posicion()
            time.sleep(2)
            for i in Personaje.personajes:
                i.start()
            self.Reloj.pausa()

    def GameOver(self, mensaje=None):
        for i in Personaje.personajes:
                i.terminate()
        self.SaveAs.setPuntaje(self.pocmon.puntaje, self.Reloj.reloj, mensaje)
        self.SaveAs.show()

    def keyPressEvent(self, event):
        key = event.key()
        if key != QtCore.Qt.Key_A:
            self.pocmon.direction(key)
        else:
            self.Pausar()

    def Pausar(self):
        if not self.pausa:
            for i in Personaje.personajes:
                i.pausar()
                self.pausa = True
            self.Reloj.pausa()
            self.hide()
            self.Pausa.show()
        else:
            for i in Personaje.personajes:
                i.pausar()
            self.pausa = False
            self.Reloj.pausa()
            self.Pausa.hide()
            self.show()

    def correr(self, pos):
        self.picman.move(pos[0], pos[1])
        if self.pocmon.running == 'Left':
            if self.c % 2 == 0:
                self.picman.setPixmap(self.myPixmapizq.scaled(self.picman.size(), QtCore.Qt.KeepAspectRatio))
            else:
                self.myScaledPixmap2 = self.myPixmap2izq.scaled(self.picman.size(), QtCore.Qt.KeepAspectRatio)
                self.picman.setPixmap(self.myScaledPixmap2)
        elif self.pocmon.running == 'Up' or self.pocmon.running == 'Down':
            if self.pocmon.running == 'Up':
                angle = -90
            else:
                angle = 90
            if self.c % 2 == 0:
                rotated_pixmap = self.myPixmap.transformed(QtGui.QMatrix().rotate(angle),
                                                           QtCore.Qt.SmoothTransformation)
                self.myScaledPixmap = rotated_pixmap.scaled(self.picman.size(), QtCore.Qt.KeepAspectRatio)
                self.picman.setPixmap(self.myScaledPixmap)
            else:
                rotated_pixmap2 = self.myPixmap2.transformed(QtGui.QMatrix().rotate(angle),
                                                             QtCore.Qt.SmoothTransformation)
                self.myScaledPixmap2 = rotated_pixmap2.scaled(self.picman.size(), QtCore.Qt.KeepAspectRatio)
                self.picman.setPixmap(self.myScaledPixmap2)
        else:
            if self.c % 2 == 0:
                self.myScaledPixmap = self.myPixmap.scaled(self.picman.size(), QtCore.Qt.KeepAspectRatio)
                self.picman.setPixmap(self.myScaledPixmap)
            else:
                self.myScaledPixmap2 = self.myPixmap2.scaled(self.picman.size(), QtCore.Qt.KeepAspectRatio)
                self.picman.setPixmap(self.myScaledPixmap2)
        self.c += 1

    def correrFantasmas(self, pos):
        im = pos[2].pic
        im.move(pos[0], pos[1])

    def ComprobarPartida(self):
        if Personaje.Monedas == 525:
            self.Reloj.pausa()
            self.GameOver('Ganaste')


    def Azul(self, fantasma):
        if not fantasma.muerto:
            if not fantasma.estado:
                fantasma.pic.setPixmap(self.myScaledAzul)
            else:
                fantasma.pic.setPixmap(fantasma.pix)
        else:
            fantasma.pic.setPixmap(self.myScaledMuerto)

    def actualizarBarra(self):
        self.ComprobarPartida()
        Puntaje = str(self.pocmon.puntaje)
        vidas = str(self.pocmon.vidas)
        self.barra.setText(
            '  Puntaje: {0:4s} Record: {1:4s} Vidas:{2:2s}  Tiempo Restante: {3:4s}'.format(Puntaje, self.record, vidas,
                                                                                             self.Reloj.reloj))

    def restart(self):
        self.hide()
        self.close()
        subprocess.call("python" + " UI.py", shell=True)

    def __getstate__(self):
        nueva = self.__dict__.copy()
        #nueva.__delitem__('PauseMenu')
        return nueva

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Pocmon()
    y = pickle.dumps(ex)
    ex.show()
    #x = pickle.loads(y)
    sys.exit(app.exec_())
