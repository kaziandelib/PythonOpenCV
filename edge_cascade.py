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
ec = cv.Canny(img, 120, 180)
cv.imshow('Edge Cascade', ec)

# Reduce Edges
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
ec2 = cv.Canny(blur, 120, 180)
cv.imshow('Edge Cascade2', ec2)

cv.waitKey(0)