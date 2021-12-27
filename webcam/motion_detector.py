import cv2, time, pandas
import os
import numpy as np
from datetime import datetime
#np.set_printoptions(threshold=np.inf)       
    
# print out all of any numpy array


first_frame=None
status_list=[None,None]
times=[]
df=pandas.DataFrame(columns=["Start", "End"])

#reading the video
video=cv2.VideoCapture(0)

while True:
    #show the video
    check, frame = video.read()
    status=0
    #convert to grayscale, apply blur to remove noise/increase accuracy
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    
    #dont run the rest of the code, just keep running the loop if there is nothing there
    if first_frame is None:
        first_frame=gray
        continue
    
    #compare first (empty) frame with current frame
    delta_frame=cv2.absdiff(first_frame,gray)

    #3. apply the threshole: if there is a difference in the delta frame of a certain
    #intensity, convert the pixel to white. convert the others to black

    thresh_frame=cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    #remove the black holes from the white areas in the white areas
    thresh_frame=cv2.dilate(thresh_frame, None, iterations=2)
    
    #find the contours of the white object. write a foor loop to check if
    #the white areas > 500px, consider it a moving object
    (cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 5000:
            continue
        status=1
        
        (x, y, w, h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
    status_list.append(status)
    #recording the time of status changes
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())
        
    # show these frames
    cv2.imshow("Gray Frame ", gray)
    cv2.imshow("Delta Frame",delta_frame)
    cv2.imshow("Threshold Frame",thresh_frame)
    cv2.imshow("Color Frame", frame)

    #key is pressed then video is released
    key=cv2.waitKey(1)
    
    if key==ord('s'):
        if status==1:
            times.append(datetime.now())
        break
    
print(status_list)
print(times)

#access the first item in times and append it to the pandas column
for i in range(0,len(times),2):
    df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)
    
df.to_csv("Times.csv")
video.release()
cv2.destroyAllWindows


''' motion capturing
1. first capture the static background so it can be used as a base.
store as a variable and convert to grayscale
2. the while loop will convert the current images/camera captures to grayscale and
apply the difference between the current/static image
3. apply the threshole: if there is a difference in the delta frame of a certain
intensity, convert the pixel to white. convert the others to black
4. find the contours of the white object. write a foor looop to check if
the white areas > 500px, consider it a moving object
5. draw rectangle around those objects
6. when the status changes from 0 to 1, record that time. record the time when the
status changes from 0to 1 as well



'''