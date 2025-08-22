import cv2 
from matplotlib import pyplot as plt 
image_path = '1bit1.png'
image=cv2.imread(image_path)
resized_image=cv2.resize(image,(1900,800))
resized_image_rgb=cv2.cvtColor(resized_image,cv2.COLOR_BGR2RGB)

Gaussian=cv2.GaussianBlur(resized_image,(15,15),0)
Gaussian_rgb=cv2.cvtColor(Gaussian,cv2.COLOR_BGR2RGB)
plt.imshow(Gaussian_rgb)
plt.axis('off')
plt.show()
