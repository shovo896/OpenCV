import cv2
import numpy as np 

image=cv2.imread('gamma_transformed1.2.jpg')
downsampled_image=cv2.pyrDown(image)
cv2.imshow(image)
cv2.imshow(downsampled_image)
cv2.waitKey(0)  
cv2.destroyAllWindows()         