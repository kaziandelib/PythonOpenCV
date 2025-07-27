import cv2 as cv 
import numpy as np

img = cv.imread('Photos/pexels-pixabay-416160.jpg')
img = cv.resize(img, (400, 400)) # To make it fit the screen (for personal ease)
cv.imshow('Sleepy Kitty', img)

# Translation

def translation(img, x, y):
    translationMatrix = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, translationMatrix, dimensions)

# -x -> left 
# -y -> up
# x -> right 
# y -> down
    

translated_img = translation(img, 100, 100)
translated_img = cv.resize(translated_img, (640, 480))
cv.imshow('Translated Image', translated_img)


translated_img2 = translation(img, 100, -100)
translated_img2 = cv.resize(translated_img2, (640, 480))
cv.imshow('Translated Image 2', translated_img2)


cv.waitKey(0)