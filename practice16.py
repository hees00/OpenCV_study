##object tracking by color

import cv2
import numpy as np
def main():
    
    cap = cv2.VideoCapture(0)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    
    while ret:
        ret,frame =cap.read()
        
        hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #h- 색상 s-채도 v-명도
        
        # #Blue
        # low = np.array([100,50,50])
        # high = np.array([140,255,255])
        
        # #Green
        # low = np.array([40,50,50])
        # high = np.array([80,255,255])
        
        #red
        low = np.array([140,50,50])
        high = np.array([180,255,255])

        # 범위내에 존재하면 그대로 아니면 0으로 반환
        image_mask = cv2.inRange(hsv,low,high)

        # 공통으로 겹치는 부분 출력
        output = cv2.bitwise_and(frame,frame, mask=image_mask)
        
        cv2.imshow("Image mask",image_mask)
        cv2.imshow("Original Webcam Feed",frame)
        cv2.imshow("color tracking",output)
        
        if cv2.waitKey(1) == 27:
            break
    
    cv2.destroyAllWindows()
    cap.release()
    
    
if __name__ == "__main__":
    main()