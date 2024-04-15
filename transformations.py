import cv2 as cv
import numpy as np

img = cv.imread('photos/cats.jpg')
cv.imshow('cats', img)

#translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x],[0, 1, y]])
    dimentions =  (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimentions)
#-x -----> left
#-y -----> up
#x ------> right
#y ------> down

translated = translate(img, 100, 100)
cv.imshow('translated', translated)

#rotation
def rotate(img, angle, rotpoint=None):
    (height,width)=img.shape[:2]
    
    if rotpoint is None :
        rotpoint =(width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)
    dimentions = (width, height)
    return cv.warpAffine(img, rotMat, dimentions)

rotated = rotate(img, 45)
cv.imshow('rotated', rotated)
rotated_rotate = rotate(img, -45)
cv.imshow('rotated rotate', rotated_rotate)

#flipping
flip = cv.flip(img, 0)                    #? 0--> vertical flip
cv.imshow('fliped', flip)                 #? 1--> horizontal flip
                                          #?-1--> both of them



cv.waitKey(0)