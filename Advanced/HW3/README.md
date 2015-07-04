Tarea 3
==========

Bienvenidos a la guia de usuario de SimulaMercado:

Funcionalidades:

***Menu Principal***

Al ejecutar el main del programa, el usuario accederá al menu principal del simulador.
El usuario avanzará por el menú a base de preguntas que el programa le irá haciendo, 
para de esta forma seleccionar cual simulación correrá, si desea o no imprimir los 
eventos en consola y, en el caso de la segunda simulación, cuantos estacionamientos
tendrá el SuperMercado.


***Simulacion 1***

Esta simulación basada en eventos discretos, programada en los archivos clases1 y clases2
consta de un modelamiento bastante intuitivo, contanto con las clases:

        Tipo_cliente:   Corresponde a los tipos de clientes y sus respectivos atributos
        Cliente:    Corresponde a un cliente en especifico, y cuenta con un atributo tipo,
                    que lo vincula con su respectivo tipo de cliente.
        Producto:   Cuenta con atributos tales como el nombre y la cantidad disponible.
        Linea:      Cuenta con el nombre de esta y una lista de los respectivos productos
                    en ella
        Caja:       Cuenta con una lista de los productos que se pueden adquirir en esta, y
                    una cola con objetos de la clase cliente.
                    
Todas con sus respectivos métodos, para de esta forma generar una interación lo más natural posible.
Finalmente tenemos la clase SuperMercado y la clase Simulación, en la primera se almacena toda la
información de las clases mencionadas anteriormente, y cuenta con metodos para hacer posible la
interacción entre estas. Mientras, por otro lado, la clase Simulación, contiene un SuperMercado y 
los respectivos atributos y metodos para hacer correr correctamente la simulación de eventos discretos
y obtener los datos para generar el posterior recuento.

***Simulacion 2***

Esta simulación aprovecha las heramientas de Simpy3, basandose, y reutilizando codigo de los archivos
clases1 y clases2. Está programada en parte2.py y una de las cosas que destaco de ella es la creación
de la clase SimpyMercado, utilizando el tipo type, de la forma vista en clases, para que este herede
de la clase SuperMercado perteneciente a clases2, para añadir metodos para la utilización de los
beneficios que Simpy ofrece.


***Calculos Reporte***

 * **Total ganado por el supermercado:** Su implementación es muy sencilla, cada vez que un cliente paga en caja, el 
                                         valor pagado se suma a un "contador de ganancias", para luego simplemente
                                         ser llamado tras el termino de la simulación y ser escrito en el reporte.
 
 * **Los 10 productos más vendidos por tipo de cliente.**  Para este cálculo se implementó una función Maximos() en la 
                                                           clase Tipo_Cliente, que toma los valores de un diccionario
                                                           que cuenta durante toda la simulación los productos y su cantidad
                                                           que compran los clientes de un respectivo tipo, para posteriormente
                                                           con Maximos() obtener los 10 productos más comprados por el 
                                                           respectivo tipo.


 * **Gasto promedio por tipo de cliente:** Para este calculo se añadieron dos atributos a la clase tipo_cliente, registro
                                           y gasto. El primero es un contador de clientes del respectivo tipo que van 
                                           entrando al supermercado (Suma valores desde el init de la clase Cliente, tras
                                           elegir el tipo de cliente correspondiente a este) mientras que el segundo
                                           va recibiendo los pagos que hace cada cliente del respectivo tipo.
                                           Así al final de la simulación, solo bastará dividir el gasto por el registro
                                           de cada cliente, para así obtener el gasto promedio por cada tipo e cliente.

 * **Tiempo promedio dentro del supermercado, por tipo de cliente:** Para este cálculo se añadió un atributo Tiempos
                                                                     a la clase tipo_clientes, que consiste en ena lista
                                                                     que va añadiendo valores del tiempo total de cada
                                                                     cliente del respectivo tipo, en el supermercado.
                                                                     Para posteriormente dividir la suma de cada uno de
                                                                     los tiempos en la lista, por el largo de esta, y 
                                                                     así obtener el promedio para cada tipo.
                                                                     
 * **Colas promedio de acuerdo a la cantidad de cajas abiertas:**  Para este cálculo se implemntó un metodo directamente
                                                                   en la simulación, que va calculando el promedio de
                                                                   largos de las colas en cada momento de la simulación
                                                                   para luego simplemente hacer la sumatoria de valores y 
                                                                   partir por el largo de la lista de promedios sacados.
                                                                   
                                                                