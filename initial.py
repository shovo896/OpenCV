import cv2

# Load an image from file
image = cv2.imread('example.jpg')  # Make sure 'example.jpg' is in the same folder

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found!")
else:
    # Display the image in a window
    cv2.imshow('My Image', image)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
