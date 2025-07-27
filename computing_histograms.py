import cv2 as cv 
import matplotlib.pyplot as plt  

img = cv.imread('Photos/pexels-pixabay-158063.jpg')
img = cv.resize(img, (400, 400)) # To make it fit the screen (for personal ease)
cv.imshow('Park', img)

# Color histogram
colors = ('b', 'g', 'r')
plt.figure()
plt.title('Histogram Colors')
plt.xlabel('Bins')
plt.ylabel('No. of Pixels')
for i, col, in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()

# Grayscale histogram
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

histo_gray = cv.calcHist([gray], [0], None, [256], [0,256])
plt.figure()
plt.title('Histogram Grayscale')
plt.xlabel('Bins')
plt.ylabel('No. of Pixels')
plt.plot(histo_gray)
plt.xlim([0, 256])
plt.show()

cv.waitKey(0)