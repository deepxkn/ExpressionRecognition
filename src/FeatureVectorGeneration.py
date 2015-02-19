'''
       /* * Forms feature vectors out of an image which is just a vector of the pixels
	  * @author : Abhilasha
	  * @author : Supriya
	  * @author : Varshini/
'''
from PIL import Image
import cv2

class FeatureVectorGenerator:
	def __init__(self,imagePath=None,image=None):
		'''Accepts image to be converted into feature vectors'''
		self.imagePath = imagePath
		self.image = image

	def get_pixels_from_image(self,imagePath=None):	#Allows image to be dynamically changed
		'''Extracts pixels from the image and stores it in the vectors data structure'''
		vectors = {} # vectors  - stores all points in the image in the form of key-value pairs ((x,y):value)
		vector = [] #List of pixel intensities- ordered
		if imagePath!= None:
			self.imagePath = imagePath
		im = Image.open(self.imagePath,'r') # Open given image		 # Does not convert to RGB
		pix = im.load()
		maxx, maxy = im.size		 # Maximum x and y
		for i in range(maxx):
			for j in range(maxy):
				vectors[(i,j)] = pix[i,j]
				'''print i
				print j
				print maxx
				print maxy'''
				vector.append(pix[i,j])
		return vectors, vector

	def get_pixels_from_rep(self,image = None):
		'''Extracts pixels from an image representation and stores it in a vector'''
		if image!= None:
			self.image = image
		vector = []
		dimensions = image.shape
		if(len(dimensions) == 2):	#Grayscale
			maxx = dimensions[0]
			maxy = dimensions[1]
			for i in range(maxx):
				for j in range(maxy):
					vector.append(image[i,j])
		print vector
		'''rows, columns, channels = image.shape
		print rows
		print columns
		print channels'''
		

im = "../images/test1.jpg"
f = FeatureVectorGenerator(im)

image = cv2.imread(im)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
f.get_pixels_from_rep(gray)
#x,y= f.get_pixels_from_image()
#print y
