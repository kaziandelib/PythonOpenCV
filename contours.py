import cv2 as cv 
import numpy as np

img = cv.imread('Photos/pexels-pixabay-69932.jpg')
img = cv.resize(img, (400, 400)) # To make it fit the screen (for personal ease)
cv.imshow('Sleepy Kitty', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

contours, hierachies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'Contours found: {len(contours)}')

blank = np.zeros(img.shape, dtype='uint8')
cv.drawContours(blank, contours, -1, (255, 255, 0))
cv.imshow('Draw Contours', blank)

cv.waitKey(0)