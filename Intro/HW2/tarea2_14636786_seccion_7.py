import random

from whatsintro_gui import *
from whatsintro_msg import *

# mis funciones:
def listamensaje(mensaje):
    lista = []
    for i in mensaje:
        a = ord(i)
        b = bin(a)
        b = b[2:]
        s = str(b)
        b = s.zfill(8)
        lista.append(b)
        mensajebin = "".join(lista)
    return mensajebin


def cadenaAleatoria():
    cadena = []
    for i in range(10):
        a = random.randint(0, 9)
        cadena.append(str(a))
    cadena = "".join(cadena)
    return cadena


def ListaDeNumeros():
    ldn = []
    for i in range(0, 256):
        ldn.append(i)
    return ldn


def union_clavecadena(clave, cadena):
    cdi = []
    c = clave + cadena
    for i in range(0, 10):
        cdi.append(c)
    cdi = "".join(cdi)
    cdi = cdi[:256]
    cdi = list(cdi)
    return cdi


def intercambios(ldn, cdi):
    for i in range(len(ldn)):
        j = i + int(cdi[i])
        if j > 255:
            j -= 256
        a = ldn[i]
        ldn[i] = ldn[j]
        ldn[j] = a
    return ldn


def ldnabin(ldn):
    lista = []
    for i in range(len(ldn)):
        a = ldn[i]
        b = bin(a)
        b = b[2:]
        b = b.zfill(8)
        lista.append(b)
    ldnbin = "".join(lista)
    return ldnbin


def compararcadenas(ldnbin, mensajebin):
    mc = []
    for i in range(len(mensajebin)):
        if mensajebin[i] == ldnbin[i]:
            mc.append(str(0))
        if mensajebin[i] != ldnbin[i]:
            mc.append(str(1))
    mc = "".join(mc)
    return mc


def desencriptar(m, clave):
    m = list(str(m))
    CA = ''.join(m[0:10])
    me = ''.join(m[10:])
    ldn = ListaDeNumeros()
    cdi = union_clavecadena(clave, CA)
    ldn = intercambios(ldn, cdi)
    ldnbin = ldnabin(ldn)
    mbin = compararcadenas(ldnbin, me)
    mbin = list(mbin)
    lista = []
    for i in range(int(len(mbin) / 8)):
        x = ''.join((mbin[8 * i:(i + 1) * 8]))
        x = int(x, 2)
        x = chr(x)
        lista.append(x)
    mensaje = ''.join(lista)
    return mensaje


def tarea(tablero):
    usuario = '@baarratia'
    clave = '7242583640253750'
    conect = conectar(usuario, clave)
    if conect == False:
        agregar_mensaje_al_inicio('', '', 'Error de conexión')
        pass  #####
    emisor(usuario)
    print(conectar(usuario, clave))
    while True:
        k = 0
        l = 0
        click = esperar_click()
        if click == 'enviar':
            mensaje = (mensaje_redactado()).strip()
            if len(mensaje) < 247:
                mensajebin = listamensaje(mensaje)
                cadena = cadenaAleatoria()  # 3
                cdi = union_clavecadena(clave, cadena)  # 4
                ldn = ListaDeNumeros()  # 5
                ldn = intercambios(ldn, cdi)
                ldnbin = ldnabin(ldn)
                mc = compararcadenas(ldnbin, mensajebin)  # 6
                mae = cadena + mc  # 7
                ve = validar_encriptacion(mensaje, mae)
                a, b = enviar_mensaje(mae)
                if a == True:
                    borrar_mensaje_redactado()
                else:
                    borrar_lista_mensajes()
                    agregar_mensaje_al_inicio('', '', b)
            else:
                agregar_mensaje_al_inicio('El mensaje', 'debe tener máximo', '246 caracteres, intentelo nuevamente')
        if click == 'recibidos':
            borrar_lista_mensajes()
            cr = cantidad_recibidos()
            while k <= cr - 1:
                mr = (str(mensaje_recibido(k))).split('\n')
                de = mr[0]
                para = mr[1]
                encriptado = mr[2]
                msg = desencriptar(encriptado, clave)
                agregar_mensaje_al_inicio(de, para, msg)
                k += 1
        if click == 'enviados':
            borrar_lista_mensajes()
            ce = cantidad_enviados()
            while l <= ce - 1:
                mE = (str(mensaje_enviado(l))).split('\n')
                de = mE[0]
                if de == "None":
                    continue
                para = mE[1]
                encriptado = mE[2]
                msg = desencriptar(encriptado, clave)
                agregar_mensaje_al_inicio(de, para, msg)
                l += 1


app = Application("tarea")
app.title('WhatsIntro')
app.loadProgram(tarea)
app.start()
