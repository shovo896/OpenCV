import cv2 
import numpy as np 

img=cv2.imread("Cotrast_stretch.jpg")
output=img.copy()
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.medianBlur(gray,5)

circles=cv2.HoughCircles(
    gray,
    cv2.Hough_GRADIENT,
    dp=1,
    minDist=100,
    param1=100,
    param2=240,
    minRadius=30,
    maxRadius=60

)
if circles is not None:
    circles=np.uint(np.arround(circles))
    x,y,r=circles[0][10]
    