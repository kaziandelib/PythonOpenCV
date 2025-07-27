import cv2 as cv 
import numpy as np 

img = cv.imread('Photos/pexels-pixabay-416160.jpg')
img = cv.resize(img, (400, 400))
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
laplacian = cv.Laplacian(gray, cv.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))
cv.imshow('Laplacian', laplacian)

# Sobel
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobel_combined = cv.bitwise_or(sobel_x, sobel_y)
cv.imshow('Sobel X', sobel_x)
cv.imshow('Sobel Y', sobel_y)
cv.imshow('Combined Sobel', sobel_combined)

cv.waitKey(0)
