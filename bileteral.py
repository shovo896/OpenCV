import cv2
img=cv2.imread('1bit1.png')
bilateral=cv2.bilateralFilter(img,15,100,100)
cv2.imshow('Bilateral',bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()