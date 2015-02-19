'''
       // * Detects noses given a face
	  * @author : Abhilasha
	  * @author : Supriya
	  * @author : Varshini
      //
'''

import cv2
import sys

class NoseDetector:
	def __init__(self,face,imagePath="",cascPath = "../haarcascades/haarcascade_mcs_nose.xml",gray = None):
		'''Accepts the image to recognise faces in'''
		self.face = face		#TODO: Clean up this section. If you have face, you do not need x,y,w,h
		self.x= face[0]
		self.y = face[1]
		self.w = face[2]
		self.h = face[3]
		self.isImage = int(gray == None)
		self.imagePath = imagePath
		self.cascPath = cascPath
		self.gray = gray
		

	def detect_noses(self):
		'''Finds the nose in a given face'''
		noseCascade = cv2.CascadeClassifier(self.cascPath)
		if self.isImage:
			# Read the image
			image = cv2.imread(self.imagePath)
			self.gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		# Detect faces in the image
		print self.x
		print self.y
		print self.w
		print self.h
		print self.gray
		roi_gray = self.gray[self.y:self.y+self.h, self.x:self.x+self.w]
		noses = noseCascade.detectMultiScale(roi_gray)
		try:
			if(len(noses) == 1):
				self.nose = noses
				print "HERE"
				print self.nose
				return self.nose
			else:
				print "Too few or too many noses detected"
			#TODO : Put nose handling logic
		except:
			print "Problem detecting nose in face"
		
			
		


	def get_nose(self):
		'''Returns nose in a face'''
		return self.nose
		

	def set_face(self, face):
		self.x= face[0]
		self.y = face[1]
		self.w = face[2]
		self.h = face[3]

	def show_visualization(self,imagePath=""):
		'''Displays the image with a rectangle drawn around each of the faces'''
		try:
			if self.nose!= None:
				if self.isImage:
					image = cv2.imread(self.imagePath)
					roi_face = image[self.y:self.y+self.h,self.x:self.x+self.w]
					#print "I'm here"
				else:
					image = self.gray
					roi_face = self.gray[self.y:self.y+self.h,self.x:self.x+self.w]
					#print "HERE"
				cv2.rectangle(image,(self.x,self.y),(self.x+self.w,self.y+self.h),(255,0,0),2)
				#roi_face = self.gray[self.y:self.y+self.h,self.x:self.x+self.w]
				#for (ex,ey,ew,eh) in self.nose:

				cv2.rectangle(roi_face,(self.nose[0][0],self.nose[0][1]),(self.nose[0][0]+self.nose[0][2],self.nose[0][1]+self.nose[0][3]),(0,0,255),2)
				print "VARSHINI AND ABHILASHA 4EVA"
				print self.face
				print self.nose
				cv2.imshow("Faces found", image)
				cv2.waitKey(0)
		except Exception as e:
			print e
			print "Cannot visualize. Nose not detected correctly"
		
	def setImagePath(self,imagePath):
		'''Sets a new image path'''
		self.imagePath = imagePath

	def setCascPath(self,cascPath):
		'''Sets a new path for haar features'''		
		self.cascPath = cascPath
