import cv2 as cv

# Only for live video 
def changeRes(width, height):
    capture.set(3, width)  
    capture.set(4, height)
    

# Start capturing from webcam
capture = cv.VideoCapture(0)


while True:
    isTrue, frame = capture.read()
    
    frame_resized = cv.resize(frame, (640, 480))
        
    # Display resized frame
    cv.imshow('Video Resized', frame_resized)

    # Press 'x' to exit
    if cv.waitKey(20) & 0xFF == ord('x'):
        break

capture.release()
cv.destroyAllWindows()
