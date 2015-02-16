'''
       // * Performs facial expression recognition by performing the following steps-
	  * 1. Face Detection 
	  * x is the x coordinate of the top-left corner of the image
	  * y is the y coordinate of the top-left corner of the image
	  * w is the width of the image
	  * h is the height of the image
	  * @author : Abhilasha
	  * @author : Supriya
	  * @author : Varshini
      //
'''
from FaceDetection import *
from HistogramNormalization import *


image = "test1.jpg"
histogram_normalizer = HistogramNormalizer(image)
lighted_image = histogram_normalizer.normalize_image()
#a.histogram_visualization()
im = FaceDetector(image)
faces = im.detect_faces(lighted_image)
#print faces
#im.no_of_faces()
#im.show_visualization()
