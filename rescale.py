import cv2 as cv

img = cv.imread('photos/animal.jpg')
cv.imshow('animal',img)

def rescaleFrame(frame, scale=0.75):
    #!this is work for images or old videos or live video
    width = int(frame.shape[1] * scale)
    height =int( frame.shape[1] * scale)
    dimentions = (width,height)

    return cv.resize(frame, dimentions, interpolation = cv.INTER_AREA )

resized_img = rescaleFrame(img, scale=0.1)
cv.imshow('image', resized_img)

def changeRes(width, height):
    #!this is work for only live video
    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture('videos/waves_large.mp4')


while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.2)

    cv.imshow('video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()