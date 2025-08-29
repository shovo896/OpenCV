import numpy as np
import cv2 
from matplotlib import pyplot as plt 

image=cv2.imread('img_5terre.jpg')
mask=np.zeros(image.shape[:2],np.uint8)
backgroundModel=np.zeros((1,65),np.float64)
foregroundModrl=np.zeros((1,65),np.float64)

rectangle=(20,100,150,150)
