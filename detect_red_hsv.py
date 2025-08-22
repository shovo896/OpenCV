import cv2 
import numpy as np

# Read image
image = cv2.imread('1bit1.png')

# Convert BGR to HSV
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define range for red color
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

# Create mask
mask = cv2.inRange(image_hsv, lower_red, upper_red)

# Apply mask
result = cv2.bitwise_and(image, image, mask=mask)

# Show results
cv2.imshow("Original", image)
cv2.imshow("Mask", mask)
cv2.imshow("Detected Red", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
