#we will try to detecd obj from certain threshold
import cv2 as cv
import numpy as np
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

main_img = cv.imread("ss.png",cv.IMREAD_UNCHANGED)#albion_cabbage.jpg
obj = cv.imread("obj.png",cv.IMREAD_UNCHANGED)#albion_farm.jpg

match_result = cv.matchTemplate(main_img,obj,cv.TM_SQDIFF_NORMED)# TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
#match_result  will return matrix in accuracy will be ther of every pixel that match with obj


threshold = 0.01#set the threshold or accuracy of pixel you want to see (80%)
locations = np.where(threshold>= match_result)#it will return tuple
locations = list(zip(*locations[::-1]))#to read that ugly tuple and extract meaningfull data of pixels.it will return list


#((((((((((((((((((( Code for making rectangle with mor than 80% accuracy)))))))))))))))))))
if locations:
    #assgining perameter of rectangle
    rec_width = obj.shape[0]
    rec_height = obj.shape[0]
    rec_color = (0,255,0)#green select rgb color
    rec_lin_typ = cv.LINE_4
    for loc in locations:
        # Determine the box positions
        top_left = loc
        bottom_right = (top_left[0] + rec_width, top_left[1] + rec_height)
        # Draw the box
        cv.rectangle(main_img, top_left, bottom_right, rec_color, rec_lin_typ)
    cv.imshow('Matches', main_img)
    cv.waitKey()
    #cv.imwrite('result.jpg', main_img)

else:
    print('Needle not found.')

#print(locations)