#it is used to control mouse and keyboard automaticaly can also use to find object on scrren

import pyautogui

##(((((((((((((((            genral function        )))))))))))))))-----------------------

'''print(pyautogui.size())#return screen resolution
print(pyautogui.position())#return currunt  position of mouse cursor
print(pyautogui.onScreen(1,6))#it will tel is given resolution is in screen resolution or not
'''
#----------------------------------------------------------------------------------

##((((((((((((((((         mouse control func      ))))))))))))))))))------------------------
#             grnral perameter   (x,y,speed)
#pyautogui.moveTo(100,300,3)#move the cursor to the given coordinates
#pyautogui.moveRel(500,1000,3)#move cursor w.r.t current pos of cursor
#pyautogui.dragTo(100,200,1)#(x,y,speed) it will click and start moving to given cordinat.and after work is done it will releas mouse 
#pyautogui.dragRel(100,345,2)#drag mnouse w.r.t current mouse pos
#pyautogui.click(0,0,button="left")#(x,y,left/right)
#pyautogui.doubleClick(345,123)#double click on given pos
#pyautogui.leftClick(124,324)#left click
#pyautogui.rightClick(454,108)#right click
#pyautogui.middleClick(234,321)
'''pyautogui.mouseDown(123,321)
pyautogui.moveTo(500,300,3)
pyautogui.mouseUp()'''

'''pyautogui.moveTo(1278, 435,1)
pyautogui.scroll(-5000)#scroll till "x" points scroll down-->-Ve no.   scroll up---->+ve no.
'''
'''
pyautogui.moveTo(1918, 448,1)
pyautogui.dragTo(1918, 100,1)
'''

#---------------------------------------------------------------------------------------


#(((((((((((((((((((( KeyBoarb      ))))))))))))))))))))
#pyautogui.write("hello")
#pyautogui.press("enter")#it will pres that keyboard key
#pyautogui.keyDown("ctrl")#it will keep pressing that key
#pyautogui.sleep(2)
#pyautogui.keyUp("a")#it will realse key which is being pressed
#pyautogui.hotkey("ctrl","a")#writte shortcut key

#NOTE:- skipd alert,confirm,promt,password function. i was not intrested

#(((((((((((((((((((((  Take ScreenShot    )))))))))))))))))))))

#pyautogui.screenshot("localdir.png")#to take ss on currunt directory
#pyautogui.screenshot("E:\programming\Py Venv\image work\photo\pic.png")#save image in given dir
pyautogui.screenshot("E:\programming\Py Venv\image work\photo\o2.png",region=(10,10,500,500))
#save ss on given diractory with given resolution (top , left, width ,height)

#NOTE:-skiping easing topic . not intresting..it actually move cursor in diffrent style

#(((((((((((((((  Finding loacation of element by giving pic)))))))))))))))
#res = pyautogui.locateOnScreen("setting_btn.PNG")

#res = pyautogui.locateCenterOnScreen("setting_btn.PNG")#give coordinate of image
pyautogui.moveTo(725,206)