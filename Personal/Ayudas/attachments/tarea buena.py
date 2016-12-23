import mezclador

def comprobar(palabra, x):
    for letra in palabra:
        if letra not in x:
            print("La palabra no esta escrita con las letras del pozo")
            return False          
               
    for i in x:
        a = 0
        for j in x:
            if j == i:
                a += 1
        b = 0
        for z in palabra:
            if z == i:
                b += 1
            if b > a:
                print("Repetiste letra!")
                return False
        
                      
        if mezclador.existe_palabra(palabra) and mezclador.palabra_usada(palabra)==False:
            print("Tu palabra existe y no fue usada")
            mezclador.agregar_palabra(palabra)
            return True
                
        elif mezclador.palabra_usada(palabra)==True:
            print("La palabra ya fue usada")
            return False

def player(jugador, puntaje, paso):
    oportunidades = 3
    reordenar = 3
    paso = 0
    salir = False
    while oportunidades > 0:
        print("Turno de", jugador,":")
        print()
        print("Que quieres hacer?")
        print()
        quequiereshacer= int(input("""
   Coloca 1 si quieres ingresar una palabra.
   Coloca 2 si quieres reordenar las letras
   Coloca 3 si quieres pasar de turno.
   Coloca 4 si quieres salir  """))
        if quequiereshacer==1:
            print()
            palabra=input("Ingresa palabra: ").upper()
            q = comprobar(palabra, x)
            if q is True:
                if len(x)>len(palabra):
                   puntaje+=5*len(palabra)
                   
                else:
                    puntaje+=2*len(palabra)
                oportunidades=0
                    
            else:
                oportunidades -= 1    
                puntaje-=2*len(palabra)
                print ("Te quedan", oportunidades, "oportunidades para escribir una palabra valida")
                
            oportunidades -= 1
            
            
        elif quequiereshacer==2:
            if reordenar>0:
                print()
                print("Quiero reordenar las letras")
                print(mezclador.reordenar_palabra(x))
                reordenar-= 1
                print("Te quedan",reordenar,"veces para reordenar")
            if oportunidades == 0:
                oportunidades = 0 
                
          
          
        elif  quequiereshacer==3:
            print()
            print("Paso") 
            paso += 1
            print("Has pasado",paso ,"veces")
            if paso==2:
                oportunidades =0
                
        
         
        else:
            print()
            print("Quiero salir")
            salir = True
            oportunidades=0
            
        
            
        
        print("Tu puntaje es", puntaje,"\n")
        print()
    return puntaje, paso, salir 

     
print(".................................................")

print("¡¡¡Bienvenidos a Text Twist 3!!!")
print()
print("""Las reglas del juego son las siguientes:
(1)Cada jugador, en su turno, debe intentar escribir una palabra valida.
(2)Una palabra valida es aquella que:
  -Existe
  -No se haya utilizado anteriormente en algun turno
  -Se pueda construir a partir de tres o mas letras del pozo de letras
(3)En su turno, cada jugador tiene 3 oportunidades para escribir una palabra valida
(4) Si ambos jugadores pasan 2 veces seguidas, se acaba el juego.""")
print()
jugador1=str(input("Nombre jugador 1: "))
jugador2=str(input("Nombre jugador 2: "))
cant_letras= int(input("Cuantas letras habran en el pozo (5, 6 o 7)?: "))
x=mezclador.obtener_palabra(cant_letras)


puntajejj1=0
puntajejj2=0
pasojj1 = 0
pasojj2 = 0
juego = True
while juego:
    print(x+"\n")
    print("Tus letras son")
    print(x+"\n")
    puntajejj1, pasojj1, salir = player(jugador1, puntajejj1, pasojj1)
    
    print(".................................................")
    if not salir:     
        print("Tus letras son")
        print(x+"\n")
        puntajejj2, pasojj2, salir = player(jugador2, puntajejj2, pasojj2)
   
    if (pasojj1==2 and pasojj2==2) or salir:
            print("El juego a terminado")
            print("El puntaje de", jugador1, "es", puntajejj1)
            print("El puntaje de", jugador2, "es", puntajejj2)
            if puntajejj1>puntajejj2:
                print("El ganador es", jugador1)
                print("Con", puntajejj1, "puntos")
            elif puntajejj1==puntajejj2:
                print("Hubo un empate")
                print("Con", puntajejj1, "puntos")
            else:
                print("El ganador es", jugador2)
                print("Con", puntajejj2, "puntos")
                   
            juego = False
    
                
    


       
