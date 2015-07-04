__author__ = 'Benja'
from PyQt4 import QtCore, QtGui
from math import *


class DragButton(QtGui.QPushButton):
    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == QtCore.Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()

        super(DragButton, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.base = QtGui.QPushButton
        if event.buttons() == QtCore.Qt.LeftButton:
            # adjust offset from clicked point to origin of widget
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)

            self.__mouseMovePos = globalPos

        super(DragButton, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos
            if moved.manhattanLength() > 100:
                event.ignore()
                return

        super(DragButton, self).mouseReleaseEvent(event)


def evaluar(operacion):
    try:
        resultado = eval(operacion)
        return True, resultado
    except ZeroDivisionError:
        mensaje = 'Division por cero no aceptada'
    except ValueError:
        mensaje = 'Esta funcion no tiene en\nsu Dominio el número que\nse intenta asignar'
    return False, mensaje


class Bloque(DragButton):
    def __init__(self, operacion, espacio):
        super(Bloque, self).__init__(operacion, espacio)
        self.operacion = operacion
        self.espacio = espacio
        self.Output = None
        self.salida = None

    def conectar_salida(self, algo):
        if self.salida is None and self.Output is not None:
            if type(algo) != Numero:
                self.salida = algo
                return True
        return False


class Numero(Bloque):
    def __init__(self, valor, espacio):
        super(Numero, self).__init__(valor, espacio)
        if valor == 'pi':
            valor = str(pi)
        if valor == 'e':
            valor = str(e)
        self.Output = valor
        self.conectar_salida = self.conectar

    def conectar(self, algo):
        if type(algo) != Numero:
            if self.salida is None:
                self.salida = algo
                return True
            else:
                return False
        else:
            return False

    def desconectar(self, algo):
        if self.salida == algo:
            self.salida = None


class Operacion_Simple(Bloque):
    def __init__(self, operacion, espacio):
        super(Operacion_Simple, self).__init__(operacion, espacio)
        if operacion == 'x':
            self.operacion = '*'
        if operacion == '^':
            self.operacion = '**'
        self.x = None
        self.y = None

    def conectar(self, algo):
        if self.x is None:
            self.x = algo
            if self.y is not None:  # Esta parte es util en el caso de que haya una interrupcion de la cadena por
                #haber eliminado algun bloque
                if self.resultado():
                    return True
                else:
                    self.x = None
                    return False
            return True
        else:
            if self.y is None:
                self.y = algo
                if not self.resultado():
                    self.y = None
                    return False
                else:
                    return True
            else:
                return False

    def resultado(self):
        operacion = ('({0}){1}({2})'.format(self.x.Output, self.operacion, self.y.Output))
        factible, resultado = evaluar(operacion)
        if factible:
            self.Output = str(resultado)
            self.espacio.textEdit.setText(self.Output)
            return True
        else:
            self.espacio.textEdit.setText('Error')
            self.espacio.Mensaje(resultado)
            return False

    def desconectar(self, algo):
        if self.x == algo:
            self.x = None
            self.Output = None
        if self.y == algo:
            self.y = None
            self.Output = None
        if self.salida == algo:
            self.salida = None


class Operacion_Compleja(Bloque):
    def __init__(self, operacion, espacio):
        super(Operacion_Compleja, self).__init__(operacion, espacio)
        self.x = None

    def conectar(self, algo):
        if self.x is None:
            self.x = algo.Output
            if not self.resultado():
                self.x = None
                return False
            else:
                return True
        else:
            return False

    def resultado(self):
        operacion = ('{0}({1})'.format(self.operacion, self.x))
        factible, resultado = evaluar(operacion)
        if factible:
            self.Output = str(resultado)
            self.espacio.textEdit.setText(self.Output)
            return True
        else:
            self.espacio.textEdit.setText('Error')
            self.espacio.Mensaje(resultado)
            return False

    def desconectar(self, algo):
        if self.x == algo:
            self.x = None
            self.Output = None
        if self.salida == algo:
            self.salida = None


class Trigonometrica(Operacion_Compleja):
    def conectar(self, algo):
        if self.x is None:
            self.x = str(radians(float(algo.Output)))
            return self.resultado()
        else:
            self.x = None
            return False


class Operacion_MM(Bloque):
    def __init__(self, operacion, espacio):
        super(Operacion_MM, self).__init__(operacion, espacio)
        self.lista = []

    def conectar(self, algo):
        self.lista.append((algo))
        if not self.resultado():
            self.lista.remove(algo)
            return False
        else:
            return True

    def resultado(self):

        if len(self.lista) == 1:
            self.Output = float(self.lista[0].Output)
            self.espacio.textEdit.setText(str(self.Output))
            return True
        else:
            tupla = '('
            for i in self.lista:
                tupla += i.Output + ','
            tupla += ')'
        operacion = ('{0}{1}'.format(self.operacion, tupla))
        factible, resultado = evaluar(operacion)
        if factible:
            self.Output = resultado
            self.espacio.textEdit.setText(str(resultado))
            return True
        else:
            self.espacio.textEdit.setText('Error')
            self.espacio.Mensaje(resultado)
            return False

    def desconectar(self, algo):
        if algo in self.lista:
            self.lista.remove(algo)
        if len(self.lista) == 0:
            self.Output = None
        else:
            self.resultado()
