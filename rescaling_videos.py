import cv2 as cv 

def rescaleFrame(frame, scale=0.75):
    height = int(frame.shape[0] * scale) 
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# When using a filepath
capture = cv.VideoCapture('Videos/855029-hd_1920_1080_30fps.mp4')

# Read video frame by fame
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    # Display each frame
    cv.imshow('Video Resized', frame_resized)
    
    # break out of the while loop
    if cv.waitKey(20) & 0xFF==ord('x'): # Press x to escape
        break 
    
capture.release()
cv.destroyAllWindows()