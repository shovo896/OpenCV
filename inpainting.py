import cv2 
import numpy as np

damaged_img=cv2.imread('img_5terre.jpg',0)
height,width=damaged_img.shape[0],damaged_img.shape[1]

for i in range(height) :
    for j in range(width):
        if damaged_img[i,j].sum() > 0 :
            damaged_img[i,j]=0 
        else:
            damaged_img[i,j]=[255,255,255]
mask=damaged_img
cv2.imwrite('mask.jpg',mask)