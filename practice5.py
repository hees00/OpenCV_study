##Mini Project: OpenCV BGR Palette with Trackbars

import cv2
import numpy as np

def emeptyFunction():
    pass

def main():
    img1=np.zeros((512,512,3),np.uint8)
    windowName='OpenCV BGR Color Palette'
    cv2.namedWindow(windowName)
    
    cv2.createTrackbar('B',windowName,0,255,emeptyFunction)
    cv2.createTrackbar('G',windowName,0,255,emeptyFunction)
    cv2.createTrackbar('R',windowName,0,255,emeptyFunction)
    
    while(True):
        cv2.imshow(windowName,img1)
        
        if cv2.waitKey(1) == 27: #esc버튼
            break

        #trackbar의 값을 각각  b,g,r값으로 넣어줌
        blue = cv2.getTrackbarPos('B',windowName)
        green = cv2.getTrackbarPos('G',windowName)
        red = cv2.getTrackbarPos('R',windowName)
        
        img1[:]= [blue,green,red]
        print(blue,green,red)
        
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()