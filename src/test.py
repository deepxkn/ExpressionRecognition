import cv2
import numpy as np
import cv


img = cv2.imread('../images/test1.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
surf = cv2.SURF(400)
##sift = cv2.SIFT()
#kp = sift.detect(gray,None)
#kp, des = surf.detectAndCompute(img,None)
#img=cv2.drawKeypoints(gray,kp)

#cv2.imwrite('sift_keypoints.jpg',img)
#print cv2.xfeatures2d.Sift()
#print surf.detectAndCompute()
#print dir(surf)
k =  surf.detect(gray,None)
#print k
#print dir(cv2)
#print dir(cv)
gray = cv.LoadImageM('../images/test1.jpg', cv.CV_LOAD_IMAGE_GRAYSCALE)
(keypoints,descriptors) =  cv.ExtractSURF(gray,None,cv.CreateMemStorage(), (0, 6000, 1, 3))
print len(descriptors)
cv.drawKeypoints(gray,keypoints)
#image,d = cv2.drawKeypoints(gray,k)
#cv2.imwrite('surf_keypoints.jpg',img)
#help(surf.detect)
