import cv2 as cv
import numpy as np

def count_total_triangle(img1):
    no=0
    notmask=cv.bitwise_not(img1)
    # convert the image to grayscale
    gray = img1 #cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # apply thresholding to convert the grayscale image to a binary image
    ret,thresh = cv.threshold(notmask,70,255,0)

    # find the contours
    contours,hierarchy = cv.findContours(thresh,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    print("Number of contours detected:",len(contours))
    cv.im
    gg=cv.drawContours(thresh, contours, -1, (0,255,0),1)
    cv.imshow("dfgh",gg)

    for cnt in contours:
       approx = cv.approxPolyDP(cnt, 0.001*cv.arcLength(cnt, True), True)
       if len(approx) == 3:
           no+=1
    return no
    
    

# read the image
img = cv.imread("11.png")

# handling wrong file name
if img is None:
        print("Invalid Image Name")
        
else:

    # convert BGR image to HSV image
    hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
    

    # Set the bounds for the brown hue
    lr_br=np.array([5,100,10])
    ur_br=np.array([30,255,200])
    

    # Set the bounds for the green hue
    lr_gr=np.array([35,100,20])
    ur_gr=np.array([80,255,255])
    

    # create a mask using bounds set for burnt area
    mask_br=cv.inRange(hsv,lr_br,ur_br)
    bit_br=cv.bitwise_and(img, img, mask=mask_br)
    

    # create a mask using bounds set for green area
    mask_gr=cv.inRange(hsv,lr_gr,ur_gr)
    bit_gr=cv.bitwise_and(img, img, mask=mask_gr)
    
    

    # Find total no of triangle in brown area
    print(count_total_triangle(mask_br))
    


    #bgr=cv.cvtColor(bit_gr,cv.COLOR_HSV2BGR)
    #cv.imshow("   ",bgr)
    #cv.imwrite("bruntimg.png",bit_gr)
        #change colour of burnt area
        #mask_br[np.where((mask_br==[1,1,1]))]=[0,0,255]
      #  burntimg=cv.cvtColor(mask_br,cv.COLOR_BGR2HSV)

       # cv.imshow("bit",bit_br)
    #cv.imshow("mask",mask_br)
    #cv.imshow("correct",bit_br)                     
        #cv.imshow("img",img)




        


