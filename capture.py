from webcam import Webcam
import cv2
from datetime import datetime
  
webcam = Webcam()
webcam.start()
 
while True:
     
    # get image from webcam
    image = webcam.get_current_frame()
 
    # display image
    cv2.imshow('grid', image)
    cv2.waitKey(300)
 
    # save image to file, if pattern found
    ret, corners = cv2.findChessboardCorners(cv2.cvtColor(image,cv2.COLOR_BGR2GRAY), (6,9), None)
 
    if ret == True:
        filename = datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f') + '.jpg'
        print(filename)
        #cv2.imwrite("sample_images/" + filename, image)
        cv2.imwrite("hehe/" + filename, image)

