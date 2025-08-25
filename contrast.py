import cv2 
import numpy as np 

def pixelVal(pix,r1,s1,r2,s2):
    if(0 <= pix and pix <=r1):
        return (s1/r1)*pix 
    elif (r1 < pix and pix <= r2):
        return ((s2-s1)/(r2-r1)*(pix-r1)+s1)
    else:
        return ((255-s2)/(255-r2))*(pix-r2)+s2
    img=cv2.imread('gamma_transformed0.1.jpg')
   