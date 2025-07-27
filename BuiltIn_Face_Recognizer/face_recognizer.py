import cv2 as cv 
import os
import numpy as np 

haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml') 

sports_people = []
for i in os.listdir(r'F:\\All My Code\\PythonOpenCV\\BuiltIn_Face_Recognizer\\Faces\\train'):
    sports_people.append(i)

features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy', allow_pickle=True)

face_recog = cv.face.LBPHFaceRecognizer_create()
face_recog.read('face_recognizer_trained.yml')

img = cv.imread(r'F:\\All My Code\\PythonOpenCV\\BuiltIn_Face_Recognizer\\Faces\\test\\maria_sharapova\\maria_sharapova33.png')
# img = cv.resize(img, (500, 500))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Person", gray)

# Detect face
face_rectangles = haar_cascade.detectMultiScale(gray, scaleFactor=1.11 ,minNeighbors=5)

for (x, y, w, h) in face_rectangles:
    face_roi = gray[y:y+h, x:x+w]
    
    label, confidence_value = face_recog.predict(face_roi)
    print(f'Label: {sports_people[label]}\n Confidence {confidence_value}')
    cv.putText(img, str(sports_people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 0), thickness=3)
    cv.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), thickness=3) 
    
cv.imshow('Detected Face', img)
cv.waitKey(0)