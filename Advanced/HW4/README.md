Tarea 4
==========

Bienvenidos a la guia de usuario de Dragculadora:

Funcionalidades:

***Menu Principal***

Al ejecutar el main del programa, el usuario accederá inmediatamente a la interfaz gráfica
de la Dragculadora. Esta está compuesta por 3 areas principales:

        Editor Numérico:   Corresponde a una QTextEdit de PyQt4 donde el usuario podrá
                           tanto ingresar datos numéricos para generarlos como bloques,
                           como ir obteniendo de forma automática los resultados de las
                           operaciones efectuadas en el area de trabajo.
                           Cabe destacar que en caso de que el dato ingresado por el 
                           usuario, no sea de caracter numérico, o con alguna inconsistencia
                           de formato, como más de un punto, o espacios, etc... El Editor 
                           Numérico mostrará un mensaje de Error, y no dejará generar ese
                           dato en específico.
                           
        Area de Botones:   En esta area el usuario podrá tanto generar nuevos bloques en
                           el area de trabajo (con tan solo presionar sobre el respectivo
                           QPushButton) como acceder a los botones "Borrar" e "Igual", que 
                           activan estados distintos en el programa.
                           Al presionar el botón "Borrar", este se mantendrá presionado
                           y permitirá borrar los bloques que el usuario presione.
                           El estado de borrador se desactivará al presionar nuevamente
                           sobre el botón, o al cambiar de modo a "Igual".
                           Por otro lado, al presionar el botón "Igual", el botón se 
                           mantenrá presionado, y permitirá obtener el Output, si es que tiene
                           de los bloques que el usuario presione, mostrando estos en el 
                           Editor Numerico, y dejandolos disponibles para generarlos como bloque, 
                           con tan solo presionar "Generar NUM"
                           
        Area de Trbajo:    Corresponde a un MdIArea de PyQt, adaptada para formar un espacio
                           de trabajo amplio y comodo para el usuario. Las grandes acciones
                           del programa ocurren en esta area, donde los bloques aparecerán en 
                           la esquina superior izquierda de esta, y podrán ser desplazados por
                           el usuario sobre el widget, al mantenerlos presionados con el mouse.
                           

***Tipos de Bloques***

Los tipos de bloque están creados en clases_botones.py, todos heredan de la clase Bloque,
que contiene los atributos básicos de estos, que son Operacion, correspondiente al signo
operatorio o valor contenido en el bloque, y espacio, que corresponde al lugar donde está
contenido, en este caso en el Widget. La clase Bloque al mismo tiempo hereda de DragButton, 
clase que hereda de QPushButton, pero le añade la capacidad o método de ser "arrastrable".
A continuación una lista de los tipos de bloque y sus características:

        Numero:    Los bloques más simples, contienen solo un Output con su valor y una salida
                   que es lo que se une a los otros bloques. Son la base de toda operación
                   y cuentan con el color azul al ser creados, son los únicos bloques que
                   no cambian de color al obtener su Output, ya que son los únicos que
                   lo tienen desde el inicio.
                   Los botones que generan bloques numéricos son, Generar NUM, e y pi.
                   
        Operaciones Simple:   Corresponden a las operaciones matemáticas básicas: suma, resta
                              multiplicación, división y potencia. Reciben dos entradas, x e y, 
                              y en el orden en el que estas ingresan será la forma en la que se 
                              calcule el resultado. Es decir, para calcular, por ejemplo, 3-2
                              el usuario deberá generar los 3 bloques (3, - y 2), presionar 
                              el bloque 3, luego presionar el bloque menos, lo que generará
                              la linea correspondiente a la representación gráfica de la unión
                              creada, luego se debe presionar el bloque 2, y finalmente el bloque
                              +, lo que creará la segunda linea de entrada, y causará que este 
                              cambie de color a un azul obscuro, representando que el Output ha 
                              sido generado dentro, y se podrá visualizar en el editor numérico
                              el resultado obtenido.
                              Estas bloques son de color gris en su estado inicial.                        
        
        Operaciones Complejas:    Representadas en primera instancia por el color morado, estas 
                                  operaciones reciben solo una entrada, de la misma forma que
                                  los bloques de operaciones simples, cambiando de color a azul
                                  obscuro.
                                  Hay 5 operaciones complejas en total: log (logaritmo natural), 
                                  abs (valor absoluto), sin (seno), cos(coseno) y tan (tangente)
                                  estos tres últimos pertenecen a la clase Trigonometrica, que hereda
                                  de la Operacion_Compleja, ya que las entradas que reciben, deben
                                  ser interpretadas como radianes, pero las 5 comparten la misma forma 
                                  de armar la operación matemática, es decir, de la forma: funcion(entrada)
                                  
        Operaciones MM:     Estas corresponden al grupo de bloques que son capaces de recibir tantas entradas
                            como el usuario estime conveniente. Representadas por el color celeste al ser 
                            recién creadas, al recibir la primera entrada ya generarán un Output, por lo 
                            que cambiarán a color azul obscuro, pero este Output se irá actualizando a medida
                            que se vayan agregando más valores a su lista de entradas.
                            Las operaciones MM corresponden a max y min, que entregan, respectivamente, el valor
                            máximo y el mínimo, de los valores que tengan conectados.
                    
Cabe destacar que, para eliminar un bloque, este no debe tener una salida asociada, o si no perjudicaría las operaciones
posteriores, por lo que si se desea eliminar un bloque con salidas asociadas, se deberá comenzar eliminando los bloques 
más recientes, o por decirlo de una forma facil de entender, los más arriba de la piramide.
Recordemos que para la correcta asignación de datos, el dato a asignar deberá ser presionado en primer lugar, y luego
la respectiva operación, de esta forma se generará la unión gráfica e interna de estos.


***Testing***

Junto con el programa, se adjunta el archivo Tarea4_test.py, que es un test, bastante sencillo, que utiliza unittest
y una serie de valores random, para probar que la evaluación de datos se efectua correctamente.
Dentro de esta aparte de las pruebas generales que se pueden hacer, agregué una que especificamente prueba con datos
negativos o igual a cero para el logaritmo natural, y una con denominador igual a 0 para la división, que son los casos
críticos donde no se puede llegar a un resultado, pero el programa ya se encarga de solucionarlo y advertir al usuario
que lo que está haciendo no es correcto, por lo que lo buscado en el testing es everiguar si realmente el programa
está advirtiendo en caso de un error de este estilo.
En cuanto a probar el programa para cadenas grandes de bloque, es irrelevante, ya que al comprobar que cada evaluación
de resultados por bloque es correcta, los resultados entre estas lo serán también, ya que se está demostrando que las
operaciones con las que se operaría para unirlas, funcionan bien, por lo que el programa resiste bien y llega a resultados
coherentes, aún cuando las cadenas sean grandes.


                                                                