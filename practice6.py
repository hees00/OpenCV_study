
import cv2
import numpy as np


windowName = 'Drawing'
img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow(windowName)

def draw_circle(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),40,(0,255,0),-1)
    if event == cv2.EVENT_MBUTTONDOWN:
        cv2.circle(img,(x,y),20,(0,255,255),-1)
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),20,(255,0,0),-1)
        
cv2.setMouseCallback(windowName, draw_circle)

def main():
    ##이벤트 종류 확인
    # events = [i for i in dir(cv2) if 'EVENT' in i]
    # print(events)
    
    while(True):
        cv2.imshow(windowName,img)
        if cv2.waitKey(20) == 27:
            break
    
    cv2.destroyAllWindows()
    
if __name__=="__main__":
    main()