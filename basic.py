import cv2 as cv

img = cv.imread('photos/cats.jpg')
cv.imshow('cats', img)

#convert to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#blur
blue = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('blur', blue)

#edge cascade
canny = cv.Canny(blue, 125, 175)
cv.imshow('canny edge', canny)

#dilating the image
dilate = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilate', dilate)

#eroding        #? get it back to the cascaded
erote = cv.erode(dilate, (7,7), iterations=3)
cv.imshow('eroted', erote)

#resized
resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resize)
#*in resizing we can use in the interpolation cv.INTER_AREA in convert to small size
#*                                                    _LINER  in convert to large size
#*                                                    _CUBIC   the slloest one but get me the the besst quality
#cropping
cropped = img[50:300,100:500]
cv.imshow('cropped', cropped)

cv.waitKey(0)