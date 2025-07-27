import cv2 as cv 

def resizeFrame(frame, scale=0.20):
    height = int(frame.shape[0] * scale) 
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Photos/pexels-pixabay-158063.jpg')
img = resizeFrame(img)
cv.imshow('Park', img)

# Convert image to grayscale
gray = cv.cvtColor(img,  cv.COLOR_BGR2GRAY)
cv.imshow('Kitty Gray', gray)

cv.waitKey(0)