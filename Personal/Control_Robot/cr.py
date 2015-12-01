# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui

from Comunicador import Comunicador_Robot

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


class Control(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.show()

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Control Robot"))
        Form.resize(668, 431)
        self.dial = QtGui.QDial(Form)
        self.dial.setGeometry(QtCore.QRect(20, 40, 351, 231))
        self.dial.setObjectName(_fromUtf8("dial"))
        self.verticalSlider = QtGui.QSlider(Form)
        self.verticalSlider.setGeometry(QtCore.QRect(480, 80, 121, 221))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
        self.conexion = QtGui.QPushButton(Form)
        self.conexion.setGeometry(QtCore.QRect(5, 5, 100, 50))
        self.conexion.setText('Conectar')
        self.conexion.setStyleSheet('QPushButton {background-color: #E60909; color: #FFFFFF;}')
        self.cambio_direccion = QtGui.QPushButton(Form)
        self.cambio_direccion.setGeometry(QtCore.QRect(165, 260, 70, 50))
        self.cambio_direccion.setObjectName(_fromUtf8("cambio_direccion"))
        self.cambio_direccion.setText('Retroceder')
        self.cambio_direccion.setStyleSheet('QPushButton {background-color: #0965E6; color: #FFFFFF;}')
        self.lcdNumber = QtGui.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(480, 320, 101, 51))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.lcdNumber_2 = QtGui.QLCDNumber(Form)
        self.lcdNumber_2.setGeometry(QtCore.QRect(80, 320, 101, 51))
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.lcdNumber_3 = QtGui.QLCDNumber(Form)
        self.lcdNumber_3.setGeometry(QtCore.QRect(220, 320, 101, 51))
        self.lcdNumber_3.setObjectName(_fromUtf8("lcdNumber_3"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 370, 91, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(220, 370, 91, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(390, 30, 21, 391))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        ''''p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkCyan)
        self.setPalette(p)'''
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Control Robot", "Control Robot", None))
        self.label.setText(_translate("Form", "Motor Izquierdo", None))
        self.label_2.setText(_translate("Form", "Motor Derecho", None))
        self.direccion = 'Avanzar'
        self.dial.valueChanged.connect(self.motores)
        self.verticalSlider.valueChanged.connect(self.pwm)
        self.c = 0
        self.cambio_direccion.pressed.connect(self.cambio)
        self.conexion.pressed.connect(self.Conectar)
        self.motor1 = 0
        self.motor2 = 0
        self.PWM = 0
        self.emparejado = False

    def Conectar(self):
        if self.emparejado is False:
            self.conexion.setText('Conectando...')
            self.conexion.setStyleSheet('QPushButton {background-color: #09E6E6; color: #000000;}')
            self.comunicacion = Comunicador_Robot()
            if self.comunicacion.CONNECTED:
                self.emparejado = True
                self.conexion.setText('Conectado!')
                self.conexion.setStyleSheet('QPushButton {background-color: #78E609; color: #000000;}')

    def motores(self, arg):
        if 47 <= arg <= 53:
            self.motor1 = 100
            self.motor2 = 100
            self.lcdNumber_2.display(self.motor1)
            self.lcdNumber_3.display(self.motor2)
        if 21 < arg < 47:
            self.motor1 = int(92 * (arg - 22) / 22)
            self.motor2 = 100
            self.lcdNumber_2.display(self.motor1)
            self.lcdNumber_3.display(self.motor2)
        if 53 < arg < 79:
            self.motor1 = 100
            self.motor2 = int(92 * (78 - arg) / 22)
            self.lcdNumber_2.display(100)
            self.lcdNumber_3.display(self.motor2)
        if 0 <= arg <= 21:
            if arg == 0:
                self.lcdNumber_2.display(-100)
            else:
                self.lcdNumber_2.display(int(94 * (arg - 22) / 21))
            self.lcdNumber_3.display(100)
            print('in1:L, in2:H, in3:H,in4:L')

        if 78 <= arg <= 99:
            self.motor1 = 100
            self.lcdNumber_2.display(self.motor1)
            if arg == 99:
                self.motor2 = -100
                self.lcdNumber_3.display(self.motor2)
            else:
                self.motor2 = int(94 * (78 - arg) / 21)
                self.lcdNumber_3.display(self.motor2)
            print('in1:H, in2:L, in3:L,in4:H')
        if self.emparejado:
            self.Send_Data()

    def pwm(self, arg):
        self.PWM = int(arg * (254 / 99))
        self.lcdNumber.display(self.PWM)
        if self.emparejado:
            self.Send_Data()

    def cambio(self):
        if self.emparejado:
            if self.c == 0:
                print('Retroceso activado')
                self.direccion = 1
                self.cambio_direccion.setText('Avanzar')
                self.cambio_direccion.setStyleSheet('QPushButton {background-color: #7809E6; color: #FFFFFF;}')

                self.verticalSlider.setValue(0)
                self.c += 1
            elif self.c == 1:
                print('Avanzar activado')
                self.direccion = 0
                self.cambio_direccion.setText('Retroceder')
                self.cambio_direccion.setStyleSheet('QPushButton {background-color: #0965E6; color: #FFFFFF;}')
                self.verticalSlider.setValue(0)
                self.c = 0
            self.Send_Data()


    def Send_Data(self):
        potenciaA = int((self.motor1 / 100) * self.PWM)
        potenciaB = int((self.motor2 / 100) * self.PWM)
        data = potenciaA, potenciaB, self.direccion
        self.comunicacion.escuchar_enviar(data)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Control()
    ex.show()
    sys.exit(app.exec_())
