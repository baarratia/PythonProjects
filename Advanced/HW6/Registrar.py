# -*- coding: utf-8 -*-
from Ichat import *
from PyQt4 import QtCore, QtGui
from Manejo_Informacion import *
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

class Registro(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(286, 247)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtGui.QLineEdit(Dialog)
        self.lineEdit_3.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.verticalLayout.addWidget(self.lineEdit_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.Registrarme = QtGui.QDialogButtonBox(Dialog)
        self.Registrarme.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.Registrarme.setObjectName(_fromUtf8("Registrarme"))
        self.verticalLayout.addWidget(self.Registrarme)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "Nombre de usuario", None))
        self.label_2.setText(_translate("Dialog", "Contraseña", None))
        self.label_3.setText(_translate("Dialog", "Confirmar Contraseña", None))
        self.Registrarme.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.Confirmar)

    def Setup(self, Lobby):
        self.Lobby = Lobby

    def Confirmar(self):
        self.usuario = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        self.confirmpass = self.lineEdit_3.text()
        if self.password == self.confirmpass:
            if self.registrar():
                self.close()

    def Reintentar(self):
        self.usuario = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        self.confirmpass = self.lineEdit_3.text()
        if self.password == self.confirmpass:
            if self.registrar(self.User):
                pass

    def registrar(self, User=None):
        if User is None:
            self.User = Cliente(self.usuario, self.password)
            self.User.EnlazarUI(self.Lobby)
        probar, probar2, r = self.User.probarconexion(True)
        while not probar:
            probar, probar2, r= self.User.probarconexion()
            time.sleep(1)
        if probar2 is False:
            return False
        print('Conectado!')
        data = self.User.s_cliente.recv(1024)
        usuarios_conectados = pickle.loads(data)
        self.Lobby.Setup_Datos(self.User)
        self.Lobby.actualizar_conectados(usuarios_conectados)
        self.User.Comenzar()
        self.Lobby.show()
        return True