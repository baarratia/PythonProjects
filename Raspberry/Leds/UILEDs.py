# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui
import time
import RPi.GPIO as GPIO

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

class Ui_LEDs(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.Rojo = False
        self.Amarillo = False
        self.Verde = False

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(525, 161)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.rojo = QtGui.QPushButton(Form)
        self.rojo.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.rojo)
        self.amarillo = QtGui.QPushButton(Form)
        self.amarillo.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout.addWidget(self.amarillo)
        self.verde = QtGui.QPushButton(Form)
        self.verde.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.verde)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.semaforo = QtGui.QPushButton(Form)
        self.semaforo.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_3.addWidget(self.semaforo)
        self.aleatorio = QtGui.QPushButton(Form)
        self.aleatorio.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_3.addWidget(self.aleatorio)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.rojo.pressed.connect(self.LED_Rojo)
        self.amarillo.pressed.connect(self.LED_Amarillo)
        self.verde.pressed.connect(self.LED_Verde)
        self.semaforo.pressed.connect(self.Semaforo)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.rojo.setText(_translate("Form", "Rojo", None))
        self.amarillo.setText(_translate("Form", "Amarillo", None))
        self.verde.setText(_translate("Form", "Verde", None))
        self.semaforo.setText(_translate("Form", "Semaforo", None))
        self.aleatorio.setText(_translate("Form", "Aleatorio", None))

    def LED_Rojo(self):
        if self.Rojo is False:
            self.Rojo = True
            GPIO.output(7, True)
        else:
            self.Rojo = False
            GPIO.output(7, False)

    def LED_Amarillo(self):
        if self.Amarillo is False:
            self.Amarillo = True
            GPIO.output(11, True)
        else:
            self.Amarillo = False
            GPIO.output(11, False)

    def LED_Verde(self):
        if self.Verde is False:
            self.Verde = True
            GPIO.output(13, True)
        else:
            self.Verde = False
            GPIO.output(13, False)

    def Semaforo(self):
        GPIO.output(7, False)
        GPIO.output(11, False)
        GPIO.output(13, False)
        while True:
            input_state = GPIO.input(15)
            if input_state == False:
                #ROJO
                GPIO.output(7, True)
                time.sleep(1)
                GPIO.output(7, False)
                #VERDE
                GPIO.output(13, True)
                time.sleep(1)
                GPIO.output(13, False)
                #AMARILLO
                GPIO.output(11, True)
                time.sleep(1)
                GPIO.output(11, False)


if __name__ == '__main__':
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    app = QtGui.QApplication(sys.argv)
    UI = Ui_LEDs()
    UI.show()
    sys.exit(app.exec_())