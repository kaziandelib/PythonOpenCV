import cv2 as cv 
import numpy as np 

# Create blank image
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# Paint image 
blank[200:300, 300:400] = 255, 0, 0
cv.imshow('bluebg', blank)

# Draw a rectangle
cv.rectangle(blank, (0, 0), (250, 250), (255, 255, 255), thickness=2)
cv.imshow('Rectangle', blank)

# Fill in image
cv.rectangle(blank, (0, 0), (250, 250), (255, 255, 255), thickness=-1)
cv.imshow('Rectangle2', blank)

# Draw a circle
cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness=3)
cv.imshow('Circle', blank)

# Draw a line
cv.line(blank, (0, 0), (250, 250), (255, 255, 215), thickness=4)
cv.imshow('Line', blank)

# Write text
cv.putText(blank, 'Mew', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.2, (201, 211, 201), 5)
cv.imshow('Text', blank)


cv.waitKey(0)