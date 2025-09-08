import cv2 
vidcap=cv2.videoCapture('13858986_2048_1080_30fps.mp4')
sucess,image=vidcap.read()
count=0
while sucess:
    sucess,image=vidcap.read()
    resize=cv2.resize(image,(700,500))
    cv2.imwrite("frame%d.jpg" % count,resize)
    if cv2.waitKey(10)==ord('q'):
        break
    count+=1 
 
