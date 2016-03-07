from clases import Robot
# -*- encoding: utf-8 -*-
import math
import os
import pickle
import cv2
import numpy as np
import Automata

# camara 0 notebook
# camara 1 lab
CAM =0
enemigo = Robot()
labestia = Robot(enemigo, True)

def nothing(x):
    pass


cap = cv2.VideoCapture(CAM)
cv2.namedWindow('Configuracion')
cv2.resizeWindow('Configuracion', 400, 600)

cv2.namedWindow('Configuracion2')
cv2.resizeWindow('Configuracion2', 400, 600)

# trackebacker
# Color 1
cv2.createTrackbar('H min', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('H max', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('S min', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('S max', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('V min', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('V max', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('Radio', 'Configuracion', 0, 100, nothing)

# Color 2
cv2.createTrackbar('H min 2', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('H max 2', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('S min 2', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('S max 2', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('V min 2', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('V max 2', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('Radio 2', 'Configuracion', 0, 100, nothing)

# Color 3
cv2.createTrackbar('H min 3', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('H max 3', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('S min 3', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('S max 3', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('V min 3', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('V max 3', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('Radio 3', 'Configuracion2', 0, 100, nothing)

# Color 4
cv2.createTrackbar('H min 4', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('H max 4', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('S min 4', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('S max 4', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('V min 4', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('V max 4', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('Radio 4', 'Configuracion2', 0, 100, nothing)

cv2.namedWindow('Configuracion3')
cv2.resizeWindow('Configuracion3', 300, 300)
cv2.createTrackbar('H min 5', 'Configuracion3', 0, 256, nothing)
cv2.createTrackbar('H max 5', 'Configuracion3', 0, 256, nothing)
cv2.createTrackbar('S min 5', 'Configuracion3', 0, 256, nothing)
cv2.createTrackbar('S max 5', 'Configuracion3', 0, 256, nothing)
cv2.createTrackbar('V min 5', 'Configuracion3', 0, 256, nothing)
cv2.createTrackbar('V max 5', 'Configuracion3', 0, 256, nothing)
cv2.createTrackbar('Radio 5', 'Configuracion3', 0, 100, nothing)

for file_ in os.listdir():
    if file_.endswith(".benja"):
        respuesta = (input('Hay datos disponibles para ser cargados, Y/N: ')).strip()
        if respuesta == 'Y':
            with open("Dat.benja", 'rb') as file:
                Hmin, Hmax, Smin, Smax, Vmin, Vmax, Radio, Hmin2, Hmax2, Smin2, Smax2, Vmin2, \
                Vmax2, Radio2, Hmin3, Hmax3, Smin3, Smax3, Vmin3, Vmax3, Radio3, Hmin4, Hmax4, Smin4, Smax4, Vmin4, \
                Vmax4, Radio4, Hmin5, Hmax5, Smin5, Smax5, Vmin5, Vmax5, Radio5, area1, area2, centro, arco, \
                arcoenemigo, cancha = pickle.load(file)

            cv2.setTrackbarPos('H min', 'Configuracion', Hmin)
            cv2.setTrackbarPos('H max', 'Configuracion', Hmax)
            cv2.setTrackbarPos('S min', 'Configuracion', Smin)
            cv2.setTrackbarPos('S max', 'Configuracion', Smax)
            cv2.setTrackbarPos('V min', 'Configuracion', Vmin)
            cv2.setTrackbarPos('V max', 'Configuracion', Vmax)
            cv2.setTrackbarPos('Radio', 'Configuracion', Radio)

            cv2.setTrackbarPos('H min 2', 'Configuracion', Hmin2)
            cv2.setTrackbarPos('H max 2', 'Configuracion', Hmax2)
            cv2.setTrackbarPos('S min 2', 'Configuracion', Smin2)
            cv2.setTrackbarPos('S max 2', 'Configuracion', Smax2)
            cv2.setTrackbarPos('V min 2', 'Configuracion', Vmin2)
            cv2.setTrackbarPos('V max 2', 'Configuracion', Vmax2)
            cv2.setTrackbarPos('Radio 2', 'Configuracion', Radio2)

            cv2.setTrackbarPos('H min 3', 'Configuracion2', Hmin3)
            cv2.setTrackbarPos('H max 3', 'Configuracion2', Hmax3)
            cv2.setTrackbarPos('S min 3', 'Configuracion2', Smin3)
            cv2.setTrackbarPos('S max 3', 'Configuracion2', Smax3)
            cv2.setTrackbarPos('V min 3', 'Configuracion2', Vmin3)
            cv2.setTrackbarPos('V max 3', 'Configuracion2', Vmax3)
            cv2.setTrackbarPos('Radio 3', 'Configuracion2', Radio3)

            cv2.setTrackbarPos('H min 4', 'Configuracion2', Hmin4)
            cv2.setTrackbarPos('H max 4', 'Configuracion2', Hmax4)
            cv2.setTrackbarPos('S min 4', 'Configuracion2', Smin4)
            cv2.setTrackbarPos('S max 4', 'Configuracion2', Smax4)
            cv2.setTrackbarPos('V min 4', 'Configuracion2', Vmin4)
            cv2.setTrackbarPos('V max 4', 'Configuracion2', Vmax4)
            cv2.setTrackbarPos('Radio 4', 'Configuracion2', Radio4)

            cv2.setTrackbarPos('H min 5', 'Configuracion3', Hmin5)
            cv2.setTrackbarPos('H max 5', 'Configuracion3', Hmax5)
            cv2.setTrackbarPos('S min 5', 'Configuracion3', Smin5)
            cv2.setTrackbarPos('S max 5', 'Configuracion3', Smax5)
            cv2.setTrackbarPos('V min 5', 'Configuracion3', Vmin5)
            cv2.setTrackbarPos('V max 5', 'Configuracion3', Vmax5)
            cv2.setTrackbarPos('Radio 5', 'Configuracion3', Radio5)
            print('Datos Cargados')

# Blucle lector frames

refPt = []


def click(event, x, y, flags, param):
    global refPt

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt.append((x, y))
        print(refPt)
    elif event == cv2.EVENT_RBUTTONDOWN:
        refPt = []


while True:
    ret, frame = cap.read()
    # frame = cv2.blur(frame, (10, 10))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convertimos imagen a HSV
    hsv2 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convertimos imagen a HSV
    hsv3 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convertimos imagen a HSV
    hsv4 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convertimos imagen a HSV
    hsv5 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convertimos imagen a HSV

    # Asignamos las variables del rango de color que seguiremos
    Hmin = cv2.getTrackbarPos('H min', 'Configuracion')
    Hmax = cv2.getTrackbarPos('H max', 'Configuracion')
    Smin = cv2.getTrackbarPos('S min', 'Configuracion')
    Smax = cv2.getTrackbarPos('S max', 'Configuracion')
    Vmin = cv2.getTrackbarPos('V min', 'Configuracion')
    Vmax = cv2.getTrackbarPos('V max', 'Configuracion')
    Radio = cv2.getTrackbarPos('Radio', 'Configuracion')
    # 2

    Hmin2 = cv2.getTrackbarPos('H min 2', 'Configuracion')
    Hmax2 = cv2.getTrackbarPos('H max 2', 'Configuracion')
    Smin2 = cv2.getTrackbarPos('S min 2', 'Configuracion')
    Smax2 = cv2.getTrackbarPos('S max 2', 'Configuracion')
    Vmin2 = cv2.getTrackbarPos('V min 2', 'Configuracion')
    Vmax2 = cv2.getTrackbarPos('V max 2', 'Configuracion')
    Radio2 = cv2.getTrackbarPos('Radio 2', 'Configuracion')
    # 3
    Hmin3 = cv2.getTrackbarPos('H min 3', 'Configuracion2')
    Hmax3 = cv2.getTrackbarPos('H max 3', 'Configuracion2')
    Smin3 = cv2.getTrackbarPos('S min 3', 'Configuracion2')
    Smax3 = cv2.getTrackbarPos('S max 3', 'Configuracion2')
    Vmin3 = cv2.getTrackbarPos('V min 3', 'Configuracion2')
    Vmax3 = cv2.getTrackbarPos('V max 3', 'Configuracion2')
    Radio3 = cv2.getTrackbarPos('Radio 3', 'Configuracion2')
    # 4
    Hmin4 = cv2.getTrackbarPos('H min 4', 'Configuracion2')
    Hmax4 = cv2.getTrackbarPos('H max 4', 'Configuracion2')
    Smin4 = cv2.getTrackbarPos('S min 4', 'Configuracion2')
    Smax4 = cv2.getTrackbarPos('S max 4', 'Configuracion2')
    Vmin4 = cv2.getTrackbarPos('V min 4', 'Configuracion2')
    Vmax4 = cv2.getTrackbarPos('V max 4', 'Configuracion2')
    Radio4 = cv2.getTrackbarPos('Radio 4', 'Configuracion2')  # subimage

    Hmin5 = cv2.getTrackbarPos('H min 5', 'Configuracion3')
    Hmax5 = cv2.getTrackbarPos('H max 5', 'Configuracion3')
    Smin5 = cv2.getTrackbarPos('S min 5', 'Configuracion3')
    Smax5 = cv2.getTrackbarPos('S max 5', 'Configuracion3')
    Vmin5 = cv2.getTrackbarPos('V min 5', 'Configuracion3')
    Vmax5 = cv2.getTrackbarPos('V max 5', 'Configuracion3')
    Radio5 = cv2.getTrackbarPos('Radio 5', 'Configuracion3')

    # Aqui mostramos la imagen en blanco o negro segun el rango de colores.
    bn_img = cv2.inRange(hsv, np.array((Hmin, Smin, Vmin)), np.array((Hmax, Vmax, Smax)))
    bn_img2 = cv2.inRange(hsv2, np.array((Hmin2, Smin2, Vmin2)), np.array((Hmax2, Vmax2, Smax2)))
    bn_img3 = cv2.inRange(hsv3, np.array((Hmin3, Smin3, Vmin3)), np.array((Hmax3, Vmax3, Smax3)))
    bn_img4 = cv2.inRange(hsv4, np.array((Hmin4, Smin4, Vmin4)), np.array((Hmax4, Vmax4, Smax4)))
    bn_img5 = cv2.inRange(hsv5, np.array((Hmin5, Smin5, Vmin5)), np.array((Hmax5, Vmax5, Smax5)))

    # Limpiamos la imagen de imperfecciones con los filtros erode y dilate
    bn_img = cv2.erode(bn_img, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)), iterations=1)
    bn_img = cv2.dilate(bn_img, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)), iterations=1)

    bn_img2 = cv2.erode(bn_img2, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)), iterations=1)
    bn_img2 = cv2.dilate(bn_img2, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)), iterations=1)

    bn_img3 = cv2.erode(bn_img3, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)), iterations=1)
    bn_img3 = cv2.dilate(bn_img3, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)), iterations=1)

    bn_img4 = cv2.erode(bn_img4, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)), iterations=1)
    bn_img4 = cv2.dilate(bn_img4, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)), iterations=1)

    bn_img5 = cv2.erode(bn_img5, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)), iterations=1)
    bn_img5 = cv2.dilate(bn_img5, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)), iterations=1)

    # Centro de masa
    M = cv2.moments(bn_img)
    if M['m00'] > 50000:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        # Cìrculo en el centro de masa con radio variable
        cv2.circle(frame, (cx, cy), Radio, (0, 255, 0), 2)

    M2 = cv2.moments(bn_img2)
    if M2['m00'] > 20000:
        cx2 = int(M2['m10'] / M2['m00'])
        cy2 = int(M2['m01'] / M2['m00'])
        cv2.circle(frame, (cx2, cy2), Radio2, (0, 0, 255), 2)
    '''
    if M['m00'] > 50000 and M2['m00'] > 20000:
        a = math.radians(Automata.angulo(cx, cy, cx2, cy2))
        dis = 30
        cv2.circle(frame, (int(cx2 + math.cos(a) * dis), int(cy2 + math.sin(a) * dis)), 15, (255, 255, 255), 2)
    '''
    M3 = cv2.moments(bn_img3, 0)
    if M3['m00'] > 25000:
        cx3 = (np.uint32)(M3['m10'] / M3['m00'])  # int(M3['m10'] / M3['m00'])
        cy3 = (np.uint32)(M3['m01'] / M3['m00'])  # int(M3['m01'] / M3['m00'])
        cv2.circle(frame, (cx3, cy3), Radio3, (0, 0, 255), 2)

    M4 = cv2.moments(bn_img4)
    if M4['m00'] > 50000:
        cx4 = int(M4['m10'] / M4['m00'])
        cy4 = int(M4['m01'] / M4['m00'])
        cv2.circle(frame, (cx4, cy4), Radio4, (0, 0, 255), 2)

    M5 = cv2.moments(bn_img5)
    if M5['m00'] > 20000:
        cx5 = int(M5['m10'] / M5['m00'])
        cy5 = int(M5['m01'] / M5['m00'])
        cv2.circle(frame, (cx5, cy5), Radio5, (0, 0, 255), 2)



    if M['m00'] > 50000 and M2['m00'] > 20000:
        a = math.radians(Automata.angulo(cx,cy,cx2,cy2))
        dis = 30
        pointx = cx2 + math.cos(a) * dis
        pointy = cy2 - math.sin(a) * dis
        cv2.circle(frame, (int(pointx), int(pointy)), 15, (255,255,255),2)

    if M4['m00'] > 50000 and M5['m00'] > 20000:
        a = math.radians(Automata.angulo(cx4,cy4,cx5,cy5))
        dis = 30
        pointx5 = cx5 + math.cos(a) * dis
        pointy5 = cy5 - math.sin(a) * dis
        cv2.circle(frame, (int(pointx5), int(pointy5)), 15, (255,255,255),2)

    if 'arco' in globals():
        cv2.line(frame, arco[0], arco[1], (0, 255, 0), 3)
    if 'arcoenemigo' in globals():
        cv2.line(frame, arcoenemigo[0], arcoenemigo[1], (0, 255, 0), 3)
    if 'centro' in globals():
        cv2.circle(frame, centro[0], 5, (255, 0, 0), 2)

    if 'cancha' in globals():
        cv2.line(frame, cancha[0], cancha[1], (255, 255, 255), 3)
        cv2.line(frame, cancha[1], cancha[2], (255, 255, 255), 3)
        cv2.line(frame, cancha[2], cancha[3], (255, 255, 255), 3)
        cv2.line(frame, cancha[3], cancha[0], (255, 255, 255), 3)

    if 'area1' in globals():
        cv2.rectangle(frame, area1[0], area1[1], (255, 255, 255), 3)
    if 'area2' in globals():
        cv2.rectangle(frame, area2[0], area2[1], (255, 255, 255), 3)
    try:
        aex = (arcoenemigo[0][0] + arcoenemigo[1][0]) / 2
        aey = (arcoenemigo[0][1] + arcoenemigo[1][1]) / 2
        a = math.radians(Automata.angulo(cx3, cy3, aex, aey))
        dist1 = 80
        dist2 = 80
        if cy3 <= 250:
            puntoairx = cx3 - math.cos(a) * dist1
            puntoairy = cy3 + math.sin(a) * dist1
            cv2.circle(frame, (int(puntoairx), int(puntoairy)), 3, (255, 255, 0), 2)
            cv2.line(frame, (cx3, cy3), (int(aex), int(aey)), (255, 255, 255), 1)
            puntoairx2 = cx3 + math.cos(a - math.radians(90)) * dist2
            puntoairy2 = cy3 - math.sin(a - math.radians(90)) * dist2
            cv2.circle(frame, (int(puntoairx2), int(puntoairy2)), 3, (255, 255, 255), 2)

        else:
            puntoairx = cx3 - math.cos(a) * dist1
            puntoairy = cy3 + math.sin(a) * dist1
            cv2.circle(frame, (int(puntoairx), int(puntoairy)), 3, (255, 255, 0), 2)
            cv2.line(frame, (cx3, cy3), (int(aex), int(aey)), (255, 255, 255), 1)
            puntoairx2 = cx3 + math.cos(a + math.radians(90)) * dist2
            puntoairy2 = cy3 - math.sin(a + math.radians(90)) * dist2
            cv2.circle(frame, (int(puntoairx2), int(puntoairy2)), 3, (255, 255, 255), 2)
    except:
        pass

    h = 0
    try:
        coordenadas = cx, cy, cx2, cy2, cx3, cy3 , cx4, cy4, cx5, cy5
        h = 1

    except:
        pass
    #labestia.comunicacion.CONNECTED is True
    if h == 1:
        enemigo.actualizar(cx4, cy4, cx5, cy5, cx3, cy3)
        labestia.actualizar(cx, cy, cx2, cy2, cx3, cy3)

    # Creamos las ventanas de salida y configuracion
    cv2.imshow('Salida', frame)

    cv2.imshow('inRange', bn_img)
    # cv2.namedWindow('inRange')
    # cv2.resizeWindow('inRange', 300, 600)

    cv2.imshow('inRange2', bn_img2)
    # cv2.namedWindow('inRange2')
    # cv2.resizeWindow('inRange2', 300, 600)

    cv2.imshow('inRange3', bn_img3)
    # cv2.namedWindow('inRange3')
    # cv2.resizeWindow('inRange3', 300, 600)

    cv2.imshow('inRange4', bn_img4)
    # cv2.namedWindow('inRange4')
    # cv2.resizeWindow('inRange4', 300, 600)

    cv2.imshow('inRange5', bn_img5)
    # cv2.namedWindow('inRange5')
    # cv2.resizeWindow('inRange5', 300, 600)

    if cv2.waitKey(20) & 0xFF == ord("w"):

        print("apreta una tecla qlo, tienes 5 segundos")

        tecla = cv2.waitKey(5000)

        if tecla & 0xFF == ord("e"):
            print("marque puntos")
            cv2.setMouseCallback("Salida", click)

        elif tecla & 0xFF == ord("t"):
            x = refPt[1][0] - refPt[0][0]
            y = refPt[1][1] - refPt[0][1]

            anng = math.degrees(math.atan(y - x))
            print(anng)

        elif tecla & 0xFF == ord("a"):
            global arco
            arco = refPt
            print("arco definido como: {}".format(arco))

        elif tecla & 0xFF == ord("o"):
            global arcoenemigo
            arcoenemigo = refPt
            print("arco enemigo definido como {}:".format(arcoenemigo))

        elif tecla & 0xFF == ord("g"):
            global centro
            centro = refPt
            print("centro definido como {}:".format(centro))
            print(centro)

        elif tecla & 0xFF == ord("h"):
            global cancha
            cancha = refPt
            print("cancha definida como {}:".format(cancha))

        elif tecla & 0xFF == ord("j"):
            global area1
            area1 = refPt
            print("area defensiva definida como {}:".format(area1))
            print(area1)

        elif tecla & 0xFF == ord("k"):
            global area2
            area2 = refPt
            print("area enemiga definida como {}:".format(area2))

        elif tecla & 0xFF == ord("p"):
            print("arco definido como: {}".format(arco))
            print("arco enemigo definido como: {}".format(arcoenemigo))
            print("centro definido como: {}".format(centro))

        elif tecla & 0xFF == ord("y"):
            cv2.circle(frame, (100, 100), 50, (0, 0, 255), 2)

        ##################
        '''
        if tecla & 0xFF == ord('c'):  # Se conecta al robot con c
            labestia.conectar()
            if labestia.CONNECTED:
                print('Conectado!')'''

        if tecla & 0xFF == ord('l'):  # Se conecta al robot con c
            labestia.pausa = False

        if tecla & 0xFF == ord('q'):  # Se cierra con Q
            break

        if tecla & 0xFF == ord('s'):  # Se guarda con s
            data = Hmin, Hmax, Smin, Smax, Vmin, Vmax, Radio, Hmin2, Hmax2, Smin2, Smax2, Vmin2, \
                   Vmax2, Radio2, Hmin3, Hmax3, Smin3, Smax3, Vmin3, Vmax3, Radio3, Hmin4, Hmax4, Smin4, Smax4, Vmin4, \
                   Vmax4, Radio4, Hmin5, Hmax5, Smin5, Smax5, Vmin5, Vmax5, Radio5, area1, area2, centro, arco, arcoenemigo, cancha
            with open("Dat.benja", 'wb') as file:
                pickle.dump(data, file)
            print('Datos Guardados')

        if tecla & 0xFF == ord('O'):
            labestia.set_inicio(arco, arcoenemigo)
            print('arcos dados')

        if tecla & 0xFF == ord('i'):
            print('Partimo')
            labestia.Pausa()
            enemigo.Pausa()

        if tecla & 0xFF == ord('b'):  # Pide un input
            final = input('A donde voy?: ').strip()

cap.release()
cv2.destroyAllWindows()
