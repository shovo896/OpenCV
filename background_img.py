import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load image
image = cv2.imread('img_5terre.jpg')
if image is None:
    raise FileNotFoundError("Image not found. Check path!")

# Create mask initialized to "probable background"
mask = np.zeros(image.shape[:2], np.uint8)

# Mark some foreground and background manually
# Example: Draw a rectangle in the center as foreground
mask[120:250, 100:300] = 1   # sure foreground (white area inside object)
mask[0:50, 0:50] = 0         # sure background (top-left corner as background)

# Models required by GrabCut (do not touch)
backgroundModel = np.zeros((1, 65), np.float64)
foregroundModel = np.zeros((1, 65), np.float64)

# Run GrabCut with mask
cv2.grabCut(image, mask, None, backgroundModel, foregroundModel, 5, cv2.GC_INIT_WITH_MASK)

# Convert mask into binary segmentation (0 = background, 1 = foreground)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
image_segmented = image * mask2[:, :, np.newaxis]

# Show results
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Segmented Image (Mask Method)")
plt.imshow(cv2.cvtColor(image_segmented, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.show()
