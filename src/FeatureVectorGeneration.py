'''
       /* * Forms feature vectors out of an image which is just a vector of the pixels
	  * @author : Abhilasha
	  * @author : Supriya
	  * @author : Varshini/
'''
from PIL import Image
import cv2
import cv
#from matplotlib.mlab import PCA
import numpy as np
from sklearn.decomposition import PCA
import cPickle as pickle

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
		self.vector = vector
		return vectors, vector

	def SURF(self,image = None):
		if image!=None:
			self.imagePath = image
		gray = cv.LoadImageM(self.imagePath, cv.CV_LOAD_IMAGE_GRAYSCALE)
		(keypoints,descriptors) =  cv.ExtractSURF(gray,None,cv.CreateMemStorage(), (0, 6000, 1, 3))
		return descriptors

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
		self.vector = vector
		print vector
		'''rows, columns, channels = image.shape
		print rows
		print columns
		print channels'''

	def get_pixels_helper(self,imagePath=None):	#Allows image to be dynamically changed
		'''Extracts pixels from the image and stores it in the vectors data structure'''
		vector = [] #List of pixel intensities- ordered
		im = Image.open(imagePath,'r') # Open given image		 # Does not convert to RGB
		pix = im.load()
		maxx, maxy = im.size		 # Maximum x and y
		for i in range(maxx):
			for j in range(maxy):
					vector.append(pix[i,j])
			#vector = vector
		return vector

	def PCA(self,imagePath=None,gray=None):
		pickled_file = "test.p"
		vector = [[]]
		if imagePath == None and gray!= None:
			for i in range(len(gray)):
				for j in range(len(gray[i])):
					vector[0].append(gray[i][j])
		else:
			vector[0] = self.get_pixels_helper(imagePath)
		y = np.array(vector)
			
		g = open('test.pickle','rb')
		pca= pickle.load(g)
		#print(pca.explained_variance_ratio_)
		return pca.transform(y) 

		

im = "../images/test.jpg"
im = "../image4.png"
f = FeatureVectorGenerator(im)
print f.PCA(im)
#print len(f.SURF())
'''
image = cv2.imread(im)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
f.get_pixels_from_rep(gray)'''
#x,y= f.get_pixels_from_image()
#print y
