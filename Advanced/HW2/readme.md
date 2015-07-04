Tarea 2
==========

Bienvenidos a la guia de usuario del mapa amarillo. (sigue el camino amarillo :D )

Funcionalidades:

***Carga de datos***

Al ejecutar el main del programa, este comenzará a leer los archivos entregados
con la función Lector, que crea las listas tal como son señaladas en los archivos
de textos.
Tras la carga de archivos comienza la creación de los objetos ubicaciones,
los cuales contienen todos los datos de la posición en el espacio de cada objeto,
de manera vertical. Al hacer esto se modifica la lista tipos, que ahora será
una lista de todos los objetos recién creados. Con esto se instancia la clase Mapa.
Esta clase tiene como atributos la lista de los objetos ubicaciones, y el zoom actual,
aparte de tener metodos que ajustan lo que se debe ver en el mapa dependiendo del zoom
existente en ese momento.
Finalmente instanciamos la clase Tarea, que recibe el mapa recién instanciado y que
se encarga de crear la sub-grilla inicial, hacer variar el zoom y permite movernos por
el mapa en la interfaz, aparte cuenta con 5 metodos que son las consultas señaladas en
el enunciado de la tarea.


***Consultas Globales***


 * **Cantidad de ubicaciones por región:** Recibe como parametros un tipo de ubicación y una región,
                                           se busca cuantos de este tipo de ubicación hay por cada tipo
                                           de región especificada, y se imprimen en la pantalla de la
                                           interfaz.
                                           La funcionalidad de esta función está basada en el uso de diccionarios
                                           y se interactúa también con los objetos ubicaciones.
 * **Regiones sin ubicaciones:** Recibe como parametros uno o más tipos de ubicación, y una región, con lo que
                                 se trabaja y retorna al usuario el nombre de los paises que no contienen los tipos
                                 de ubicación entregados.


***Consultas Sub-Grilla Actual***


 * **Cantidad de ubicación en distancia:** Recibe como parametros un nombre de una ubicación y un número que representa
                                           las grillas de distancia para buscar y contarlo.
                                           _________
                                          |    |    |
                                          |_A__|____|       Como se puede ver en el diagrama de al lado,
                                          |    |    |       una grilla nueva será la que no poseé ningín
                                          |____|____|       elemento en común con la otra, es decir, para llegar
                                           _________        de B a A se debe presionar dos veces la flecha de movimiento.
                                          |    |    |
                                          |_B__|____|       Cabe señalar que para que este programa funcione,
                                          |    |    |       el mapa debe estar en un nivel de zoom igual a 6,
                                          |____|____|       que es exactamente el nivel donde se encuentran los tipos
                                                            de ubicaciones buscados.

        *El sistema recorre en forma de cruz, es decir con cuatro bloques: superior, inferior, derecho, izquierdo

 * **Distancia a n ubicaciones:** El sistema recorrerá por bloques en forma de cruz, similar a la funcionalidad anterior,
                                  pero esta vez buscando una cantidad, entregada por el usuario, de cierto tipo de ubicación
                                  también entregado por este. Para finalmente retornar la cantidad de movimientos que se tuvo
                                  que recorrer para lograr encontrar esta cantidad asignada, en las subgrillas adyacentes a
                                  la que se visualiza en el mapa.