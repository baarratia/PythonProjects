# -*- coding: utf-8 -*-
import pickle
from PyQt4 import QtCore, QtGui
from Buscar_Imagenes import *

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


class Ui_Chat(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.User = None
        self.Receptor = None

    def setupUi(self, Chat):
        Chat.setObjectName(_fromUtf8("Chat"))
        Chat.resize(845, 577)
        self.pushButton = QtGui.QPushButton(Chat)
        self.pushButton.setGeometry(QtCore.QRect(740, 440, 93, 91))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textEdit = QtGui.QTextEdit(Chat)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(20, 440, 711, 121))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayoutWidget = QtGui.QWidget(Chat)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 811, 401))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.plainTextEdit = QtGui.QTextBrowser(self.horizontalLayoutWidget)
        self.plainTextEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.plainTextEdit.setPlainText(_fromUtf8(""))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.retranslateUi(Chat)
        QtCore.QMetaObject.connectSlotsByName(Chat)

    def retranslateUi(self, Chat):
        Chat.setWindowTitle(_translate("Chat", "Form", None))
        self.pushButton.setText(_translate("Chat", "Enviar", None))
        self.textEdit.setHtml(_translate("Chat",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>",
                                         None))
        self.pushButton.clicked.connect(self.enviar)
        self.pushButton.setShortcut('Enter')

    def enviar(self):
        mensaje = self.textEdit.toPlainText()
        if len(mensaje) > 0:
            self.textEdit.clear()
            self.insertar(mensaje)
            m = '{0} : {1}'.format(self.user.usuario, mensaje)
            self.plainTextEdit.append(_fromUtf8(m))
            data = (self.user.usuario, self.receptor, mensaje)
            self.user.enviar(data)

    def recibir(self, mensaje):
        m = '{0} : {1}'.format(self.receptor, mensaje)
        self.insertar(mensaje)
        self.plainTextEdit.append(_fromUtf8(m))

    def insertar(self, mensaje):
        posible_img, n= Comprobar_Mensaje(mensaje) #Configuar esto para que se puedan enviar distintas imagenes
        if posible_img is not False:
            tick_icon = QtGui.QTextDocumentFragment.fromHtml(r"<img src='Data/{}.png'>".format(n))
            self.plainTextEdit.textCursor().insertFragment(tick_icon)

    def SetUp(self, nombre, user):
        self.receptor = nombre
        self.user = user
        self.setWindowTitle(_translate("Chat", "Conversacion con {}".format(nombre), None))

    def keyPressEvent(self, qKeyEvent):
        if qKeyEvent.key() == QtCore.Qt.Key_Return:
            self.enviar()
        else:
            super().keyPressEvent(qKeyEvent)


