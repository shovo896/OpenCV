import cv2 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascade+'haarcascade_eye.xml' )
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')