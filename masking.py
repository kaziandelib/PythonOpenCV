import cv2 as cv 
import numpy as np 

img = cv.imread('Photos/pexels-pixabay-158063.jpg')
img = cv.resize(img, (400, 400)) # To make it fit the screen (for personal ease)
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('MASK', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked)

cv.waitKey(0)