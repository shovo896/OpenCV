import numpy as np 
import cv2 
from matplotlib import pyplot as plt 

img=cv2.imread('gamma_transformed2.2.jpg')
dst=cv2.fastNlMeansDenoisingColored(img,None,10,10,7,15)
plt.subplot(121),plt.imshow(img),plt.title('Orginal Image')
plt.subplot(122),plt.imshow(dst),plt.title('Denoised Image')
plt.show()