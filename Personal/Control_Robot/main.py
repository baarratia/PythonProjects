def interfaz():
    #conectarse con el robot
    #verificar camara
    while True:
        i = input('Que hacer?: ').strip()
        #detectar x1, y1, x2, y2 del robot

        if i == 'Centro':
            pass  # Saber donde estoy y donde esta el centro, ejecutar funcion seguir con esos datos

        if i == 'Balon':
            pass  # Ir hacia la pelota, usando la funcion que ya esta casi lista en detectar colores

        if i == 'Recta':
            pass  # Mover la pelota en linea recta

        if i == 'Girar':
            pass  # Girar con la pelota

        if i == 'Arco':
            pass  # Ir hacia el arco a defender

        if i == 'Defender':
            pass  # ponerse entre la pelota y el arco

        if i == 'Achicar':
            pass  # evitar que la pelota en movimiento entre al arco, tal vez se podria usar lo mismo que en balon

        if i == 'Gol':
            pass  # llevar la pelota al arco enemigo

        if i == 'Pasear':
            pass  # pasearse al robot enemigo, esquivarlo, rodearlo, hacerle un jara

        if i == 'Patear':
            pass  # Avanzar hacia la pelota, pegarle y frenar, con angulo hacia el arco enemigo.

        if i == 'Exterminar':
            pass #Ir hacia el robot enemigo y exterminarlo, luego proceder con el grupo dueño del robot

        if i == 'Salir':
            break


interfaz()
