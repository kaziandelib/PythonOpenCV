import os 
import cv2 as cv 
import numpy as np 

sports_people = []
for i in os.listdir(r'F:\\All My Code\\PythonOpenCV\\BuiltIn_Face_Recognizer\\Faces\\train'):
    sports_people.append(i)

DIR = r'F:\\All My Code\\PythonOpenCV\\BuiltIn_Face_Recognizer\\Faces\\train'
haar_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml') 


features = []
labels = []

def create_train():
    for sports_person in sports_people:
        path = os.path.join(DIR, sports_person)
        label = sports_people.index(sports_person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rectangle = haar_cascade.detectMultiScale(gray, scaleFactor=1.11, minNeighbors=5)
            
            for (x, y, w, h) in faces_rectangle:
                face_roi = gray[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)
                
                
create_train()
print(f'Length of features: {len(features)}')
print(f'Lengthof labels: {len(labels)}')

# Convert features and labels to np arrays
features = np.array(features, dtype='object')
labels = np.array(labels)

face_recog = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer
face_recog.train(features, labels)
print(f'Training Done')

face_recog.save('face_recognizer_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
print(f'Saving Done')
