from Ichat import *
from Registrar import *

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

class LogIn(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(259, 238)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Ichat", "Ichat", None))
        self.label.setText(_translate("Form", "Correo UC:", None))
        self.label_2.setText(_translate("Form", "Contraseña:", None))
        self.pushButton.setText(_translate("Form", "Iniciar Sesión", None))
        self.pushButton_2.setText(_translate("Form", "Registrar nuevo usuario", None))
        self.pushButton.clicked.connect(self.Ingresar)
        self.pushButton_2.clicked.connect(self.RegistrarUsuario)

    def SetUp(self, Lobby):
        self.Lobby = Lobby

    def Ingresar(self):
        self.usuario = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        if self.ConectarUsuario():
            self.close() #ver si funciona esto
        else:
            self.pushButton.clicked.connect(self.Reintentar)

    def Reintentar(self):
        self.usuario = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        if self.ConectarUsuario(self.User):
            self.close()

    def ConectarUsuario(self, User = None):
        if User is None:
            self.User = Cliente(self.usuario, self.password)
            self.User.EnlazarUI(self.Lobby)
        else:
            self.User.usuario = self.usuario
            self.User.password = self.password
        probar, probar2, mensaje = self.User.probarconexion()
        while not probar:
            probar, probar2, mensaje = self.User.probarconexion()
            time.sleep(1)
        if probar2 is False:
            self.Mensaje(mensaje)
            return False
        print('Conectado!')
        data = self.User.s_cliente.recv(1024)
        usuarios_conectados = pickle.loads(data)
        self.Lobby.Setup_Datos(self.User)
        self.Lobby.actualizar_conectados(usuarios_conectados)
        self.User.Comenzar()
        self.Lobby.show()
        return True

    def RegistrarUsuario(self):
        self.registwindow = Registro()
        self.registwindow.Setup(self.Lobby)
        self.registwindow.show()

    def keyPressEvent(self, qKeyEvent):
        if qKeyEvent.key() == QtCore.Qt.Key_Return:
            self.Ingresar()
        else:
            super().keyPressEvent(qKeyEvent)

    def Mensaje(self, texto):
        msgBox = QtGui.QMessageBox()
        msgBox.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
        msgBox.setText(texto)
        ret = msgBox.exec_()