# -*- coding: utf-8 -*-
from Serializar import *
from Ranking import *
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

class SaveAs(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        self.Rank = Ranking()
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(70, 20)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkRed)
        self.setPalette(p)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS UI Gothic"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Layout = QtGui.QVBoxLayout(Form)
        self.Layout.setObjectName(_fromUtf8("verticalLayout"))
        self.texto = QtGui.QLabel(Form)
        self.texto.setFont(font)
        self.texto.setText('GAME OVER')
        self.Layout.addWidget(self.texto)
        self.puntos = QtGui.QLabel(Form)
        self.puntos.setFont(font)
        self.puntos.setText('SCORE: {}'.format('0'))
        self.Layout.addWidget(self.puntos)
        self.User = QtGui.QLineEdit(Form)
        self.User.setObjectName(_fromUtf8("plainTextEdit"))
        self.Layout.addWidget(self.User)
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.Layout.addWidget(self.buttonBox)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.buttonBox.clicked.connect(self.IngresarNombre)
        shortcut = QtGui.QShortcut(QtGui.QKeySequence("Enter"), self, self.IngresarNombre)
        shortcut.setContext(QtCore.Qt.WidgetShortcut)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Game Over", "Game Over", None))

    def setPuntaje(self, puntaje, time, mensaje=None):
        if mensaje is not None:
            self.texto.setText(mensaje)
        self.puntaje = str(puntaje)
        self.time = time
        self.puntos.setText('SCORE: {0}\n Time: {1}'.format(self.puntaje, self.time))

    def IngresarNombre(self):
        usuario = self.User.text()
        if len(usuario) > 0:
            Data = SaveData(usuario, self.puntaje, self.time)
            self.Rank.setRanking(Data, usuario)
            self.Rank.show()
            self.hide()




