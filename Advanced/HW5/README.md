Tarea 5
==========

Bienvenidos a la guia de usuario de Poc-Mon!:

Funcionalidades:

***Interfaz de Juego***

Como esta versi�n del juego a�n est� en Beta, para ejecutarlo ser� necesario correr el archivo UI.py, 
m�s adelante se correr�a ejecutando Main.py, pero no corrieron la tarea...(:c)
Al ejecutar el main del programa, el usuario acceder� inmediatamente al juego, donde observar�
los siguientes elementos:

        Poc-Mon:    El protagonista del juego, el usuario lo mueve usando las flechas del teclado
                           
        Fantasmas:   Los enemigos de Pom-Mon, si lo tocan cuando est�n en su estado normal,
                     le restan una vida, si Poc-Mon toca alguno cuando est�n en su modo escape
                     (Azules) huyen inteligentemente de Poc-Mon, ellos se vuelven blancos y vuelan a su base hasta que se recuperan
                     y salen a seguir su cacer�a...
                     Hay dos clases de fantasmas implementadas, el fantasma rojo, que persigue a pacman
                     y el Naranjo, que es tonto y corre aleatoriamente, por falta de tiempo no pude implementar
                     los otros dos, as� que 3 de los 4 fantasmas son tontos y el otro tiene inteligencia(o algo as� :))
                     
        Monedas:    Las hay rojas y amarillas, las rojas le otorgan una vida a poc-mon y activan su
                    superpoder y el terror de sus enemigos, suma 10 puntos (Probabiidad de que aparezcan
                    es de un 3%), las amarillas otorgan 1 punto a pacman.
                    Cuando se acaban las monedas, el juego termina.
                
                           

***Men�s:***

Los distintos Men�s se activan, de diferentes formas, el de Pausa se activa cuando apretas la tecla 'a' del teclado, 
y permite crear una nueva partida, los otros botones que posee ser�n implementados en un futuro cercano (Me falt� tiempo :C)
El menu de SaveAs permite al usuario dar su nombre de usuario, y tras apretar el boton ok, mostrar� el top10 de jugadores
y luego, tras otro ok, mostrar� las 10 mejores partidas del usuario. (Todo esto usando serializaci�n en el archivo Serializar.py
y SaveAs.py en conjunto)


***Maps:***

Consisten en grandes archivos de texto con n�meros, los 0s representan murallas, los 2 monedas, los 7 monedas rojas, y los 1s caminos, 
el resto de los n�meros, como el 5 representan las posiciones iniciales de cada personaje (en el 5 va pacman)