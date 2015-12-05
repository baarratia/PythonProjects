from Comunicador import Comunicador_Robot

comunicacion = Comunicador_Robot()
if comunicacion.CONNECTED:
    while True:
        r = input('Ingresa Tupla:').strip()
        comunicacion.escuchar_enviar(r)

