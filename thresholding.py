import cv2 as cv 

img = cv.imread('Photos/pexels-pixabay-158028.jpg')
img = cv.resize(img, (400, 400))
cv.imshow('Park', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple threshold
threshold, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', thresh)

# Inverse Threshold
threshold, thresh_inverse = cv.threshold(gray, 125, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Inverse Threshold', thresh_inverse)

# Adaptive Threshold 
adaptive_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 15, 3)
cv.imshow('Adaptive Threshold', adaptive_threshold)

cv.waitKey(0)