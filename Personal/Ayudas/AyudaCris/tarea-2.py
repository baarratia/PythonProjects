import Tarea2GUI


print("********* BIENVENIDO AL EDITOR DE IMAGENES DE PYTHON *********\n"
      "En este programa vas a poder abrir, editar y guardar imagenes\n"
      "**************************************************************")
qh=input("* Qué deseas hacer?:\n"
             "1.- Abrir una imagen\n"
             "2.- Editar la imagen actual\n"
             "3.- Guardar la imagen actual\n"
             "4.- Ver imagen actual\n"
             "5.- Salir\n"
             "OPCIÓN:  ")
imagenabierta=""
while qh!="5":
    if qh=="1":
        qaa=input("Diga el nombre del archivo:  ")
        if qaa=="bb8":
            imagen=Tarea2GUI.cargar_imagen("bb8")
            imagenabierta="si"
            print("Imagen cargada con éxito!... Ahora puedes editarla")
        elif qaa == "dora":
            imagen = Tarea2GUI.cargar_imagen("dora")
            imagenabierta = "si"
            print("Imagen cargada con éxito!... Ahora puedes editarla")
        elif qaa == "gato":
            imagen = Tarea2GUI.cargar_imagen("gato")
            imagenabierta = "si"
            print("Imagen cargada con éxito!... Ahora puedes editarla")
        elif qaa == "mario":
            imagen = Tarea2GUI.cargar_imagen("mario")
            imagenabierta = "si"
            print("Imagen cargada con éxito!... Ahora puedes editarla")

    elif qh=="2":
        if imagenabierta=="si":
            ee=input("* Qué edición quieres realizar?:\n"
                           "1.- Cambiar a sepia\n"
                           "2.- Difuminar\n"
                           "3.- Invertir horizontalmente\n"
                           "4.- Invertir verticalmente\n"
                           "5.- Invertir colores (negativo)\n"
                           "Opción: ")
            if ee=="1":
                Tarea2GUI.nueva_ventana(2.54 * len(imagen), 1.3 * len(imagen[0]))
                Tarea2GUI.cambiar_nombre_ventana("Tarea 2")
                Tarea2GUI.inicializar_lienzo(len(imagen[0]), len(imagen), len(imagen[0]), len(imagen))
                for x in range(len(imagen)):
                    for y in range(len(imagen[0])):
                        pixel = imagen[x][y]
                        pixel = pixel.strip("(")
                        pixel = pixel.strip(")")
                        pixel = pixel.split(",")
                        r = int(pixel[0])
                        g = int(pixel[1])
                        b = int(pixel[2])
                        Tarea2GUI.dibujar_pixel(1, r, g, b, x, y)
                for x in range(len(imagen)):
                    for y in range(len(imagen[0])):
                        pixel = imagen[x][y]
                        pixel = pixel.strip("(")
                        pixel = pixel.strip(")")
                        pixel = pixel.split(",")
                        r = int(0.393 * float(pixel[0]) + 0.769 * float(pixel[1]) + 0.189 * float(pixel[2]))
                        g = int(0.349 * float(pixel[0]) + 0.686 * float(pixel[1]) + 0.168 * float(pixel[2]))
                        b = int(0.272 * float(pixel[0]) + 0.534 * float(pixel[1]) + 0.131 * float(pixel[2]))
                        if r > 255:
                            r = 255
                        if b > 255:
                            b = 255
                        if g > 255:
                            g = 255

                        Tarea2GUI.dibujar_pixel(2, r, g, b, x, y)

                Tarea2GUI.desplegar_imagenes(30, 30, 1.4 * len(imagen), 30, 0.5 * len(imagen) + 25, 50 + len(imagen[0]),
                                             1.8 * len(imagen) + 25, 50 + len(imagen[0]), "Original",
                                             "Editada")
                print("Se ha cerrado la ventana")

            elif ee=="2":
                Tarea2GUI.nueva_ventana(2.54 * len(imagen), 1.3 * len(imagen[0]))
                Tarea2GUI.cambiar_nombre_ventana("Tarea 2")
                Tarea2GUI.inicializar_lienzo(len(imagen[0]), len(imagen), len(imagen[0]), len(imagen))
                for x in range(len(imagen)):
                    for y in range(len(imagen[0])):
                        pixel = imagen[x][y]
                        pixel = pixel.strip("(")
                        pixel = pixel.strip(")")
                        pixel = pixel.split(",")
                        r = int(pixel[0])*8
                        g = int(pixel[1])*8
                        b = int(pixel[2])*8
                        c = 0
                        for i in range(-1,2):
                            for j in range(-1,2):
                                if (0 <= x + i <= len(imagen)) and (0 <= y + j <= len(imagen[0])):
                                    c += 1
                                    pixel2 = imagen[x + i][y +j]
                                    pixel2 = pixel2.strip("(")
                                    pixel2 = pixel2.strip(")")
                                    pixel2 = pixel2.split(",")
                                    r += int(pixel2[0])
                                    g += int(pixel2[1])
                                    b += int(pixel2[2])
                        r = r/c
                        g = g/c
                        b = b/c
                        Tarea2GUI.dibujar_pixel(1, r, g, b, x, y)
                Tarea2GUI.desplegar_imagenes(30, 30, 1.4 * len(imagen), 30, 0.5 * len(imagen) + 25, 50 + len(imagen[0]),
                                            1.8 * len(imagen) + 25, 50 + len(imagen[0]), "Original", "Editada")


            elif ee=="3":
                Tarea2GUI.nueva_ventana(2.54 * len(imagen), 1.3 * len(imagen[0]))
                Tarea2GUI.cambiar_nombre_ventana("Tarea 2")
                Tarea2GUI.inicializar_lienzo(len(imagen[0]), len(imagen), len(imagen[0]), len(imagen))
                for x in range(len(imagen)):
                    for y in range(len(imagen[0])):
                        pixel = imagen[x][y]
                        pixel = pixel.strip("(")
                        pixel = pixel.strip(")")
                        pixel = pixel.split(",")
                        r = int(pixel[0])
                        g = int(pixel[1])
                        b = int(pixel[2])
                        Tarea2GUI.dibujar_pixel(1, r, g, b, x, y)
                for x in range(len(imagen)):
                    for y in range(len(imagen[0])):
                        pixel = imagen[-x][y]
                        pixel = pixel.strip("(")
                        pixel = pixel.strip(")")
                        pixel = pixel.split(",")
                        r = int(pixel[0])
                        g = int(pixel[1])
                        b = int(pixel[2])
                        Tarea2GUI.dibujar_pixel(2, r, g, b, x, y)

                Tarea2GUI.desplegar_imagenes(30, 30, 1.4 * len(imagen), 30, 0.5 * len(imagen) + 25, 50 + len(imagen[0]),
                                             1.8 * len(imagen) + 25, 50 + len(imagen[0]), "Original", "Editada")
                print("Se ha cerrado la ventana")
            elif ee=="4":
                Tarea2GUI.nueva_ventana(2.54 * len(imagen), 1.3 * len(imagen[0]))
                Tarea2GUI.cambiar_nombre_ventana("Tarea 2")
                Tarea2GUI.inicializar_lienzo(len(imagen[0]), len(imagen), len(imagen[0]), len(imagen))
                for x in range(len(imagen)):
                    for y in range(len(imagen[0])):
                        pixel = imagen[x][y]
                        pixel = pixel.strip("(")
                        pixel = pixel.strip(")")
                        pixel = pixel.split(",")
                        r = int(pixel[0])
                        g = int(pixel[1])
                        b = int(pixel[2])
                        Tarea2GUI.dibujar_pixel(1, r, g, b, x, y)
                for x in range(len(imagen)):
                    for y in range(len(imagen[0])):
                        pixel = imagen[x][-y]
                        pixel = pixel.strip("(")
                        pixel = pixel.strip(")")
                        pixel = pixel.split(",")
                        r = int(pixel[0])
                        g = int(pixel[1])
                        b = int(pixel[2])
                        Tarea2GUI.dibujar_pixel(2, r, g, b, x, y)

                Tarea2GUI.desplegar_imagenes(30, 30, 1.4 * len(imagen), 30, 0.5 * len(imagen) + 25, 50 + len(imagen[0]),
                                             1.8 * len(imagen) + 25, 50 + len(imagen[0]), "Original", "Editada")
                print("Se ha cerrado la ventana")

            elif ee=="5":
                Tarea2GUI.nueva_ventana(2.54 * len(imagen), 1.3 * len(imagen[0]))
                Tarea2GUI.cambiar_nombre_ventana("Tarea 2")
                Tarea2GUI.inicializar_lienzo(len(imagen[0]), len(imagen), len(imagen[0]), len(imagen))
                for x in range(len(imagen)):
                    for y in range(len(imagen[0])):
                        pixel = imagen[x][y]
                        pixel = pixel.strip("(")
                        pixel = pixel.strip(")")
                        pixel = pixel.split(",")
                        r = int(pixel[0])
                        g = int(pixel[1])
                        b = int(pixel[2])
                        Tarea2GUI.dibujar_pixel(1, r, g, b, x, y)
                for x in range(len(imagen)):
                    for y in range(len(imagen[0])):
                        pixel = imagen[x][y]
                        pixel = pixel.strip("(")
                        pixel = pixel.strip(")")
                        pixel = pixel.split(",")
                        r = int(255 - float(pixel[0]))
                        g = int(255 - float(pixel[1]))
                        b = int(255 - float(pixel[2]))
                        Tarea2GUI.dibujar_pixel(2, r, g, b, x, y)

                Tarea2GUI.desplegar_imagenes(30, 30, 1.4 * len(imagen), 30, 0.5 * len(imagen) + 25, 50 + len(imagen[0]),
                                             1.8 * len(imagen) + 25, 50 + len(imagen[0]), "Original",
                                             "Editada")
                print("Se ha cerrado la ventana")


        else:
            print("Inválido,primero debes abrir una imagen.")

    print("**************************************************************")
    qh = input("* Qué deseas hacer?:\n"
                   "1.- Abrir una imagen\n"
                   "2.- Editar la imagen actual\n"
                   "3.- Guardar la imagen actual\n"
                   "4.- Ver imagen actual\n"
                   "5.- Salir\n"
                   "OPCIÓN:  ")
if qh=="5":
    print(">> Adios!")