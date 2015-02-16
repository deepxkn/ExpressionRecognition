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

a = FaceDetector("test1.jpg")
a.detect_faces()
a.no_of_faces()
a.show_visualization()
