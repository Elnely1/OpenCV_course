import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank', blank) 
#img = cv.imread('photos/weman.jpg')
#cv.imshow('image', img)

#1-Paint
#blank[200:300,300:400]=0,0,255                                 #* Green (0,255,0)
#cv.imshow('Green', blank)                                     #! Red (0,0,255)
                                                              #? Blue (255,0,0)
#2-Draw a rectangle                                           #White (255,255,255) 
cv.rectangle(blank, (0,0), (250,250),(0,255,0),thickness=2)
#to make a plonde rectangle make the thickness = cv.FILLED or -1
#to make a square make the second pt is = (blank.shape[1]//2, blank.shape[0]//2),
cv.imshow('rectangle', blank)

#3-Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 150, (0,0,255),thickness=-1)
cv.imshow('circle', blank)

#4-Draw a line
cv.line(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2), (255,0,0),thickness=5)
cv.imshow('line', blank)

#5-Write a text
cv.putText(blank, 'Hello, My name is Elneely', (20, blank.shape[0]//2), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255),2)
cv.imshow('text', blank)

cv.waitKey(0)