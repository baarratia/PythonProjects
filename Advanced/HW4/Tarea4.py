__author__ = 'Benja'
from clases_botones import *
import sys

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


class Dragculadora(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Dragculadora"))
        Form.resize(1200, 900)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.font = QtGui.QFont()
        self.font.setFamily(_fromUtf8("Fixedsys"))
        self.font.setPointSize(36)
        self.font.setBold(True)
        self.font.setWeight(75)
        self.textEdit.setFont(self.font)
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setFrameShape(QtGui.QFrame.WinPanel)
        self.textEdit.setFrameShadow(QtGui.QFrame.Sunken)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.font.setFamily(_fromUtf8("MS Shell Dlg 2"))
        self.font.setPointSize(14)
        self.setFont(self.font)
        self.NUM = QtGui.QPushButton(Form)
        self.NUM.setEnabled(True)
        self.NUM.setObjectName(_fromUtf8("NUM"))
        self.horizontalLayout_8.addWidget(self.NUM)
        self.euler = QtGui.QPushButton(Form)
        self.euler.setObjectName(_fromUtf8("euler"))
        self.horizontalLayout_8.addWidget(self.euler)
        self.pi = QtGui.QPushButton(Form)
        self.pi.setObjectName(_fromUtf8("pi"))
        self.horizontalLayout_8.addWidget(self.pi)
        self.absoluto = QtGui.QPushButton(Form)
        self.absoluto.setObjectName(_fromUtf8("absoluto"))
        self.horizontalLayout_8.addWidget(self.absoluto)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.suma = QtGui.QPushButton(Form)
        self.suma.setObjectName(_fromUtf8("suma"))
        self.horizontalLayout_3.addWidget(self.suma)
        self.division = QtGui.QPushButton(Form)
        self.division.setObjectName(_fromUtf8("division"))
        self.horizontalLayout_3.addWidget(self.division)
        self.seno = QtGui.QPushButton(Form)
        self.seno.setObjectName(_fromUtf8("seno"))
        self.horizontalLayout_3.addWidget(self.seno)
        self.maximo = QtGui.QPushButton(Form)
        self.maximo.setObjectName(_fromUtf8("maximo"))
        self.horizontalLayout_3.addWidget(self.maximo)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.resta = QtGui.QPushButton(Form)
        self.resta.setObjectName(_fromUtf8("resta"))
        self.horizontalLayout_10.addWidget(self.resta)
        self.potencia = QtGui.QPushButton(Form)
        self.potencia.setObjectName(_fromUtf8("potencia"))
        self.horizontalLayout_10.addWidget(self.potencia)
        self.coseno = QtGui.QPushButton(Form)
        self.coseno.setObjectName(_fromUtf8("coseno"))
        self.horizontalLayout_10.addWidget(self.coseno)
        self.minimo = QtGui.QPushButton(Form)
        self.minimo.setObjectName(_fromUtf8("minimo"))
        self.horizontalLayout_10.addWidget(self.minimo)
        self.gridLayout.addLayout(self.horizontalLayout_10, 1, 0, 1, 1)
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.gridLayout.addLayout(self.verticalLayout_11, 8, 0, 1, 1)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.multiplicacion = QtGui.QPushButton(Form)
        self.multiplicacion.setObjectName(_fromUtf8("multiplicacion"))
        self.horizontalLayout_12.addWidget(self.multiplicacion)
        self.logaritmo = QtGui.QPushButton(Form)
        self.logaritmo.setObjectName(_fromUtf8("logaritmo"))
        self.horizontalLayout_12.addWidget(self.logaritmo)
        self.tangente = QtGui.QPushButton(Form)
        self.tangente.setObjectName(_fromUtf8("tangente"))
        self.horizontalLayout_12.addWidget(self.tangente)
        self.igual = QtGui.QPushButton(Form)
        self.igual.setCheckable(True)
        self.igual.setObjectName(_fromUtf8("igual"))
        self.horizontalLayout_12.addWidget(self.igual)
        self.gridLayout.addLayout(self.horizontalLayout_12, 2, 0, 1, 1)
        self.mdiArea = QtGui.QMdiArea(Form)
        self.mdiArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.Dense7Pattern)
        self.mdiArea.setBackground(brush)
        self.mdiArea.setViewMode(QtGui.QMdiArea.SubWindowView)
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.gridLayout.addWidget(self.mdiArea, 5, 0, 1, 1)
        self.borrar = QtGui.QPushButton(Form)
        # self.borrar.setFont(font)
        self.borrar.setObjectName(_fromUtf8("borrar"))
        self.borrar.setCheckable(True)
        self.gridLayout.addWidget(self.borrar, 3, 0, 1, 1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", _fromUtf8("Dragculadora"), None))
        self.textEdit.setHtml(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Fixedsys\'; font-size:36pt; font-weight:600; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>",
                                         None))
        self.NUM.setText(_translate("Form", "Generar NUM", None))
        self.euler.setText(_translate("Form", "e", None))
        self.pi.setText(_translate("Form", "pi", None))
        self.absoluto.setText(_translate("Form", "abs", None))
        self.suma.setText(_translate("Form", "+", None))
        self.division.setText(_translate("Form", "/", None))
        self.seno.setText(_translate("Form", "sin", None))
        self.maximo.setText(_translate("Form", "max", None))
        self.resta.setText(_translate("Form", "-", None))
        self.potencia.setText(_translate("Form", "^", None))
        self.coseno.setText(_translate("Form", "cos", None))
        self.minimo.setText(_translate("Form", "min", None))
        self.multiplicacion.setText(_translate("Form", "x", None))
        self.logaritmo.setText(_translate("Form", "log", None))
        self.tangente.setText(_translate("Form", "tan", None))
        self.igual.setText(_translate("Form", "=", None))
        self.borrar.setText(_translate("Form", "Borrar", None))
        self.NUM.clicked.connect(self.Generar_NUM)
        self.euler.clicked.connect(self.Add)
        self.pi.clicked.connect(self.Add)
        self.absoluto.clicked.connect(self.Add)
        self.suma.clicked.connect(self.Add)
        self.division.clicked.connect(self.Add)
        self.seno.clicked.connect(self.Add)
        self.maximo.clicked.connect(self.Add)
        self.resta.clicked.connect(self.Add)
        self.potencia.clicked.connect(self.Add)
        self.coseno.clicked.connect(self.Add)
        self.minimo.clicked.connect(self.Add)
        self.multiplicacion.clicked.connect(self.Add)
        self.logaritmo.clicked.connect(self.Add)
        self.tangente.clicked.connect(self.Add)
        self.igual.clicked.connect(self.activar_Output)
        self.borrar.clicked.connect(self.activar_borrar)
        self.NUM.setStyleSheet('QPushButton {background-color: #F6F285; color: #3366FF;}')
        self.NUM.setFont(self.font)
        self.igual.setStyleSheet('QPushButton {background-color: gray; color: white;}')
        self.igual.setFont(self.font)
        self.borrar.setStyleSheet('QPushButton {background-color: #FF3333; color: white;}')
        self.borrar.setFont(self.font)
        self.setStyleSheet('QPushButton {background-color: #3366FF; color: white;}')
        self.draggers = []
        self.estado = None
        self.borrado = False
        self.Op = False
        self.data = None
        self.uniones = []

    def activar_borrar(self):
        self.igual.setChecked(False)
        self.Op = False
        if self.borrado:
            self.borrado = False
            self.borrar.setChecked(False)
        else:
            self.borrado = True
            self.borrar.setChecked(True)

    def activar_Output(self):
        self.borrar.setChecked(False)
        self.borrado = False
        if self.Op:
            self.Op = False
            self.igual.setChecked(False)
        else:
            self.Op = True
            self.igual.setChecked(True)

    def bifurcacion(self):
        if self.borrado:
            self.Del()
        elif self.Op:
            self.Output()
        else:
            self.Button()

    def Generar_NUM(self):
        num = self.textEdit.toPlainText()
        c = 0
        d = 0
        p = 0
        for i in num:
            if not i.isdigit():
                if i == '.':
                    c += 1
                elif i == '-':
                    if p == 0:
                        d += 1
                    else:
                        return self.textEdit.setText('Error')
                else:
                    return self.textEdit.setText('Error')
            p += 1
        if c <= 1 and d <= 1:
            b = Numero(self.textEdit.toPlainText(), self)
            b.tipo = ['Numero']
            b.tipodef = 'Completa'
            b.conectado = False
            b.accion = True
            b.clicked.connect(self.bifurcacion)
            b.move(30, 400)
            b.setStyleSheet('QPushButton {background-color: #3366FF; color: white;}')
            b.setFont(self.font)
            b.resize(len(b.text()) * 15 + 100, 60)
            b.show()
            self.draggers.append(b)
        else:
            return self.textEdit.setText('Error')

    def Add(self):
        sender = self.sender()
        lista_op = ['+', '-', 'x', '/', '^']
        lista_trig = ['sin', 'cos', 'tan']
        lista_sop = ['log', 'abs']
        if sender.text() in lista_op:
            b = Operacion_Simple(sender.text(), self)
            b.setStyleSheet('QPushButton {background-color: gray; color: white;}')
        elif sender.text() in lista_sop:
            b = Operacion_Compleja(sender.text(), self)
            b.setStyleSheet('QPushButton {background-color: #6E00FF; color: white;}')
        elif sender.text() in lista_trig:
            b = Trigonometrica(sender.text(), self)
            b.setStyleSheet('QPushButton {background-color: #6E00FF; color: white;}')
        elif sender.text() == 'e' or sender.text() == 'pi':
            b = Numero(sender.text(), self)
            b.setStyleSheet('QPushButton {background-color: #3366FF; color: white;}')
        else:
            b = Operacion_MM(sender.text(), self)
            b.setStyleSheet('QPushButton {background-color: #00A1FF; color: white;}')
        b.setFont(self.font)
        b.conectado = False
        b.accion = True
        self.draggers.append(b)
        b.clicked.connect(self.bifurcacion)
        b.resize(len(b.text()) * 5 + 100, 60)
        b.move(20, 400)
        b.show()

    def Del(self):
        sender = self.sender()
        if sender.salida == None:
            sender.deleteLater()
            self.draggers.remove(sender)
            clon = self.uniones.copy()
            for i in clon:
                if sender in i:
                    i[0].desconectar(i[1])
                    i[1].desconectar(i[0])
                    self.uniones.remove(i)
            self.estado = None
        else:
            self.Mensaje('No se puede eliminar el elemento seleccionado\npues su salida está unida a otra entidad')

    def Output(self):
        sender = self.sender()
        if sender.Output is not None:
            self.textEdit.setText(str(sender.Output))

    def Button(self):
        sender = self.sender()
        if self.data != sender:
            if not self.estado:
                self.estado = True
                self.data = sender
            else:
                self.unir(self.data, sender)
                self.estado = None

    def unir(self, a, b):
        if a.conectar_salida(b):
            if b.conectar(a):
                self.uniones.append((a, b))
                if b.Output is not None:
                    b.setStyleSheet('QPushButton {background-color: #004C99; color: white;}')
            else:
                a.desconectar(b)
                print('No conectado')
        else:
            print('No conectado')

    def paintEvent(self, event):
        paper = QtGui.QPainter(self)
        pen = QtGui.QPen(QtCore.Qt.black, 5, QtCore.Qt.SolidLine)
        paper.setPen(pen)
        for i in self.uniones:
            a = i[0].pos()
            b = i[1].pos()
            ax = a.x() + len(i[0].text()) * 5 + 50
            ay = a.y() + 30
            bx = b.x() + len(i[1].text()) * 5 + 50
            by = b.y() + 30
            paper.drawLine(ax, ay, bx, by)
            self.update()

    def Mensaje(self, texto):
        msgBox = QtGui.QMessageBox()
        msgBox.addButton(QtGui.QPushButton('OK'), QtGui.QMessageBox.YesRole)
        msgBox.setText(texto)
        ret = msgBox.exec_()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ex = Dragculadora()
    ex.show()
    sys.exit(app.exec_())