import cv2 as cv 

def resizeFrame(frame, scale=0.20):
    height = int(frame.shape[0] * scale) 
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Photos/pexels-pixabay-158063.jpg')
img = resizeFrame(img)
cv.imshow('Park', img)

# Edge Cascade
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
ec = cv.Canny(blur, 120, 180)
cv.imshow('Edge Cascade', ec)

# Dilate the image
dilate = cv.dilate(ec, (3,3), iterations=3)
cv.imshow('Dilated', dilate)

# Eroding the dilation
eroded = cv.erode(dilate, (3,3), iterations=3)
cv.imshow('Eroded', eroded)

cv.waitKey(0)