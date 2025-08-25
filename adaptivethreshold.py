import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
image = cv2.imread('gamma_transformed0.1.jpg')
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
def show_image(img,title):
    plt.imshow(img,gray_image)
    plt.title(title)
    plt.axis('off')
    plt.show()
show_image(gray_image,"Orginal Grayscale Image")

thresh_mean=cv2.adaptiveThreshold(
    gray_image,255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    199,5
)
show_image(thresh_mean,"Adaptive mean Thresholding ")
thresh_gauss=cv2.adaptiveThreshold(
    gray_image,255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    199,5

)
show_image(thresh_gauss,"Adaptive Gaussian Thresholding ")