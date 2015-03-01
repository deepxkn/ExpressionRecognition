''' /** Script to learn the PCA model to use
	Dimensionality reduction applied
	
	Model pickled
	Subsequently can beused to transform new vector*/

'''
from PIL import Image
import cPickle as pickle
import cv2
import numpy as np
#import pickle
#import sklearn
from sklearn.decomposition import PCA
import glob

np.seterr(divide='ignore', invalid='ignore')
def get_pixels_from_image(imagePath=None):	#Allows image to be dynamically changed
	'''Extracts pixels from the image and stores it in the vectors data structure'''
	vectors = {} # vectors  - stores all points in the image in the form of key-value pairs ((x,y):value)
	vector = [] #List of pixel intensities- ordered
	im = Image.open(imagePath,'r') # Open given image		 # Does not convert to RGB
	pix = im.load()
	maxx, maxy = im.size		 # Maximum x and y
	for i in range(maxx):
		for j in range(maxy):
				#vectors[(i,j)] = pix[i,j]
				'''print i
				print j
				print maxx
				print maxy'''
				vector.append(pix[i,j])
		#vector = vector
	return vector


def construct_dataset():
	#listOfImages = glob.glob("../testimages/*")
	listOfImages = ['../image2.png','../image3.png','../image4.png']
	vectorList = []
	for image in listOfImages:
		vectorList.append(get_pixels_from_image(image))
	print "Vector List"
	#print vectorList
	print len(vectorList)
	return np.array(vectorList)
	

#X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
#y = np.array([[3,-1]])
X = construct_dataset()
print len(X)
#pca = PCA(n_components="mle")
pca = PCA(n_components=4)
pca.fit(X)

#PCA(copy=True, n_components=2, whiten=False)
f = open('test.pickle','wb')
pickle.dump(pca,f)
f.close()
'''g = open('test.pickle','rb')
pca= pickle.load(g)
print(pca.explained_variance_ratio_)
print pca.transform(y) '''
