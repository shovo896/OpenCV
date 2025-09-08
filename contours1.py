import numpy as np
import cv2
font=cv2.FONT_HERSELY_COMPLEX

img2=cv2.imread('contrast_stretch.jpg',cv2.IMREAD_COLOR)
img=cv2.imread('DSC07229.JPG',cv2.IMREAD_GRAYSCALE)
_,threshold=cv2.threshold(img,110,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APROX_SIMPLE)

for cnt in contours:
    approx=cv2.approxpolyDP(cnt,0.09*cv2.arcLength(cnt,True),True)
    cv2.drawContours(img2,[approx],0,(0,0,255),5)
    n=approx.ravel()
    i=0
    for j in n :
        if i%2==0:
            x,y=n[i],n[i+1]
            coord=f"{x} {y}"
            if i%2==0:
                cv2.putText(img2,coord,(x,y),font,0.5,(0,255,0))
            else:
                cv2.putText(img2,coord,(x,y),font,(0,255,0))
        else:
            cv2.putText(img2,coord,(x,y),font,0.5,(0,255,0))
        i+=1
cv2.imshow('contours',img2)

if cv2.waitKey(0) & 0xFF==27:
    cv2.destroyAllWindows()

