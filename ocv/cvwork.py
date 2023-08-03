import cv2 as cv 
import numpy as np


def match_img(live_img_path , obj_img_path , threshold=0.9 , style="rect"):
    
    live_img = cv.imread(live_img_path,cv.IMREAD_UNCHANGED)
    obj = cv.imread(obj_img_path,cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(live_img,obj,method = cv.TM_CCOEFF_NORMED)

    obj_w = obj.shape[1]
    obj_h = obj.shape[0]
    min_val , max_val , min_loc , max_loc = cv.minMaxLoc(result)

    #threshold
    location = np.where(result >= threshold)
    location = list(zip(*location[::-1]))#to convert (array([294], dtype=int64), array([856], dtype=int64)) into (x,y) form

    #creating reactangle list to give function
    rectangle = []
    for loc in location:
        rect = [int(loc[0]),int(loc[1]),obj_w , obj_h]
        rectangle.append(rect)
        rectangle.append(rect)#written twic becuse if their is only one match groupRectangle functon will ignor it and nothing will print
    
    rectangle , weight = cv.groupRectangles(rectangle,1,0.5)
    #points = []
    if len(rectangle):
        for (x,y,w,h) in rectangle:
            if style =="rect":
                top_left = (x,y)
                bottom_right = (x+w , y+h)
                rec_img = cv.rectangle(live_img,top_left , bottom_right , (0,0,255) , 2)
                cv.imwrite("detected_spot.png",rec_img)

            elif style == "points":
                center_x = x + int(w/2)
                center_y = y + int(h/2)
                rec_img = cv.drawMarker(live_img , (center_x,center_y) , (2,30,0) , cv.MARKER_CROSS )
                cv.imwrite("detected_spot.png",rec_img)


    return center_x , center_y 

