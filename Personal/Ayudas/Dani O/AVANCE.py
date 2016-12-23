#FUNCIONES

def moverme_en_tablero(d): #Puedo moverme por filas, y luego por columnas
    archivo = open((d + ".txt"),"r")
    lista_lineas = archivo.read()

    a = lista_lineas.split("\n") #Lista de listas
    tablero = []
    for i in a:
        j = i.split(",")
        tablero.append(j)
    return tablero

def lista_string(tablero): #NO FUNCIONA :(
    for w in tablero:
        p = " "
        string = p.join(w)
    return string

def fila(i):
    fila = []
    for k in tablero[i]:
        fila.append(k)
    return fila

def columna(j):
    columna = []
    for l in range(0,len(tablero)):
        for m in tablero[l][j]:
            columna.append(m)
    return columna
    
#CLASE TABLERO
class Tablero:
    def __init__(self,nombre):
        self.nombre = nombre #Es el nombre del archivo.
        self.tablero = moverme_en_tablero(self.nombre)

    def mostrar_tablero(self): #Consideramos d como la dificultad del juego   
        for i in self.tablero:
            tablero = " ".join(i)
            print(tablero)

            

#BIENVENIDA
print("Bienvenido a Akari")

#Acciones a realizar
print("¿Qué acción desea realizar?")
accion = input("    1. Jugar una nueva partida.\n    2. Jugar una partida guardada anteriormente.\n")

#OTRA OPCIÓN
while accion != "1" and accion != "2":
    print("No es una acción válida, intentalo nuevamente :)!\n")
    print("¿Qué acción desea realizar?")
    accion = input("    1. Jugar una nueva partida.\n    2. Jugar una partida guardada anteriormente.\n")
           
#ACCION 1   
if accion == "1":
    print("¿Qué dificultad quiere jugar?")
    dificultad = input("    1. Fácil.\n    2. Medio.\n    3. Difícil.\n    4. BONUS.\n")

    #OTRA OPCIÓN
    while dificultad != "1" and dificultad != "2" and dificultad != "3" and dificultad != "4":
        print("No es una dificultad válida, intentalo nuevamente :)!\n")
        print("¿Qué dificultad quiere jugar?")
        dificultad = input("    1. Fácil.\n    2. Medio.\n    3. Difícil.\n")

    #DIFICULTAD FÁCIL
    if dificultad == "1":
        print("Has escogido dificultad fácil. Este es tú tablero\n")
        tablero = Tablero("facil")
        tablero.mostrar_tablero()
        dificultad = "facil"
        
    #DIFICULTAD MEDIO
    elif dificultad == "2":
        print("Has escogido dificultad medio. Este es tú tablero\n")
        tablero = Tablero("medio")
        tablero.mostrar_tablero()
        dificultad = "medio"
        
    #DIFICULTAD DIFÍCIL
    elif dificultad == "3":
        print("Has escogido dificultad difícil. Este es tú tablero\n")
        tablero = Tablero("dificil")
        tablero.mostrar_tablero()
        dificultad = "dificil"

    #DIFICULTAD BONUS
    elif dificultad == "4":
        print("Has escogido dificultad bonus. Este es tú tablero\n")
        tablero = Tablero("bonus")
        tablero.mostrar_tablero()
        dificultad = "bonus"

#ACCION 2   
elif accion == "2":
    tablero_a_jugar = input("Por favor digite el nombre escrito correctamente del archivo guardado (FORMATO: dificultad.guardado): ")

    #ARCHIVO NO VÁLIDO
    while tablero_a_jugar != "facil.guardado" and tablero_a_jugar != "medio.guardado" and tablero_a_jugar != "dificil.guardado" and tablero_a_jugar != "bonus":
        print("No es un nombre de archivo válido, intentalo nuevamente :)!\n")
        tablero_a_jugar = input("Por favor digite el nombre escrito correctamente del archivo guardado: ")

    #DIFICULTAD FÁCIL
    if tablero_a_jugar == "facil.guardado":
        print("Tu tablero guardado era de dificultad fácil. Este era tú tablero:\n")
        tablero = Tablero("facil.guardado")
        tablero.mostrar_tablero()
        dificultad = "facil"
        
    #DIFICULTAD MEDIO
    elif tablero_a_jugar == "medio.guardado":
        print("Tu tablero guardado era de dificultad medio. Este era tú tablero:\n")
        tablero = Tablero("medio.guardado")
        tablero.mostrar_tablero()
        dificultad = "medio"
        
    #DIFICULTAD DIFÍCIL
    elif tablero_a_jugar == "dificil.guardado":
        print("Tu tablero guardado era de dificultad dificil. Este era tú tablero:\n")
        tablero = Tablero("dificil.guardado")
        tablero.mostrar_tablero()
        dificultad = "dificil"

    #DIFICULTAD BONUS
    elif tablero_a_jugar == "bonus.guardado":
        print("Tu tablero guardado era de dificultad bonus. Este era tú tablero:\n")
        tablero = Tablero("bonus")
        tablero.mostrar_tablero()
        dificultad = "bonus"

print("\n¡Que comience el juego!")

salir = 1
intentos_correctos = 0
intentos_incorrectos = 0
razon = 0

