import cv2 as cv
import numpy as np 

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 225, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# bitwise AND -> intersecting regions 
bitwise_AND = cv.bitwise_and(rectangle, circle)
cv.imshow('AND', bitwise_AND)

# bitwise OR -> non-intersecting and intersecting regions 
bitwise_OR = cv.bitwise_or(rectangle, circle)
cv.imshow('OR', bitwise_OR)

# bitwise XOR -> non-intersecting regions
bitwise_XOR = cv.bitwise_xor(rectangle, circle)
cv.imshow('XOR', bitwise_XOR)

# bitwise NOT
bitwise_NOT = cv.bitwise_not(rectangle)
cv.imshow('NOT', bitwise_NOT)


cv.waitKey(0)