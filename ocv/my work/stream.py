#import cv2 as cv
import numpy as np
#from time import time
import win32ui , win32gui , win32con


class window_handling:
    #properties
    w = 0
    h = 0
    hwnd = None

    #constructor
    def __init__(self,window_name):# , window_name):
        self.w = 1920
        self.h = 1080
        self.hwnd = win32gui.FindWindow(None ,window_name)# "opencv_tutorials/004_window_capture/windowcapture.py at master · learncodebygaming/opencv_tutorials - Google Chrome"
        if not self.hwnd:
            raise Exception(f"Window Not Found:{window_name}")
        

    def screenshot(self):#self is used so we can acsess varibel present outside the def function but inside the class

        wDC = win32gui.GetWindowDC(self.hwnd)#hwnd
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj , self.w , self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0) , (self.w,self.h) , dcObj , (0,0) , win32con.SRCCOPY)
        
        #dataBitMap.SaveBitmapFile(cDC , "ss.bmp")
        signedIntsArray = dataBitMap.GetBitmapBits(True) 
        img = np.fromstring(signedIntsArray , dtype = "uint8")
        img.shape = (self.h , self.w , 4)
        #free resourse
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd , wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
        img = img[...,:3]
        img  = np.ascontiguousarray(img)

        return img
    def all_wind_name():
        def winEnumHandler( hwnd, ctx ):
            if win32gui.IsWindowVisible( hwnd ):
                print ( hex( hwnd ), win32gui.GetWindowText( hwnd ) )

        return win32gui.EnumWindows( winEnumHandler, None )


