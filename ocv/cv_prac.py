import cv2 as cv
#import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))#to make directry in cuurent location so opencv can read imag easly and dont shoe error

live_img = cv.imread("ss.png",cv.IMREAD_UNCHANGED)#let opencv to read image from where we want to find object
obj = cv.imread("setting_btn.png",cv.IMREAD_UNCHANGED)#let opencv to read obj we want to find in main imag


result = cv.matchTemplate(live_img , obj ,cv.TM_CCOEFF_NORMED)#allow cv to match thos images.and will return matrix of imag

#cv.imwrite('result_CCOEFF_NORMED.png', result * 255)#make new imag which will show black and white color more the whiter the spot in image most likly to be obj present on that spot

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)#for geting max and min value of new imag matrix.max value indicat the most probality of obj presented spot

print('Best match top left position: %s' % str(max_loc))
print('Best match confidence: %s' % max_val)


#------------------   code for making rectangl in detected spot ----------------------------
needle_w = obj.shape[1]
needle_h = obj.shape[0]

# Calculate the bottom right corner of the rectangle to draw
top_left = max_loc
bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

# Draw a rectangle on our screenshot to highlight where we found the needle.
# The line color can be set as an RGB tuple
l = cv.rectangle(live_img, top_left, bottom_right, 
                    color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)

cv.imwrite('detecd_spot.jpg', live_img)

x,y = max_loc
print(x,y)


