__author__ = 'Benja'
import socket


class Comunicador_Robot:
    def __init__(self):
        self.TCP_IP = '192.168.0.139'  # Conexi�n IP del modulo WiFly al cual se conectar�
        self.TCP_PORT = 2000  # Puerto al cual se enviar� la informaci�n
        self.BUFFER_SIZE = 20  # Tama�o del buffer que almacena la informaci�n enviada
        self.MESSAGE = "Listo"
        self.PASS = b"G02"  # Password de su modulo inal�mbrico
        self.CONNECTED = False
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.TCP_IP, self.TCP_PORT))
        self.conectar()

    def conectar(self):
        while True:
            data = self.s.recv(self.BUFFER_SIZE)
            data = data.decode('utf-8')
            print("received data:", data)
            if data == "PASS?":
                self.s.send(self.PASS)

            elif data == "AOK":
                self.CONNECTED = True
                break

            else:
                self.CONNECTED = False
                break

    def escuchar_enviar(self, data):
        data = str(data)
        if self.CONNECTED:
            MESSAGE = data.encode('utf-8')
            self.s.send(MESSAGE)
            print(data)
