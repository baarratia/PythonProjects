# -*- coding: utf-8 -*-
from ChatGrupal import *
from AgregarGrupo import *
from Ventana_Chat import *
from LogIn import *
import sys
import random

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

class Lobby(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Lobby"))
        Form.resize(588, 607)
        self.horizontalLayoutWidget = QtGui.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 322, 89))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.icono = QtGui.QLabel(self)
        self.icono.setStyleSheet('QLabel {background-color: #FF0000}')  # Luego fijar el color unico por usuario
        self.icono.resize(40, 40)
        self.horizontalLayout.addWidget(self.icono)
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB"))
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 130, 271, 80))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.line = QtGui.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(17, 110, 561, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 50, 101, 31))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 220, 569, 91))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Berlin Sans FB"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.Usuarios_Conectados = QtGui.QListWidget(Form)
        self.Usuarios_Conectados.setGeometry(QtCore.QRect(310, 290, 201, 261))
        self.Usuarios_Conectados.setObjectName(_fromUtf8("Usuarios_Conectados"))
        self.Conversaciones = QtGui.QListWidget(Form)
        self.Conversaciones.setGeometry(QtCore.QRect(50, 290, 201, 261))
        self.Conversaciones.setObjectName(_fromUtf8("Conversaciones"))
        self.line_2 = QtGui.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(10, 210, 581, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(280, 220, 20, 381))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.Log = LogIn()
        self.Log.SetUp(self)
        self.Log.show()
        self.listaconectados = []
        self.pushButton.clicked.connect(self.NuevoChatGrupal)
        self.pushButton_3.clicked.connect(self.salir)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Nombre de Usuario", None))
        self.pushButton.setText(_translate("Form", "Nuevo Grupo", None))
        self.pushButton_3.setText(_translate("Form", "Cerrar Sesión", None))
        self.label_3.setText(_translate("Form", "Conversaciones Activas:", None))
        self.label_2.setText(_translate("Form", "Usuarios Conectados:", None))

    def Setup_Datos(self, user):
        self.user = user
        self.label.setText(_translate("Form", self.user.usuario, None))
        self.user.trigger.connect(self.actualizar_conectados)
        self.user.trigger2.connect(self.actualizar_conversaciones)

    def Chat(self, item):
        item = item.text()
        if item not in self.user.chats:
            if item in self.user.grupos:
                self.user.grupos[item].show()
            else:
                VentanaChat = Ui_Chat()
                VentanaChat.SetUp(item, self.user)
                VentanaChat.show()
                self.user.chats[item] = VentanaChat
        else:
            self.user.chats[item].show()
        self.actualizar()

    def NuevoChatGrupal(self):
        self.Config = Config_Grupo()
        self.Config.info.connect(self.Crear_nuevo_grupo)
        self.Config.usuarios_conectados(self.listaconectados, self.user)
        self.Config.show()

    def Crear_nuevo_grupo(self, datos):
        usuarios, nombre = self.generar_grupo(datos)
        self.user.grupos[datos[0]].setAdmin()
        self.user.grupos[datos[0]].show()
        self.user.enviar((self.user.usuario, usuarios, nombre))

    def generar_grupo(self, datos): #Crea un grupo con los datos recolectados
        nombre = datos[0]
        usuarios = datos[1]
        grupo = Ventana_Grupo()
        grupo.setup(self.user, usuarios, nombre)
        self.user.grupos[nombre] = grupo
        usuarios.append(self.user.usuario)
        return usuarios, nombre

    def actualizar_conectados(self, lista_usuarios):
        self.listaconectados = lista_usuarios
        print('Actualizando Conectados')
        __sortingEnabled = self.Conversaciones.isSortingEnabled()
        self.Usuarios_Conectados.setSortingEnabled(True)
        self.Usuarios_Conectados.clear()
        for i in lista_usuarios:
            if i != self.user.usuario:
                item = QtGui.QListWidgetItem()
                item.setText(_translate("Form", i, None))
                self.Usuarios_Conectados.addItem(item)
                self.Usuarios_Conectados.itemClicked.connect(self.Chat)
        self.Usuarios_Conectados.setSortingEnabled(__sortingEnabled)

    def actualizar_conversaciones(self, mensaje):
        usuario = mensaje[0]
        if type(mensaje[1]) == list:
            print('Nuevo grupo!')
            self.generar_grupo((mensaje[2], mensaje[1]))
        else:
            if len(mensaje) == 3:
                mensaje = mensaje[2]
                if usuario not in self.user.chats:
                    VentanaChat = Ui_Chat()
                    VentanaChat.SetUp(usuario, self.user)
                    self.user.chats[usuario] = VentanaChat
                    VentanaChat.recibir(mensaje)
                else:
                    self.user.chats[usuario].recibir(mensaje)
            else:
                self.user.grupos[mensaje[1]].recibir(mensaje[2],mensaje[0] )
        self.actualizar()

    def actualizar(self):
        __sortingEnabled = self.Conversaciones.isSortingEnabled()
        self.Conversaciones.setSortingEnabled(True)
        self.Conversaciones.clear()
        for i in self.user.grupos:
            conv = QtGui.QListWidgetItem()
            conv.setText(_translate("Form", i, None))
            self.Conversaciones.addItem(conv)
            self.Conversaciones.itemClicked.connect(self.Chat)
        for i in self.user.chats:
            if i in self.listaconectados:
                conv = QtGui.QListWidgetItem()
                conv.setText(_translate("Form", i, None))
                self.Conversaciones.addItem(conv)
                self.Conversaciones.itemClicked.connect(self.Chat)
        self.Conversaciones.setSortingEnabled(__sortingEnabled)

    def Mensaje(self, texto, funcion):
        msgBox = QtGui.QMessageBox()
        msgBox.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.DestructiveRole)
        msgBox.setText(texto)
        ret = msgBox.exec_()
        if msgBox.clickedButton():
            funcion()

    def salir(self):
        self.Mensaje('Desea Cerrar Sesión?\n Se perderán las conversaciones actuales', self.cerrar)

    def cerrar(self):
        sys.exit(app.exec_())

app = QtGui.QApplication(sys.argv)
ex = Lobby()
sys.exit(app.exec_())
