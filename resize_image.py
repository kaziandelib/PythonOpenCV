import cv2 as cv 

img = cv.imread('Photos/pexels-pixabay-158028.jpg')
resized = cv.resize(img, (640, 480))
cv.imshow('Resize', resized)

cv.waitKey(0)