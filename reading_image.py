import cv2 as cv 

img1 = cv.imread('Photos/pexels-ihsanaditya-1056251.jpg')
cv.imshow('Cat', img1)

cv.waitKey(0)