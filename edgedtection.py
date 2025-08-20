import cv2
FILE_NAME='2bit2.png'
img=cv2.imread(FILE_NAME)
edges=cv2.canny(img,100,200)
cv2.imshow('Edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
               