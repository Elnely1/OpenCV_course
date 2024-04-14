import cv2 as cv
#!Reading photos
# For example, to load an image:
# frame = cv2.imread('image.jpg')
#*this is to use cv2 as cv
img = cv.imread('photos/weman.jpg')
#*this to import the photo
cv.imshow('weman',img)
#*to discribe the photo
cv.waitKey(0)
#* TODO the time that the photo will appear in

#import cv2

# Check if the frame is loaded successfully
# if frame is not None:
# or if you're reading from a video:
# if cap.isOpened():

# Ensure that the loaded image or frame has valid dimensions
# if frame.shape[0] > 0 and frame.shape[1] > 0:

# Display the image or video frame
# cv2.imshow('Window Name', frame)

# Wait for a key press and then close the window
# cv2.waitKey(0)
# cv2.destroyAllWindows
#? Reading Videos
capture = cv.VideoCapture('videos/1112.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()




