'''
       // * Detects faces (0<=f<=10) in an image and returns them in the form of a list of tuples.
	  * Tuples are of the form (x,y,w,h) where 
	  * x is the x coordinate of the top-left corner of the image
	  * y is the y coordinate of the top-left corner of the image
	  * w is the width of the image
	  * h is the height of the image
	  * @author : Abhilasha
	  * @author : Supriya
	  * @author : Varshini
      //
'''

import cv2
import sys

class FaceDetector:
	def __init__(self,imagePath,cascPath = "haarcascade_frontalface_alt.xml"):
		'''Accepts the image to recognise faces in'''
		self.imagePath = imagePath
		self.cascPath = cascPath

	def detect_faces(self):
		'''Finds the faces in a given image'''
		faceCascade = cv2.CascadeClassifier(self.cascPath)
		# Read the image
		image = cv2.imread(self.imagePath)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		# Detect faces in the image
		self.faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags = cv2.cv.CV_HAAR_SCALE_IMAGE)

	def get_faces(self):
		'''Returns faces in an image'''
		return self.faces
		
	def no_of_faces(self):
		'''Returns number of faces in an image'''
		#print len(self.faces)
		return len(self.faces)

	def show_visualization(self):
		'''Displays the image with a rectangle drawn around each of the faces'''
		image = cv2.imread(self.imagePath)
		for (x, y, w, h) in self.faces:
		    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
		cv2.imshow("Faces found", image)
		cv2.waitKey(0)
		
	def setImagePath(self,imagePath):
		'''Sets a new image path'''
		self.imagePath = imagePath

	def setCascPath(self,cascPath):
		'''Sets a new path for haar features'''		
		self.cascPath = cascPath
