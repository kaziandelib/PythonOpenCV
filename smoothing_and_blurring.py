import cv2 as cv 
import matplotlib.pyplot as plt 

# BGR image
img = cv.imread('Photos/pexels-pixabay-158063.jpg')
img = cv.resize(img, (400, 400)) # To make it fit the screen (for personal ease)
cv.imshow('Park', img)

# Average Blur
average_blur =  cv.blur(img, (3, 3))
cv.imshow('Average Blur', average_blur)

# Gaussian Blur
gaussian_blur = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gaussian_blur)

# Median Blur
median_blur = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median_blur)

# Bilateral Blur
bilateral_blur = cv.bilateralFilter(img, 12, 35, 35)
cv.imshow('Bilateral Blur', bilateral_blur)

cv.waitKey(0)