# -*- coding: utf-8 -*-
__author__ = 'Benja'
import socket
import threading

from PyQt4 import QtCore

from Manejo_Informacion import *


class Cliente(QtCore.QObject):
    trigger = QtCore.pyqtSignal(object)
    trigger2 = QtCore.pyqtSignal(object)

    def __init__(self, usuario, password, parent=None):
        super(Cliente, self).__init__(parent)
        self.usuario = usuario
        self.password = password
        self.host = '127.0.0.1'
        self.port = 12350
        self.s_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.chats = {}
        self.grupos = {}
        self.conectado = False

    def probarconexion(self, registrar=None):
        try:
            self.s_cliente.connect((self.host, self.port))
            if registrar is None:
                tupla = (self.usuario, self.password)
            else:
                tupla = (self.usuario, self.password, 1)
            self.enviar(tupla)
            validacion = self.s_cliente.recv(1024)
            tupla = pickle.loads(validacion)
            respuesta = tupla[0]
            mensaje = tupla[1]
            if respuesta is True:
                self.conectado = True
                return True, True, mensaje
            else:
                return True, False, mensaje
        except socket.error as err:
            print("No fue posible realizar la conexión " + str(err))
            return False, False, False

    def EnlazarUI(self, lobby):
        self.lobby = lobby

    def escuchar(self):
        while self.conectado:
            try:
                data = self.s_cliente.recv(1024)
                mensaje = pickle.loads(data)
                if type(mensaje) == list:
                    self.trigger.emit(mensaje)
                else:
                    self.trigger2.emit(mensaje)
            except Exception as E:
                print(E)
                print('Esto deberia aparecer solo una vez')
                self.conectado = False

    def enviar(self, mensaje):
        data = pickle.dumps(mensaje)
        self.s_cliente.send(data)

    def Comenzar(self):
        escuchador = threading.Thread(target=self.escuchar, args=())
        escuchador.daemon = True
        escuchador.start()


class Servidor(threading.Thread):
    def __init__(self):
        super().__init__()
        self.host = '127.0.0.1'
        self.port = 12350
        self.s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_servidor.bind((self.host, self.port))
        self.s_servidor.listen(1)
        self.clientes = {}  # clientes conectados
        self.grupos = {}  # Grupos

    def escuchar(self, cliente, nombre):
        conectado = True
        while conectado:
            try:
                data = cliente.recv(1024)
                mensaje = pickle.loads(data)
                if type(mensaje[1]) == list:
                    self.grupos[mensaje[2]] = mensaje[1]
                    for i in mensaje[1]:
                        if i in self.clientes:
                            if i != mensaje[0]:
                                self.enviar(self.clientes[i][0], mensaje)
                else:
                    destino = mensaje[1]
                    if destino in self.clientes:
                        self.enviar(self.clientes[mensaje[1]][0], mensaje)
                    elif destino in self.grupos:
                        mensaje = list(mensaje)
                        mensaje.append('!')
                        mensaje = tuple(mensaje)
                        for i in self.grupos[destino]:
                            if i in self.clientes:
                                if i != mensaje[0]:
                                    self.enviar(self.clientes[i][0], mensaje)
            except:
                print('Se ha perdido la conexion')
                del self.clientes[nombre]
                self.actualizar_conectados()
                conectado = False

    def aceptar(self):
        cliente_nuevo, address = self.s_servidor.accept()
        if str(address) not in self.clientes:
            data = cliente_nuevo.recv(1024)
            tupla = pickle.loads(data)
            nombre = tupla[0]
            password = tupla[1]
            if len(tupla) == 2:
                respuesta, mensaje = Validar_Datos(nombre, password)
            else:
                respuesta, mensaje = Nuevo_Usuario(nombre, password)
            t = (respuesta, mensaje)
            self.enviar(cliente_nuevo, t)
            if respuesta:
                self.clientes[nombre] = (cliente_nuevo, address)
                print('cliente {} ingresa al chat'.format(nombre))
                thread_cliente = threading.Thread(
                    target=self.escuchar, args=(cliente_nuevo, nombre))
                thread_cliente.daemon = True
                thread_cliente.start()
                self.actualizar_conectados()
            else:
                print(mensaje)

    def enviar(self, cliente, mensaje):
        cliente.send(pickle.dumps(mensaje))

    def actualizar_conectados(self):
        lista_clientes = list(self.clientes.keys())
        for i in self.clientes:
            self.clientes[i][0].send(pickle.dumps(lista_clientes))

    def run(self):
        while True:
            try:
                self.aceptar()
            except:
                pass
