import cv2 

# Open video file
vidcap = cv2.VideoCapture('13858986_2048_1080_30fps.mp4')

success, image = vidcap.read()
count = 0

while success:
    # Resize frame
    resize = cv2.resize(image, (700, 500))

    # Save frame as image
    cv2.imwrite(f"frame{count}.jpg", resize)

    # Read next frame
    success, image = vidcap.read()
    count += 1

    # Optional: quit with 'q'
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

vidcap.release()
cv2.destroyAllWindows()

