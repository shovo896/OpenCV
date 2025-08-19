import cv2
import numpy as np

# Read images
image1 = cv2.imread('DSC07229.JPG')
image2 = cv2.imread('487021350_122205127634162765_4776978011534063537_n.jpg')

# Check if images are loaded
if image1 is None or image2 is None:
    print("Error: One or both images not found!")
    exit()

# Resize image2 to match image1's size
image2_resized = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Subtract images
sub = cv2.subtract(image1, image2_resized)

# Show result
cv2.imshow('Subtracted Image', sub)

# Wait for key press
if cv2.waitKey(0) & 0xFF == 27:  
    cv2.destroyAllWindows()
