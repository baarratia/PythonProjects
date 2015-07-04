# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ranking.ui'
#
# Created: Thu Jun 11 03:49:21 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ranking(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(336, 336)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtCore.Qt.darkRed)
        self.setPalette(p)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.treeWidget = QtGui.QTreeWidget(Form)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        for i in range(10):
            item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        self.verticalLayout.addWidget(self.treeWidget)
        self.buttonBox = QtGui.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.buttonBox.clicked.connect(self.setRankingUser)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "TOP 10", None))
        self.label.setText(_translate("Form", "TOP 10", None))
        self.treeWidget.headerItem().setText(0, _translate("Form", "Name", None))
        self.treeWidget.headerItem().setText(1, _translate("Form", "Time", None))
        self.treeWidget.headerItem().setText(2, _translate("Form", "Score", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.setSortingEnabled(__sortingEnabled)

    def setRanking(self, lista, user):
        self.lista = sorted(lista, key=lambda x: x[1])
        self.user = user
        self.lista.reverse()
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(True)
        if len(self.lista) < 10:
            num = len(lista)
        else:
            num = 10
        for i in range(num):
            dat = self.lista[i]
            self.treeWidget.topLevelItem(i).setText(0, _translate("Form", dat[0], None))
            self.treeWidget.topLevelItem(i).setText(1, _translate("Form", dat[2], None))
            self.treeWidget.topLevelItem(i).setText(2, _translate("Form", dat[1], None))
        self.treeWidget.setSortingEnabled(__sortingEnabled)

    def setRankingUser(self):
        self.label.setText(_translate("Form", "TOP 10 {}".format(self.user), None))
        self.treeWidget.clear()
        for i in range(10):
            item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        top10 = []
        for i in self.lista:
            if i[0] == self.user:
                top10.append(i)
        lista = top10
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(True)
        if len(lista) < 10:
            num = len(lista)
        else:
            num = 10
        for i in range(num):
            dat = lista[i]
            self.treeWidget.topLevelItem(i).setText(0, _translate("Form", dat[0], None))
            self.treeWidget.topLevelItem(i).setText(1, _translate("Form", dat[2], None))
            self.treeWidget.topLevelItem(i).setText(2, _translate("Form", dat[1], None))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.buttonBox.clicked.connect(self.salir)

    def salir(self):
        self.hide()

