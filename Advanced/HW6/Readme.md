Tarea 6
==========

Bienvenidos a la guia de usuario de Ichat beta:


***Instrucciones de uso:***

Para iniciar el programa, se debe ejecutar el archivo StartServer.py y el archivo Lobby.py por cada
usuario que se desee conectar, recomendamos probar con dos o 3 usuarios conectados, ya que si no
el chat puede ser un tanto solitario...

**Primeros Pasos:**


        Registrarse:   Como todo servicio de mensajería, Ichat pide a los usuarios registrarse
                       antes de poder usar sus servicios, por lo que al iniciar el programa
                       por primera vez, en la ventana inicial, de LogIn, se debe pinchar en 
                       Registrar Nuevo Usuario.
                       Tras esto surgirá una nueva ventana, donde deberás ingresar tus datos y 
                       contraseña. Recordar que Ichat es un servicio de mensajería auspiciado 
                       por la PUC, por lo que tu nombre de usuario debe ser tu correo uc, es decir
                       debe terminar en "@puc.cl" o "@uc.cl", mientras que la contraseña ingresada
                       debe tener al menos 8 carácteres, una Mayuscula, Mínusculas y al menos 1 
                       número.
                       
                           
        Iniciar Sesión:  Si es primera vez que usas el programa, al momento de registrarte se iniciará
                         la sesión automáticamente, en el caso de que estés registrado de antes, deberás
                         escribir tu correo uc y contraseña, si estos son válidos el servidor te permitirá
                         iniciar sesión correctamente, y podrás ingresar al Lobby del chat.
                         Como esta todavía es una versión beta del programa, si te equivocas ingresando tus
                         datos, te mostratrá un mensaje de advertencia, pero al momento de intentar nuevamente
                         el programa no podrá acceder al servicio, por lo que en estos casos se recomienda
                         cerrar y volver a iniciar el archivo Lobby.py, para un correcto funcionamiento, 
                         sentimos las molestias.
                           
        Lobby:    En el Lobby podrás encontrar toda la información y botones claves para tu interacción con
                  el programa y el resto de los usuarios. Cuenta con dos QListViews, una que muestra las 
                  conversaciones y grupos activos, y otra que meustra los usuarios conectados.
                  Si un usuario te habla, su nombre aparecerá en la lista de conversaciones activas, y con
                  solo pinchar el nombre podrás abrir la Ventana del chat correspondiente y poder comunicarte.
                  Si en cambio, eres alguien que toma la iniciativa, para iniciar una conversación tu mismo
                  bastará con presionar sobre el nombre de un usuario en la lista de usuarios conectados, 
                  lo que generará automáticamente un a pestaña de conversación.
                  
                  Por otro lado, si eres un ser más sociable todavía, y no te basta solo con hablar con una
                  persona, Ichat ofrece la opción de chats grupales. Basta con presionar el botón Nuevo Grupo
                  donde podrás marcar a los usuarios actualmente conectados con los que deseas hablar, pero
                  siempre recuerda nombrar al grupo, ya que si no, no podrás crearlo.
                  Con el grupo ya creado, podrás contar con las mismas ventajas del chat entre dos personas, 
                  pero incluyendo tantas personas como desees a la conversación.
                  
        Pestañas de Chat:       Tanto en las pestañas de chat básico como en las grupales los funcionamientos
                                son parecidos, escribe lo que deseas comunicar, presiona enviar y el destinatario
                                lo recibirá. 
                                Además estamos implementando una nueva tecnología en colaboración con Google (si,
                                Google), donde si quieres puedes escribir una palabra entre $$, por ejemplo, 
                                si quieres mandr una imagen de Godzilla, basta con que escribas $$Godzilla$$
                                y tu destinatario se llevará un gran susto, ya que aparecerá una imagen del 
                                mismisimo en su pantalla, esta tecnoogía está aún en desarrollo, por lo que 
                                como compañía pedimos paciencia, ya lanzaremos una actualización que mejore
                                el funcionamiento, agradecemos la comprensión de nuestro público.
                                
        Cerrar Sesión:      Como su nombre lo dice, este botón te permite cerrar sesión de nuestro servicio, 
                            aunque todavía no encontramos una razón por no estar todo el día conectado a esta
                            tan innovadora plataforma... (Perderás tus conversaciones actuales si cierras sesión, 
                            más razones por la que no cerrar nunca el programa...)
                  

***Organización del Código***

La estructura creada está bastante ordenada y separada por módulos por temática para poder
hacer más fácil la corrección por parte de los Ayudantes.


        Ichat.py:   Base de conectividad del programa, aquí podremos encontrar las clases
                 Cliente y Servidor, con sus respectivos atributos, métodos y señales
                 para poder interactuar correctamente con las interfaces.
                   
        Manejo_de_informacion.py:       En este archivo podremos encontrar todo lo relacionado
                                        con la importante seguridad de nuestros usuarios, aquí
                                        se maneja la creación de nuevos usuarios, el cuidadoso
                                        guardado de sus contraseñas usando hash+salt para asegurarlas.
                                        También es donde se comprueban que los datos ingresados
                                        por el usuario al momento de iniciar sesión seán correctos
                                        y de ser así, se pueda ingresar al servicio.
                                        En esta parte se usa regex (re) para el manejo de strings, 
                                        tal como se pide.
                                        
        Buscar_Imagenes.py:     Como puede hacer suponer el nombre, este archivo se encarga de gurdar
                                las funciones que, dado el mensaje que se envia en un chat, verifican
                                si existe alguna palabra entre $$ y si es así, usando request y la api
                                de google images, busca y descarga la imagen solicitada, retornando
                                el nombre de esta, para que luego la ventana de chat la pueda setear
                                como miniatura en la Qtextbrowser que poseen todos los chats.
                                  
        Lobby.py:     El lobby es tanto el centro de operaciones del usuario, como del programa, en este se
                   ejecutan todas las funciones y ventanas, y, como había comentado antes, es necesaria la ejecución
                   de este para poder iniciar el porgrama desde la perspectiva del usuario.
                   
        StartServer.py:     Programa simple que importa y ejecuta el server, para que los usuarios puedan conectarse
                            al servicio.
                            
         Otros:         El resto de los archivos son más que nada interfaces gráficas con sus respectivos botones
                        y señales conectadas y listas para aportar en el funcionamiento del programa.
                    
Finalmente, ayudantes, no me dio el tiempo para poder adjuntar archivos (consideren que estamos en periodo de examenes
y hay que salvar todo...) pero nuestra compañía espera mandar una actualización en un tiempo... 
Otra cosa, para que no tengan que registrar varios usuarios para probar, dejé ya guardados unos usuarios de ejemplo
con los que se pueden conectar y probar, estos son:

ejemplo@uc.cl pass= Ejemplo123
ejemplo2@puc.cl pass = Ejemplo456
baarratia@uc.cl pass = Artemis611
cbcornejo@uc.cl pass = Cata123
f@uc.cl pass = Francisco1


