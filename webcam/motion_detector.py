import cv2, time
import os
import numpy as np
#np.set_printoptions(threshold=np.inf)       
    
# print out all of any numpy array


first_frame=None

#reading the video
video=cv2.VideoCapture(0)

while True:
    #show the video
    check, frame = video.read()

    #convert to grayscale, apply blur to remove noise/increase accuracy
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    
    #dont run the rest of the code, just keep running the loop if there is nothing there
    if first_frame is None:
        first_frame=gray
        continue
    
    #compare first (empty) frame with current frame
    delta_frame=cv2.absdiff(first_frame,gray)
    
    
# time.sleep(6)
    cv2.imshow("Gray Frame ", gray)
    cv2.imshow("Delta Frame",delta_frame)

    #key is pressed then video is released
    key=cv2.waitKey(1)
    
    if key==ord('s'):
        break

video.release()
cv2.destroyAllWindows


''' motion capturing
1. first capture the static background so it can be used as a base.
store as a variable and convert to grayscale
2. the while loop will convert the current images/camera captures to grayscale and
apply the difference between the current/static image
3. apply the threshole: if there is a difference in the dleta frame of a certain
intensity, convert the pixel to white. convert the others to black
4. find the contours of the white object. write a foor looop to check if
the white areas > 500px, consider it a moving object
5. draw rectangle around those objects



'''