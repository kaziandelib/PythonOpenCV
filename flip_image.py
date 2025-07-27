import cv2 as cv 

img = cv.imread('Photos/pexels-pixabay-416160.jpg')
img = cv.resize(img, (400, 400)) # To make it fit the screen (for personal ease)
cv.imshow('Sleepy Kitty', img)


flipA = cv.flip(img, 0) # vertical flip (over the x-axis)
cv.imshow('Vert', flipA)


flipB = cv.flip(img, 1) # horizontal flip (over the y-axis)
cv.imshow('Hor', flipB)

flipC = cv.flip(img, -1) # both horizontal and vertical flip
cv.imshow('Both', flipC)

cv.waitKey(0)