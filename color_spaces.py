import cv2 as cv 
import matplotlib.pyplot as plt 

# BGR image
img = cv.imread('Photos/pexels-pixabay-158063.jpg')
img = cv.resize(img, (400, 400)) # To make it fit the screen (for personal ease)
cv.imshow('Park', img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV (hue saturation value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB [L*a*b]
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
gmi = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', gmi)

cv.waitKey(0)