import cv2

def resize(sample_images):
    for images in sample_images:
        resized_image=cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))
        cv2.imshow("", resized_image)
        cv2.imwrite(".jpg", resized_image)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()
        return images
