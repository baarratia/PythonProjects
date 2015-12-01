# -*- coding: utf-8 -*-
__author__ = 'Benja'
import socket

TCP_IP = '192.168.0.139'  # Conexión IP del modulo WiFly al cual se conectará
TCP_PORT = 2000  # Puerto al cual se enviará la información
BUFFER_SIZE = 20  # Tamaño del buffer que almacena la información enviada
MESSAGE = "Listo"
PASS = b"G02"  # Password de su modulo inalámbrico
CONNECTED = False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while True:

    data = s.recv(BUFFER_SIZE)
    data = data.decode('utf-8')
    print("received data:", data)
    if data == "PASS?":
        s.send(PASS)

    elif data == "AOK":
        CONNECTED = True
        break

    else:
        CONNECTED = False
        break

while CONNECTED:

    MESSAGE = input("Ingrese Comando:\n").encode('utf-8')

    if MESSAGE == "c":
        break

    else:
        s.send(MESSAGE)
        print("meensajeenviado")

s.close()

quit()
