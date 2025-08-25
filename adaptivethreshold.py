import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('gamma_transformed0.1.jpg')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Function to show image
def show_image(img, title):
    plt.imshow(img, cmap='gray')  # Corrected cmap
    plt.title(title)
    plt.axis('off')
    plt.show()

# Show original grayscale image
show_image(gray_image, "Original Grayscale Image")

# Adaptive Mean Thresholding
thresh_mean = cv2.adaptiveThreshold(
    gray_image, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    199, 5
)
show_image(thresh_mean, "Adaptive Mean Thresholding")

# Adaptive Gaussian Thresholding
thresh_gauss = cv2.adaptiveThreshold(
    gray_image, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    199, 5
)
show_image(thresh_gauss, "Adaptive Gaussian Thresholding")
