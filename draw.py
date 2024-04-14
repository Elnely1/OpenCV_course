import cv2 as cv
import numpy as np

blank = np.zeros((500,500), dtype='uint8')
cv.imshow('blank', blank) 
img = cv.imread('photos/weman.jpg')

cv.imshow('image', img)

cv.waitKey(0)