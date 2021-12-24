import cv2
import os

''' 
===================

===================
'''

#create/ import haar file to search img for faces
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#find img
this_folder = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(this_folder, "photo.jpg")

#read the img as grayscalle (increased accuracy, but colored img at the end)
img = cv2.imread(my_file)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cv2.imshow("Gray", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

