#3
#in this we will make many rectangl that into one
import cv2 as cv
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

main_img = cv.imread("albion_farm.jpg",cv.IMREAD_UNCHANGED)
obj = cv.imread("albion_cabbage.jpg",cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(main_img,obj,cv.TM_SQDIFF_NORMED)

threshold = 0.17
locations = np.where(threshold >= result )
locations = list(zip(*locations[::-1]))

#(((((((((((((((((((((((((  detect most probeble position by showing rect    )))))))))))))))))))))))))
'''if locations:
    #--------------- code for printing rectangle on location ----------------
    #assgining perameter of rectangle
    rec_width = obj.shape[1]
    rec_height = obj.shape[0]
    rec_color = (0,255,0)#green select rgb color
    rec_lin_typ = cv.LINE_4
    for loc in locations:
        # Determine the box positions
        top_left = loc
        bottom_right = (top_left[0] + rec_width, top_left[1] + rec_height)
        # Draw the box
        cv.rectangle(main_img, top_left, bottom_right, rec_color, rec_lin_typ)
        #------------------------  Rect close -------------------------------
        
        #----code for printing msg on scren---------
        font = cv.FONT_HERSHEY_SIMPLEX
        # org
        org = loc
        # fontScale
        fontScale = 1
        # Blue color in BGR
        color = (255, 230, 10)
        # Line thickness of 2 px
        thickness = 2
        # Using cv2.putText() method
        image = cv.putText(main_img, 'obj', org, font, 
                   fontScale, color, thickness, cv.LINE_AA)
        #--------------------- Msg on scrn close---------------------------------------
   
    # Displaying the image
    cv.imshow("result", image) 
    cv.waitKey()

else:
    print('Needle not found.')'''#code for printing many rec
#((((((((((((((((((((  showing close  ))))))))))))))))))))


#(((((((((((((((((((   Will try to reduce rectangle   )))))))))))))))))))
#we will get many location we will take most accurat rectanle from many
#we can do it by opencv groupRectangle() function but for that we have to amke list of x,y,w,h
rectangles = []
rec_width = obj.shape[1]
rec_height = obj.shape[0]
for loc in locations:
        rect = [int(loc[0]), int(loc[1]), rec_width, rec_height]# [x,y,w,h]
        # Add every box to the list twice in order to retain single (non-overlapping) boxes
        rectangles.append(rect)
        rectangles.append(rect)

# The groupThreshold parameter should usually be 1. If you put it at 0 then no grouping is
# done. If you put it at 2 then an object needs at least 3 overlapping rectangles to appear
# in the result. I've set eps to 0.5, which is:
# "Relative difference between sides of the rectangles to merge them into a group."
rectangles, weights = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)

for (x,y,w,h) in rectangles:
        top_left = (x, y)
        bottom_right = (x + w, y + h)
        color = (0,255,0)
        lin_typ = cv.LINE_4
        cv.rectangle(main_img, top_left, bottom_right, color ,lin_typ )
                
        #---------------- to get center point of rectangle ------------------------
        points = []
        center_x = x + int(w/2)
        center_y = y + int(h/2)
        # Save the points
        points.append((center_x, center_y))
        cv.drawMarker(main_img, (center_x, center_y),
                              color=(255, 0, 255), markerType=cv.MARKER_CROSS, 
                              markerSize=40, thickness=2)
        #-------------- center point close ----------------
        #NOTE center point can be use full if we want to clik on that place using win32 python lib




cv.imshow("result",main_img)
cv.waitKey()

#((((((((((((((((((    try code close   )))))))))))))))))) 




