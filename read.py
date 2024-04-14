import cv2 as cv                            #this is to use cv2 as cv
#!Reading photos:
img = cv.imread('photos/weman.jpg')       #this to import the photo
cv.imshow('weman',img)                   #to discribe the photo
cv.waitKey(0)                           # the time that the photo will appear in 

#? Reading Videos:
capture = cv.VideoCapture('videos/1112.mp4')
while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()