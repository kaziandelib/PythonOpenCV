import cv2 as cv 
import numpy as np

# BGR image
img = cv.imread('Photos/pexels-pixabay-158063.jpg')
img = cv.resize(img, (400, 400)) # To make it fit the screen (for personal ease)
cv.imshow('Park', img)

b, g, r = cv.split(img)
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(f'Shapes:\nImage: {img.shape}\nBlue: {b.shape}\nGreen: {g.shape}\nRed: {r.shape}')

combined = cv.merge([b, g, r])
cv.imshow('Combined', combined)


blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow('JustBlue', blue)
cv.imshow('JustGreen', green)
cv.imshow('JustRed', red)


cv.waitKey(0)