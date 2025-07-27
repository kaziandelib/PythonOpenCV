import cv2 as cv 
import numpy as np

img = cv.imread('Photos/pexels-pixabay-416160.jpg')
img = cv.resize(img, (640, 480)) # To make it fit the screen (for personal ease)
cv.imshow('Sleepy Kitty', img)

# Rotation
def rotate(img, angle, rotationPoint=None):
    (height, width) = img.shape[:2]
    if rotationPoint is None:
        rotationPoint = (width//2, height//2)
    
    rotationMatrix = cv.getRotationMatrix2D(rotationPoint, angle, 1.0)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotationMatrix, dimensions)

rotated = rotate(img, 90)
cv.imshow('Rotate', rotated)

rotated2 = rotate(rotated, 90)
cv.imshow('Rotate2', rotated2)

rotated3 = rotate(rotated2, 90)
cv.imshow('Rotate3', rotated3)

cv.waitKey(0)