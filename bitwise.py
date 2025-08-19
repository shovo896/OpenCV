import cv2
import numpy as np
img1=cv2.imread('1bit1.png')
img2=cv2.imread('2bit2.png')
dest_or = cv2.bitwise_and(img2,img1,mask=None)
cv2.imshow('Bitwise And',dest_or)
if cv2.waitKey(0) & 0xff==27:
    cv2.destroyAllWindows()