print("\nHola, bienvenido al tragamonedas. Para comenzar a jugar, debes disponer de minimo $500.\n")
bols = 0
contador = 0
while (bols < 500) and (contador < 2):
    contador = contador + 1
    bols = int(input("Cuanto dinero dispones para gastar?: "))
if contador == 2 and bols < 500:
    print("No puedes apostar menos de $500. Fin de juego.")
else:
    print("Que comience el juego!")

    ganancia = 0
    apuesta = 0
    puntaje = 0

    while True:
        # {quiero que solo aparezca al principio. Puedo definir las funciones fuera del while ?

        print("Estado actual de rodillo")
        print(CorrerRodillo())
        puntaje = 0
        apuesta = 0
        apuesta = int(input("Cuanto quieres apostar (Minimo $10 y maximo $500)?: "))
        contpreg = 0

        while apuesta < 9 or apuesta > 500:
            apuesta = int(input("La apuesta minima es $10 y maximo $500. Cuanto quieres apostar?: "))
            contpreg +=1
            if contpreg == 3:
                break
        while apuesta > 10 and apuesta < 501:
            ganancia = (bols - apuesta) + apuesta * puntaje

        pregunta = str(input("Quieres seguir jugando?(responde si o no): "))
        if pregunta == "no":
            print("Gracias por jugar! \nHasta luego")
            break

        while pregunta == "si":
            apuesta = bols
            apuesta = int(input("Cuanto quieres apostar (Minimo $10 y maximo $500)?: "))
            while apuesta < 10 or apuesta > 500:
                apuesta = int(input("Cuanto quieres apostar (Minimo $10 y maximo $500)?: "))
                break
            print(CorrerRodillo())

            print("Tienes $", bols, "en tu bolsillo")

            print(apuesta)
            print(ganancia)
            print(bols)
            print(puntaje)
