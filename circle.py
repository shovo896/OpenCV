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

params.filterByInertia=True
params.minInertiaRatio=0.01

detector=cv2.SimpleBlobDetector_create(params)
keypoints=detector.detect(image)
blank=np.zeros((1,1))
blobs=cv2.drawKeypoints(image,keypoints,blank,(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
number_of_blobs=len(keypoints)