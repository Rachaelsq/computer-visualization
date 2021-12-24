''' from cv2 import cv2'''
import cv2
import numpy

''' 
===================
LOAD IMAGE
===================
'''
img=cv2.imread("webcam\galaxy.jpg",0)
print(type(img))
print(img.shape)
print(img)
print(img.shape)


''' 
===================
DISPLAY IMAGE
===================
'''

#show the image(galaxy)
resized_image=cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("galaxy", resized_image)
cv2.waitKey(2)
cv2.destroyAllWindows()


''' 
===================
SAVE resized IMAGE
===================
'''
resized_image=cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()