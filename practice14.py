#webcam video recording to a file

import cv2
import matplotlib.pyplot as plt

def main():

    windowName = "Live Video Feed Capture"
    cv2.namedWindow(windowName)

    cap = cv2.VideoCapture(0)

    filename= "C:\\Users\\User\\Desktop\\ssu\\output\\out.avi"
    codec = cv2.VideoWriter_fourcc('M','J','P','G')
    framerate = 30 #초당 저장될 frame
    resolution = (640,480) #사이즈

    VideoFileouput= cv2.VideoWriter(filename,codec,framerate,resolution)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while ret :
        ret,frame = cap.read()
        #이런식으로 변환 가능
        # frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        VideoFileouput.write(frame)

        cv2.imshow(windowName, frame)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    VideoFileouput.close()
    cap.release()

if __name__ == "__main__":
    main()