import numpy as np
import cv2

# Correct font
font = cv2.FONT_HERSHEY_COMPLEX

# Read images
img2 = cv2.imread('contrast_stretch.jpg', cv2.IMREAD_COLOR)
img = cv2.imread('DSC07229.JPG', cv2.IMREAD_GRAYSCALE)

# Thresholding
_, threshold = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.09 * cv2.arcLength(cnt, True), True)
    cv2.drawContours(img2, [approx], 0, (0, 0, 255), 5)

    n = approx.ravel()
    for i in range(0, len(n), 2):  # step by 2 (x,y pairs)
        x, y = n[i], n[i+1]
        coord = f"{x} {y}"
        cv2.putText(img2, coord, (x, y), font, 0.5, (0, 255, 0), 1)

# Show result
cv2.imshow('contours', img2)

# Wait for ESC key to close
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
