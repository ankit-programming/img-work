import cv2 as cv
import numpy as np
import os
import time
from windowcapture import WindowCapture
from vision import Vision
import pyautogui

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#WindowCapture.list_window_names()

# initialize the WindowCapture class
wincap = WindowCapture()#"Stock Market Jobs – Stock Market Online Job | REVADVERT - Google Chrome")

# initialize the object images
obj_serachBAR = Vision("search bar.png")
obj_serachBAR2 = Vision("search bar2.png")
obj_verify_Human = Vision("cloudflair.png")
obj_verify = Vision('verify.png')
obj_pls_wait = Vision('please wait...png')
obj_continue = Vision('continue.png')
obj_getlink = Vision('get link.png')
obj_close_chrome = Vision('x chrome.png')
obj_add_page = Vision("+ page.png")



loop_time = time.time()
while(True):    

    screenshot = wincap.get_screenshot()#take screanshot
    # display the processed image
    verify_points = obj_verify.find(screenshot, 0.5, 'rectangles',debug_mode="yes")
    obj_getlink_points = obj_getlink.find(screenshot, 0.5, 'rectangles',debug_mode="yes")
    obj_searchBAR_points = obj_serachBAR.find(screenshot , 0.5,"rectangles",debug_mode="yes")#, debug_mode="yes")
    obj_searchBAR2_points = obj_serachBAR2.find(screenshot , 0.5,"rectangles",debug_mode="yes")
    
    #https://gplinks.co/Oir0
    #working
    if obj_searchBAR_points:#or obj_searchBAR2_points :
        print("search bar detedted")
        ss_points = wincap.get_screen_position(obj_searchBAR_points[0])# or wincap.get_screen_position(obj_searchBAR2_points[0])
        print(ss_points)
        pyautogui.click(ss_points)
        pyautogui.write("https://gplinks.co/Oir0")
        pyautogui.press("enter")

    screenshot = wincap.get_screenshot()#take screanshot of new event
    obj_verify_Human_points = obj_verify_Human.find(screenshot,0.5,"rectangles",debug_mode="yes")#detect captcha
    if obj_verify_Human_points:#if captha found
        print("cloud flaer captcha detected")
        ss_points = wincap.get_screen_position(obj_verify_Human_points[0])#get position of captcha
        pyautogui.click(ss_points)#move coursor to  that captcha
        

    if verify_points:      #find verify button  
        print("     IN  VERIFY     ")
        #verify_points is a list but in its 0 element tuple is there and get_screen_position take input in tuple so we convert list into tuple
        ss_point = wincap.get_screen_position(verify_points[0])
        pyautogui.click(ss_point)
        pyautogui.move(3,50)

        screenshot = wincap.get_screenshot()#take new ss in which please wait button must show to run further code
        obj_pls_wait_points = obj_pls_wait.find(screenshot, 0.5, 'rectangles',debug_mode="yes")        
        if obj_pls_wait_points:
            print(f" IN   PLEASE WAIT   ")
            ss_point = wincap.get_screen_position(obj_pls_wait_points[0])
            pyautogui.moveTo(ss_point)

            while True:
                screenshot = wincap.get_screenshot()
                obj_continue_points = obj_continue.find(screenshot, 0.5, 'rectangles',debug_mode="yes")
                if obj_continue_points:                                        
                    print(f" IN  CONTINUE  ")
                    ss_point = wincap.get_screen_position(obj_continue_points[0])
                    pyautogui.click(ss_point)
                    break
                    #print(f" IN  CONTINUE  ")
                pyautogui.scroll(-200)
                

    if obj_getlink_points:
        print(f"   GET   LINK ")
        ss_point = wincap.get_screen_position(obj_getlink_points[0])
        pyautogui.click((ss_point))
        #to close open app usinf short cut ctrl + f4

        obj_add_page_points = obj_add_page.find(screenshot , 0.5 , "rectangles",debug_mode="yes")
        if obj_add_page_points:
            print("adding page")
            ss_point = wincap.get_screen_position(obj_add_page_points[0])
            pyautogui.click(ss_point)
            for i in range(1):
                obj_close_chrome_points = obj_close_chrome.find(screenshot, 0.5, 'rectangles',debug_mode="yes")
                if obj_close_chrome_points:
                    print(f" CLOSE TAB  X   ")
                    ss_point = wincap.get_screen_position(obj_close_chrome_points[0])
                    pyautogui.click(ss_point)
        



    # debug the loop rate
    print('FPS {}'.format(1 / (time.time() - loop_time)))
    loop_time = time.time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')



#NOTE:_ CLIKING