while salir > 0:
    print("\nLleva", intentos_correctos, " intentos correctos y ", intentos_incorrectos,"intentos incorrectos en esta partida.")
    print("\n¿Qué quiere hacer?")
    hacer = input("    1. Realizar jugada.\n    2. Resolver tablero.\n    3. Eliminar una ampolleta.\n    4. Prender luces.\n    5. Guardar partida actual.\n    6. Salir del juego.\n")

    while hacer != "1" and hacer != "2" and hacer != "3" and hacer != "4" and hacer != "5" and hacer != "6":
        print("No es una acción válida, intentalo nuevamente :)!\n")
        hacer = input("    1. Realizar jugada.\n    2. Resolver tablero.\n    3. Eliminar una ampolleta.\n    4. Prender luces.\n    5. Guardar partida actual.\n    6. Salir del juego.\n")
        
    #ACCIONES EN TABLERO:

    #REALIZAR JUGADA
    if hacer == "1":
        print("Realiza tu jugada...")
        salir = 1
        #cambiar estos valores
        
        intentos_correctos = 0
        intentos_incorrectos = 0
        
        #me imagino que van muchos codigos aca adentro
        # PONE UNA AMPOLLETA EN UNA CELDA
        #VEREFICAR QUE LA CELDA ESTE DENTRO DE LAS DIMENSIONES Y QUE LA AMPOLLETA NO VIOLE REGLAS
            
    #RESOLVER TABLERO
    elif hacer == "2":
        print("Resolviendo tablero...")
        #entregar tablero listo, que fome :(, SE TERMINAR EL JUEGO
        salir = 0
        print("Se ha terminado el juego")
            
    #ELIMINAR AMPOLLETA (OK)
    elif hacer == "3":
        print("Elimina una ampolleta...")
        ampolleta_eliminar = input("¿Que ampolleta quieres eliminar? (FORMATO: fila,columna) (EJEMPLO: 2,3)\n ")
        pos_ae = ampolleta_eliminar.split(",")
        fila_ae = int(pos_ae[0])
        columna_ae = int(pos_ae[1])

        celda_eliminar = tablero.tablero[fila_ae][columna_ae]
        if celda_eliminar == "*":
            tablero.tablero[fila_ae][columna_ae] = "-"
        
        for w in tablero.tablero: #STRING
            p = " "
            string = p.join(w)
            print(string)

        salir += 1

    #PRENDER LUCES
    elif hacer == "4":
        tablero_luces = tablero.tablero
        print("Prendiendo las luces...")
        cont_a=0 #Fila ampolleta
        cont_b=0 #Columna ampolleta
        for a in tablero_luces:
            cont_a+=1
            cont_c=-1
            for b in a:
                cont_b+=1
                cont_c+=1
                if b == "*":
                    print("entre")
                    fila_l = cont_a - 1
                    columna_l = (cont_b % len(tablero_luces))-1
                    print(fila_l,columna_l)
                    print(fila_l,columna_l)

                    #FILAS

                    fila = []
                    for c in tablero_luces[fila_l]:
                        fila.append(c)
                    d = fila
                    
                    if cont_c == 0: #Ampolleta ubicada al principio
                        sig_der = tablero_luces[fila_l][columna_l + 1]
                        for h in range(columna_l+1,len(tablero_luces)):#Reviso a la derecha
                            if tablero_luces[fila_l][h] == "-":
                                tablero_luces[fila_l][h] = "+"
                            else:
                                break

                    elif cont_c == len(tablero_luces)-1: #Ampolleta ubicada al final
                        sig_izq = tablero_luces[fila_l][columna_l - 1]
                        

                    else: #Ampolleta al medio 
                        sig_der = tablero_luces[fila_l][columna_l + 1]
                        sig_izq = tablero_luces[fila_l][columna_l - 1]
                        for h in range(columna_l + 1,len(tablero_luces)): #Reviso a la derecha
                            if d[h] == "-":
                                d[h] = "+"
                            else:
                                break
                        print("llego aquí")
                        print(d)
    

                    cont_h= -1
                    for h in d: #Por cada elemento en la fila
                        if h == "-":
                            cont_h += 1
                            d[cont_h] = "+"

                        elif h == "X":
                            cont_h += 1
                            d[cont_h] = h

                        elif h == "*":
                            cont_h += 1
                            d[cont_h] = "*"
                            
                        else:
                            cont_h += 1
                            d[cont_h] = h

                    print(d)

                    #COLUMNAS

                    columna = []
                    for e in range(0,len(tablero_luces)):
                        for f in tablero_luces[e][columna_l]:
                            columna.append(f)
                    g = columna

                    cont_i = -1
                    for i in g:
                        if i == "-":
                            cont_i += 1
                            g[cont_i] = "+"

                        elif i == "X":
                            cont_i += 1
                            g[cont_i] = i

                        elif i == "*":
                            cont_i += 1
                            g[cont_i] = "*"
                            
                        else:
                            cont_i += 1
                            g[cont_i] = i

                    print(g)
                        

                    """
                    for p in tablero_luces[fila_l]:
                        col = -1
                        if p == "-":
                            col += 1
                            tablero_luces[fila_l][col] = "+"
                            print(col)
                            print(p)
                                           """
        #ilumina todas las celdas que tengan luz

    #GUARDAR PARTIDA ACTUAL (OK)
    elif hacer == "5":
        print("Guardando partida...")
        archivo_guardado = open(dificultad +".guardado.txt","w")
        
        for w in tablero.tablero: #STRING
            p = " "
            string = p.join(w)
            archivo_guardado.write(string + "\n")
            
        archivo_guardado.close()
        print("Partida guardada")
        salir += 1

    #SALIR DEL JUEGO (OK)
    elif hacer == "6":
        print("Haz salido del juego")
        salir = 0
        razon = 1

while razon > 0:
    if razon == 1:
        print("El juego ha terminado porque haz elegido salir del juego. Nos vemos a la próxima :)!")
        razon = -1
    elif razon == 2:
        print("caca")
