import cv2 as cv
import numpy as np

try:

    img = cv.imread("11.png")
    if img is None:
        print("Invalid Image Name")
    else:
       # cv.imshow("Display window", img)
        hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
        lrg=np.array([50,100,100])
        urg=np.array([700,255,255])
        mask=cv.inRange(hsv,lrg,urg)
        cv.imshow("mask",mask)




        
except cv.error:
    print("Something Went Wrong")

