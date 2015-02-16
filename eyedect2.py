import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/haarcascades/haarcascade_eye.xml')

img = cv2.imread('test2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
print len(faces)
'''
for (x,y,w,h) in faces:
    img1 = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    roi_gray = gray1[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

'''
cv2.imshow('img',img)
cv2.waitKey(0)
#cv2.destroyAllWindows()
