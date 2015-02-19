'''
       /* * Performs image processing for facial expression recognition by performing the following steps-
	  * 1. Histogram Normalization
	  * 2. Face Detection 
	  * x is the x coordinate of the top-left corner of the image
	  * y is the y coordinate of the top-left corner of the image
	  * w is the width of the image
	  * h is the height of the image
	  * @author : Abhilasha
	  * @author : Supriya
	  * @author : Varshini/
      
'''
from FaceDetection import *
from NoseDetection import *
from EyeDetection import *
from HistogramNormalization import *


def find_nose(face):
	noseFinder = NoseDetector(face,imagePath=image)  #pass gray=lighted_image if using histogrm lighting
	return noseFinder.detect_noses()
	#noseFinder.show_visualization()
	

def find_noses_in_faces(faces):
	faces_noses = [] #List of lists, where each list consists of [face,nose]
	for face in faces:
		faces_noses.append([face,find_nose(face)])
	return faces_noses
	

def find_eye_after_noses(faces_noses):
	faces_noses_eyes = []
	for pair in faces_noses:
		face = pair[0]
		eyeFinder = EyeDetector(face,imagePath = image)
		pair.append(eyeFinder.detect_eyes())
		eyeFinder.show_visualization()
		faces_noses_eyes.append(pair)
	return faces_noses_eyes
	

image = "../images/test1.jpg"
'''histogram_normalizer = HistogramNormalizer(image)
lighted_image = histogram_normalizer.normalize_image()		#Lighted_image is now grayscale, image is in colour
'''
#a.histogram_visualization()
im = FaceDetector(image)
faces = im.detect_faces() #Pass lighted_image 
faces_noses = find_noses_in_faces(faces) 
faces_noses_eyes = find_eye_after_noses(faces_noses)
print faces_noses_eyes
#print faces
#im.no_of_faces()
#im.show_visualization()
