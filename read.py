import cv2 
img=cv2.imread("1bit1.png",cv2.IMREAD_COLOR)
cv2.imshow("Title",img)
cv2.waitKey(0)
cv2.destroyAllWindows()