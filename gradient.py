import cv2 
import numpy as np 
screenRead=cv2.VideoCapture(0)
while True :
    _,image=screenRead.read()
    hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    blue1=np.array([110,50,50])
    blue2=np.array([130,255,255])
    mask=cv2.inRange(hsv,blue1,blue2)
    kernel=np.ones((5,5),np.uint8)
    gradient=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel)
    cv2.imshow('Orginal Blue Mask',mask)
    cv2.imshow('after gradient (Edges Highlighted)',gradient)
    if cv2.waitKey(1) & 0xFF== ord('a') :
        break 
cv2.destroyAllWindows()
screenRead.release()