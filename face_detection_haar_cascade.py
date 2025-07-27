import cv2 as cv 

# img = cv.imread('Photos/pexels-pixabay-415829.jpg') # single face
img = cv.imread('Photos/pexels-gabby-k-6238122.jpg') # multiple faces
# img = cv.imread('Photos/pexels-cottonbro-3419676.jpg') # multiple faces not looking in the same directions
img = cv.resize(img, (500, 500))
cv.imshow('Face', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Download the xml file from the opencv github 
# Link: https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml') 


faces_rectangle = haar_cascade.detectMultiScale(gray, scaleFactor=1.11, minNeighbors=3)
print(f'Faces found: {len(faces_rectangle)}')


for (x, y, w, h) in faces_rectangle:
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), thickness=3)    
cv.imshow('Faces Detected', img)

cv.waitKey(0)