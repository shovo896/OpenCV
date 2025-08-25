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
#define paramenters 
r1=70;
s1=0;
r2=140;
s2=255;
pixelVal_vec=np.vectorize(pixelVal)
contrast_stretched=pixelVal_vec(img,r1,r2,s1,s2)
cv2.imwrite('Cotrast_stretch.jpg',contrast_stretched)
   