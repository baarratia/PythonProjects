import cv2
import numpy as np

CAM = 0
cap = cv2.VideoCapture(CAM)


refPt = []



def click(event, x, y, flags, param):
    # grab references to the global variables
    global refPt

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt.append((x, y))
        print(refPt)
    elif event == cv2.EVENT_RBUTTONDOWN:
        refPt=[]

def click2(event, x, y, flags, param):
    # grab references to the global variables
    global refPt2

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt2.append((x, y))
        print(refPt2)
    elif event == cv2.EVENT_RBUTTONDOWN:
        refPt2=[]

while True:
    ret, frame = cap.read()
    cv2.imshow('Salida', frame)


    if cv2.waitKey(20) & 0xFF == ord("w"):

        print("apreta una tecla qlo, tienes 5 segundos")

        tecla=cv2.waitKey(5000)

        if tecla & 0xFF == ord("e"):
            print("marque puntos")
            cv2.setMouseCallback("Salida", click)

        elif tecla & 0xFF == ord("a"):
            global arco
            arco=refPt
            print("arco definido como:");print(arco)

        elif tecla & 0xFF == ord("o"):
            global arcoenemigo
            arcoenemigo=refPt
            print("arco enemigo definido como:");print(arcoenemigo)

        elif tecla & 0xFF == ord("c"):
            global centro
            centro=refPt
            print("centro definido como:");print(centro)

        elif tecla & 0xFF == ord("p"):
            print("arco definido como:");print(arco)
            cv2.line(frame, arco[0], arco[1], (255,0,0), 3)
            print("arco enemigo definido como:");print(arcoenemigo)
            cv2.line(frame, arcoenemigo[0], arcoenemigo[1], (255,0,0), 3)
            print("centro definido como:");print(centro)
            cv2.circle(frame, centro[0],5, (0, 0, 255), 2)
        elif tecla & 0xFF == ord("y"):
            cv2.circle(frame, (100,100),50,(0,0,255),2)
        elif tecla & 0xFF == ord("q"):
            break

        cv2.imshow('Salida', frame)

cv2.destroyAllWindows()
