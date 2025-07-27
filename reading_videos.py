import cv2 as cv 

# When using the camera
# capture = cv.VideoCapture(0) -> when using webcam 
# [it can be 0, 1, 2, 3 depending on the camera 
# 0 is the built-in webcam of the laptop] 


# When using a filepath
capture = cv.VideoCapture('Videos/855029-hd_1920_1080_30fps.mp4')

# Read video frame by fame
while True:
    isTrue, frame = capture.read()
    # Display each frame
    cv.imshow('Video', frame)
    
    # break out of the while loop
    if cv.waitKey(20) & 0xFF==ord('x'): # Press x to escape
        break 
    
capture.release()
cv.destroyAllWindows()