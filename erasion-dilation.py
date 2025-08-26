import cv2 
import numpy as np
image=cv2.imread('gamma_transformed0.5.jpg',0)
kernel=np.ones((5,5),np.uint8)
erosion=cv2.erode(image,kernel,iterations=1)
dilation=cv2.dilate(image,kernel,iterations=1)
cv2.imshow("Orginal",image)
cv2.imshow("Erosion",image)
cv2.imshow("Dilation",image)
cv2.waitKey(0)
cv2.destroyAllWindows()