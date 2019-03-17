import numpy as np
import random
import cv2

def getImage():
	image = cv2.imread('full1.jpg')
	height, width, channels = image.shape
	print(height)
	print(width)
	image = cv2.resize(image,(800,600))
	#getImage(image)
	y=90
	x=250
	h=430
	w=400
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
	#cv2.imshow('Image1' , image)
	crop = image[y:y+h, x:x+w]
	#cv2.imshow('Image', crop)
	#choice = input("Do you want to save the file")
	cv2.imwrite("ImagetobeSearched/image.jpg" , crop)
	cv2.waitKey(5)
	print("Saved Successfully!!")
