import cv2
img=cv2.imread('img_5terre.jpg',0)
cv2.imshow('Orginal',image)

cv2.imshow('Grayscale',img)
cv2.waitKey(0)
cv2.destroyAllWindows()