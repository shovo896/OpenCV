import cv2
import numpy as np

# Load grayscale image
damaged_img = cv2.imread('img_5terre.jpg', 0)

# Create an empty mask with the same shape
mask = np.zeros_like(damaged_img)

# Threshold: if pixel > 0 → set to 0, else → set to 255
mask[damaged_img > 0] = 0
mask[damaged_img == 0] = 255

# Save the result
cv2.imwrite('mask.jpg', mask)
