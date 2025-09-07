import cv2 
import numpy as np

image=cv2.imread('contrast_stretch.jpg')
params=cv2.SimpleBlobDetector_params()
params.filterByArea=True
params.minArea=100 

params.filterByCircularuity=True 
params.minCircularity=0.8

params.filterByConvexity=True
params.minConvexity=0.2