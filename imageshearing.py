import cv2 
import matplotlib.pyplot as plt 
import numpy as np 
image=cv2.imread('img_5terre.jpg')
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
width,height=image_rgb.shape[1],image_rgb.shape[0]
shearX,shearY=-0.15,0
transformation_matrix=np.array([[[1,shearX,0],[0,1,shearY]]],dtype=np.float32)
sheard_image=cv2.warpAffine(image_rgb,transformation_matrix,(width,height))
fig,axs=plt.subplots(1,2,figsize=(7,4))
axs[0].imshow(image_rgb),axs[0].set_title('Orginal Image')
axs[1].imshow(sheared_image),axs[1].set_title('Sheared Image')
for ax in axs :
    ax.set_xticks([]),ax.set_yticks([])
plt.tight_layout()
plt.show()