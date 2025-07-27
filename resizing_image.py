import cv2 as cv 

def resizeFrame(frame, scale=0.20):
    height = int(frame.shape[0] * scale) 
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('Photos/pexels-ihsanaditya-1056251.jpg')
resize_img = resizeFrame(img)
cv.imshow('Sleepy Cat', resize_img)

cv.waitKey(0)