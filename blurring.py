import cv2 
from matplotlib import pyplot as plt 
image_path = '1bit1.png'
image=cv2.imread(image_path)
resized_image=cv2.resize(image,(1900,800))
resized_image_rgb=cv2.cvtColor(resized_image,cv2.COLOR_BGR2RGB)
plt.imshow(resized_image_rgb)
plt.title('Orginal Image')
plt.axis('Off')
plt.show()

