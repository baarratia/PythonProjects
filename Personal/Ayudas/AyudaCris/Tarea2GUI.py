import tkinter

def cambiar_nombre_ventana(nombre_ventana):
    t.title(nombre_ventana)

def nueva_ventana(ancho_ventana,largo_ventana):
    global t
    global h_window
    global w_window

    h_window = largo_ventana
    w_window = ancho_ventana
    t = tkinter.Tk()

def cargar_imagen(nombre_archivo):
    global texto_imagen
    pixeles = []
    try:        
        f = open(nombre_archivo+'.txt','r')
        pixeles = []
        for line in f:
            line = line.strip("\n")
            line = line.strip(";")
            pixeles.append(line.split(";"))
        f.close()
        return pixeles
    except:
        return []

def guardar_imagen(imagen,nombre):
    try:
        f = open(nombre+'.txt', 'w')
        for i in range(len(imagen)):
            string = ""
            for j in range(len(imagen[0])):
                string += str(tuple(imagen[j][i]))+";"
            f.write(string+"\n")
        f.close()
        return True
    except:
        return False

def inicializar_lienzo(alto_1,ancho_1,alto_2,ancho_2):
    global image_1
    global image_2


    image_1 = tkinter.PhotoImage(width=ancho_1,height=alto_1)
    image_2 = tkinter.PhotoImage(width=ancho_2,height=alto_2)


def dibujar_pixel(num,r,g,b,i,j):
    a = r,g,b
    if num == 1:
        image_1.put("#%02x%02x%02x" % tuple(a),to=(i,j))
    else:
        image_2.put("#%02x%02x%02x" % tuple(a),to=(i,j))
   
def desplegar_imagenes(x_imagen1,y_imagen1,x_imagen2,y_imagen2,x_texto1,y_texto1,x_texto2,y_texto2,texto1,texto2):
    c = tkinter.Canvas(t, width=w_window, height=h_window)
    c.pack()
    c.create_image(x_imagen1, y_imagen1, image = image_1, anchor=tkinter.NW)
    c.create_image(x_imagen2, y_imagen2, image = image_2, anchor=tkinter.NW)
    c.create_text(x_texto1, y_texto1, text= texto1)
    c.create_text(x_texto2, y_texto2, text= texto2)
    t.mainloop()
