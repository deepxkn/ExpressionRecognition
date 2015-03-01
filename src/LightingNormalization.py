'''
       // * Performs lighting normalisation on an image
	  * Increases contrast and brighness. Highlights get brighter, lowlights darker 
	  * @author : Abhilasha
	  * @author : Supriya
	  * @author : Varshini
      //
'''

import cv2
import numpy as np

class LightingNormalizer:
	def __init__(self, imagePath):
		'''Takes in image to be light normalized'''
		self.imagePath = imagePath

	def normalize_image(self):
		'''return brightened grayscale version of image'''
		img = cv2.imread(self.imagePath)
		self.grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

		clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
		self.equalized = clahe.apply(self.grayscale)
		#self.equalized = cv2.equalizeHist(self.grayscale)    # Remember histogram equalization works only for grayscale images
		return self.equalized

	def clahe_visualization(self):
		'''shows a visualization of the lighting normalised grayscale image'''
		cv2.imshow('src',self.grayscale)
		cv2.imshow('equ',self.equalized)
		cv2.waitKey(0)
		cv2.destroyAllWindows()

	def setImagePath(self,imagePath):
		'''Sets a new image path'''
		self.imagePath = imagePath




l = LightingNormalizer("../images/test1.jpg")
l.normalize_image()
l.clahe_visualization()
