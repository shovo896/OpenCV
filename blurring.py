import cv2 
from matplotlib import pyplot as plt 
image_path = 'img_5terre.jpg'
image=cv2.imread(image_path)
resized_image=cv2.resize(image,(1900,800))
resized_image_rgb=cv2.cvtColor(resized_image,cv2.COLOR_BGR2RGB)
median=cv2.medianBlur(resized_image,11)
median_rgb=cv2.cvtColor(median,cv2.COLOR_BGR2RGB)
plt.imshow(median_rgb)
plt.axis('Off')
plt.show()

