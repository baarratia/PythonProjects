__author__ = 'Benja'
import time

from PyQt4 import QtCore


class Reloj(QtCore.QThread):
    trigger = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        super(Reloj, self).__init__(parent)
        self.Activo = True
        self.time = 4 * 60
        self.Editar()
        self.stop = False

    def run(self):
        while True:
            if self.Activo:
                self.time -= 1
                time.sleep(1)
                self.Editar()
                if self.time == 0:
                    self.Activo = False
                    self.stop = True
                self.trigger.emit(self)
            else:
                time.sleep(1)

    def setup(self, tiempo):
        self.time = tiempo

    def pausa(self):
        if self.Activo:
            self.Activo = False
        else:
            self.Activo = True

    def Editar(self):
        min = str(int(self.time // 60))
        sec = str(int(self.time % 60))
        self.reloj = ('{0}:{1}'.format(min.zfill(2), sec.zfill(2)))