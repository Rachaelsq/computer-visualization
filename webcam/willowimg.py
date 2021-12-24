''' from cv2 import cv2'''
import cv2
import numpy

''' 
===================
LOAD IMAGE
===================
'''
img=cv2.imread("webcam\willow.jpg",0)
print(type(img))
print(img.shape)
print(img)
print(img.shape)


''' 
===================
DISPLAY IMAGE
===================
'''
#resize image before showing it

#show the image


#show the image(galaxy)
''' resized_image=cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("galaxy", resized_image)
cv2.waitKey(2)
cv2.destroyAllWindows() '''


''' 
===================
SAVE resized IMAGE
===================
'''
