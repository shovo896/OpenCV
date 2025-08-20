import numpy as np
import cv2 
img=np.zeros((400,400,3),dtype="uint8")
cv2.rectangle(img,(30,30),(300,200),(0,255,0),5)
cv2.imshow('dark',img)
cv2.waitKey()
cv2.destroyAllWindows()