#Prender virtualenv
## tirar en el directorio root: source env/bin/activate
##Apagar virtualenv
## entrar en env/bin y mandar: deactivate

import cv2
import numpy as np

print("sizer running")

#Declaro las cámaras
native_camera = 1
usb_camera = 0

#Declaro la captura de imagen
cap = cv2.VideoCapture(usb_camera)

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): #La q produce un escape
        break

cap.release()
cv2.destroyAllWindows()
