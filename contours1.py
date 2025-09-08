import numpy as np
import cv2
font=cv2.FONT_HERSELY_COMPLEX

img2=cv2.imread('contrast_stretch.jpg',cv2.IMREAD_COLOR)
img=cv2.imread('DSC07229.JPG',cv2.IMREAD_GRAYSCALE)
_,threshold=cv2.threshold(img,110,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APROX_SIMPLE)

for cnt in contours:
    approx=cv2.approxpolyDP(cnt,0.09*cv2.arcLength(cnt,True),True)
