import cv2
import numpy as np 
image=cv2.imread('2bit2.png')
cv2.waitKey()
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edged=cv2.Canny(gray,30,200)
cv2.waitKey(0)

#Finding Contours 
contours,hierarchy=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.imshow('canny Edges contouring',edged)
cv2.waitKey()
print("Number of Contours found="+str(len(contours)))
cv2.drawContours(image,contours,-1,(0,255,0),3)
cv2.imshow('Contours',image)
cv2.waitKey()
cv2.destroyAllWindows()