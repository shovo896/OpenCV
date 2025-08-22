import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
image=cv2.imread('img_5terre.jpg')
image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
kernel=np.ones((3,3),np.uint8)
dilated=cv2.dilate(image_gray,kernel,iterations=2)
eroded=cv2.erode(image_gray,kernel,iterations=2)
opening=cv2.morphologyEx(image_gray,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(image_gray,cv2.MORPH_CLOSE,kernel)
fig,axs=plt.subplots(2,2,figsize=(7,7))
axs[0,0].imshow(dilated,camp='Greys'),axs[0,0].set_title('Dilated Image')
axs[0,1].imshow(eroded,camp='Greys'),axs[0,1].set_title('eroded Image')
axs[1,0].imshow(opening,camp='Greys'),axs[0,0].set_title('Opening Image')

axs[1,1].imshow(closing,camp='Greys'),axs[1,1].set_title('closing Image')
for ax in axs.flatten():
    ax.set_xticks([]),ax.set_ticks([])
plt.tight_layout()
plt.show()

