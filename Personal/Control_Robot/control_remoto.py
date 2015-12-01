__author__ = 'Benja'
import sys
from PyQt4 import QtGui, QtCore

class RotatableView(QtGui.QGraphicsView):
    def __init__(self, item, rotation=0):
        QtGui.QGraphicsView.__init__(self)
        scene = QtGui.QGraphicsScene(self)
        self.setScene(scene)
        graphics_item = scene.addWidget(item)
        graphics_item.rotate(rotation)

        # make the QGraphicsView invisible
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setFixedHeight(item.height())
        self.setFixedWidth(item.width())
        self.setStyleSheet("border: 0px")

class DialExample(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        dial = QtGui.QDial()
        dial.setNotchesVisible(True)
        label = QtGui.QLabel('0')
        dial.valueChanged.connect(label.setNum)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(RotatableView(dial, 180))
        layout.addWidget(label)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dialexample = DialExample()
    dialexample.show()
    sys.exit(app.exec_())