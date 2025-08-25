import cv2
import numpy as np

# Read the image
image = cv2.imread('gamma_transformed1.2.jpg')

# Downsample the image
downsampled_image = cv2.pyrDown(image)

# Show images with window names
cv2.imshow("Original Image", image)
cv2.imshow("Downsampled Image", downsampled_image)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
