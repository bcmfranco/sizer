#Prender virtualenv
## tirar en el directorio root: source env/bin/activate
##Apagar virtualenv
## entrar en env/bin y mandar: deactivate

import cv2
import numpy as np
import matplotlib as plt

print("sizer running")

#Declaro las cámaras
native_camera = 1
usb_camera = 0

#Declaro la captura de imagen
cap = cv2.VideoCapture(usb_camera)

while(True):
    _, frame = cap.read()
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([38, 86, 0])
    upper_blue = np.array([121, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    contours,hierachy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # print(contours)

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 1000:
            cv2.drawContours(frame, contour, -1, (0, 0, 255), 3)

    cv2.imshow('frame',frame)
    # cv2.imshow('mask', mask)

    #Cerrar la cámara
    if cv2.waitKey(1000) & 0xFF == ord('q'): #La q produce un escape
        break
        
cap.release()
cv2.destroyAllWindows()

