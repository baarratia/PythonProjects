__author__ = 'Marcelo'
# -*- encoding: utf-8 -*-
import cv2
import numpy as np
from Comunicador import Comunicador_Robot
import Automata
import pickle
import os
# camara 0 notebook
# camara 1 lab
CAM = 0


def nothing(x):
    pass
'''
for file_ in os.listdir():
    if file_.endswith(".benja"):
        respuesta = (input('Hay datos disponibles para ser cargados, Y/N: ')).strip()
        if respuesta == 'Y':
            with open("Dat.benja", 'rb') as file:
                DESC, km, listaPaths, listaimgs = pickle.load(file)
        else:
            n = int(input('Ingrese un 1 o 2, dependiendo del ejemplo a correr: '))
            DESC, km, listaPaths, listaimgs  = Recorrer(n)
            datos = DESC, km, listaPaths, listaimgs
            print("Size of descriptor matrix:", DESC.shape)
            with open("Dat.benja", 'wb') as file:
                 pickle.dump(datos, file)'''

cap = cv2.VideoCapture(CAM)
cv2.namedWindow('Configuracion')
cv2.resizeWindow('Configuracion', 300, 600)

cv2.namedWindow('Configuracion2')
cv2.resizeWindow('Configuracion2', 300, 600)


# trackebacker
#Color 1
cv2.createTrackbar('H min', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('H max', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('S min', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('S max', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('V min', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('V max', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('Radio', 'Configuracion', 0, 100, nothing)

#Color 2
cv2.createTrackbar('H min 2', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('H max 2', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('S min 2', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('S max 2', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('V min 2', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('V max 2', 'Configuracion', 0, 256, nothing)
cv2.createTrackbar('Radio 2', 'Configuracion', 0, 100, nothing)

#Color 3
cv2.createTrackbar('H min 3', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('H max 3', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('S min 3', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('S max 3', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('V min 3', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('V max 3', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('Radio 3', 'Configuracion2', 0, 100, nothing)

#Color 4
cv2.createTrackbar('H min 4', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('H max 4', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('S min 4', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('S max 4', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('V min 4', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('V max 4', 'Configuracion2', 0, 256, nothing)
cv2.createTrackbar('Radio 4', 'Configuracion2', 0, 100, nothing)

emparejado = False
# Blucle lector frames
while True:
    ret, frame = cap.read()
    frame = cv2.blur(frame, (10, 10))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convertimos imagen a HSV
    hsv2 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convertimos imagen a HSV
    hsv3 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convertimos imagen a HSV
    hsv4 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convertimos imagen a HSV

    # Asignamos las variables del rango de color que seguiremos
    Hmin = cv2.getTrackbarPos('H min', 'Configuracion')
    Hmax = cv2.getTrackbarPos('H max', 'Configuracion')
    Smin = cv2.getTrackbarPos('S min', 'Configuracion')
    Smax = cv2.getTrackbarPos('S max', 'Configuracion')
    Vmin = cv2.getTrackbarPos('V min', 'Configuracion')
    Vmax = cv2.getTrackbarPos('V max', 'Configuracion')
    Radio = cv2.getTrackbarPos('Radio', 'Configuracion')
    #2
    Hmin2 = cv2.getTrackbarPos('H min 2', 'Configuracion')
    Hmax2 = cv2.getTrackbarPos('H max 2', 'Configuracion')
    Smin2 = cv2.getTrackbarPos('S min 2', 'Configuracion')
    Smax2 = cv2.getTrackbarPos('S max 2', 'Configuracion')
    Vmin2 = cv2.getTrackbarPos('V min 2', 'Configuracion')
    Vmax2 = cv2.getTrackbarPos('V max 2', 'Configuracion')
    Radio2 = cv2.getTrackbarPos('Radio 2', 'Configuracion')
    #3
    Hmin3 = cv2.getTrackbarPos('H min 3', 'Configuracion2')
    Hmax3 = cv2.getTrackbarPos('H max 3', 'Configuracion2')
    Smin3 = cv2.getTrackbarPos('S min 3', 'Configuracion2')
    Smax3 = cv2.getTrackbarPos('S max 3', 'Configuracion2')
    Vmin3 = cv2.getTrackbarPos('V min 3', 'Configuracion2')
    Vmax3 = cv2.getTrackbarPos('V max 3', 'Configuracion2')
    Radio3 = cv2.getTrackbarPos('Radio 3', 'Configuracion2')
    #4
    Hmin4 = cv2.getTrackbarPos('H min 4', 'Configuracion2')
    Hmax4 = cv2.getTrackbarPos('H max 4', 'Configuracion2')
    Smin4 = cv2.getTrackbarPos('S min 4', 'Configuracion2')
    Smax4 = cv2.getTrackbarPos('S max 4', 'Configuracion2')
    Vmin4 = cv2.getTrackbarPos('V min 4', 'Configuracion2')
    Vmax4 = cv2.getTrackbarPos('V max 4', 'Configuracion2')
    Radio4 = cv2.getTrackbarPos('Radio 4', 'Configuracion2')

    # Aqui mostramos la imagen en blanco o negro segun el rango de colores.
    bn_img = cv2.inRange(hsv, np.array((Hmin, Smin, Vmin)), np.array((Hmax, Vmax, Smax)))
    bn_img2 = cv2.inRange(hsv2, np.array((Hmin2, Smin2, Vmin2)), np.array((Hmax2, Vmax2, Smax2)))
    bn_img3 = cv2.inRange(hsv3, np.array((Hmin3, Smin3, Vmin3)), np.array((Hmax3, Vmax3, Smax3)))
    bn_img4 = cv2.inRange(hsv4, np.array((Hmin4, Smin4, Vmin4)), np.array((Hmax4, Vmax4, Smax4)))


    # Limpiamos la imagen de imperfecciones con los filtros erode y dilate
    bn_img = cv2.erode(bn_img, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)), iterations=1)
    bn_img = cv2.dilate(bn_img, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)), iterations=1)

    bn_img2 = cv2.erode(bn_img2, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)), iterations=1)
    bn_img2 = cv2.dilate(bn_img2, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)), iterations=1)

    bn_img3 = cv2.erode(bn_img3, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)), iterations=1)
    bn_img3 = cv2.dilate(bn_img3, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)), iterations=1)

    bn_img4 = cv2.erode(bn_img4, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)), iterations=1)
    bn_img4 = cv2.dilate(bn_img4, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)), iterations=1)

    # Centro de masa
    M = cv2.moments(bn_img)
    if M['m00'] > 50000:
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        # Cìrculo en el centro de masa con radio variable
        cv2.circle(frame, (cx, cy), Radio, (0, 255, 0), 2)

    M2 = cv2.moments(bn_img2)
    if M2['m00'] > 50000:
        cx2 = int(M2['m10'] / M2['m00'])
        cy2 = int(M2['m01'] / M2['m00'])
        cv2.circle(frame, (cx2, cy2), Radio2, (0, 0, 255), 2)

    M3 = cv2.moments(bn_img3)
    if M3['m00'] > 50000:
        cx3 = int(M3['m10'] / M3['m00'])
        cy3 = int(M3['m01'] / M3['m00'])
        cv2.circle(frame, (cx3, cy3), Radio3, (0, 0, 255), 2)

    M4 = cv2.moments(bn_img4)
    if M4['m00'] > 50000:
        cx4 = int(M4['m10'] / M4['m00'])
        cy4 = int(M4['m01'] / M4['m00'])
        cv2.circle(frame, (cx4, cy4), Radio4, (0, 0, 255), 2)
    h = 0
    try:
        print('cx = {}, cy = {}'.format(cx,cy))
    except:
        pass
    try:
        print('cx2 = {}, cy2 = {}'.format(cx2,cy2))
    except:
        pass
    try:
        print('cx3 = {}, cy3 = {}'.format(cx3,cy3))
    except:
        pass
    try:
        coordenadas = cx,cy, cx2, cy2, cx3, cy3
        h = 1
    except:
        pass

    if emparejado is True and h== 1:
        posiciones = cx,cy, cx2, cy2, cx3, cy3
        data = Automata.seguir(posiciones)
        comunicacion.escuchar_enviar(data)
        print('datos enviados!')
    # Creamos las ventanas de salida y configuracion
    cv2.imshow('Salida', frame)


    cv2.imshow('inRange', bn_img)
    #cv2.namedWindow('inRange')
    #cv2.resizeWindow('inRange', 300, 600)

    cv2.imshow('inRange2', bn_img2)
    #cv2.namedWindow('inRange2')
    #cv2.resizeWindow('inRange2', 300, 600)

    cv2.imshow('inRange3', bn_img3)
    #cv2.namedWindow('inRange3')
    #cv2.resizeWindow('inRange3', 300, 600)

    cv2.imshow('inRange4', bn_img4)
    #cv2.namedWindow('inRange4')
    #cv2.resizeWindow('inRange4', 300, 600)

    if cv2.waitKey(1) & 0xFF == ord('c'):  # Se conecta al robot con c
        comunicacion = Comunicador_Robot()
        if comunicacion.CONNECTED and emparejado is False:
            emparejado = True
            print('Conectado!')


    if cv2.waitKey(1) & 0xFF == ord('q'):  # Se cierra con Q
        break

cap.release()
cv2.destroyAllWindows()
