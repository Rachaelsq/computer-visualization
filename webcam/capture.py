import cv2, time
import os
import numpy as np
#np.set_printoptions(threshold=np.inf)       
np.set_printoptions(threshold=55)       
# print out all of any numpy array

''' 
1. read a video (webcam or video file)
2. apply operations such as adding text or detecting objects
3. 



'''

#reading the video
video=cv2.VideoCapture(0)

while True:
    #show the video
    check, frame = video.read()
    print(check)
    print(frame)

    #convert to grayscale, sleep, show
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
# time.sleep(6)
    cv2.imshow("Capturing", gray)

    #key is pressed then video is released
    key=cv2.waitKey(1)
    
    if key==ord('s'):
        break

    
video.release()
cv2.destroyAllWindows