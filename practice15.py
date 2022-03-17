#video player
#동영상 재생하기

import cv2
import matplotlib.pyplot as plt

def main():

    windowName = "OpenCv Media Player"
    cv2.namedWindow(windowName)

    filename= "C:\\Users\\User\\Desktop\\ssu\\output\\out.avi"
    cap = cv2.VideoCapture(filename)

    ret = True
    while (cap.isOpened()):

        ret, frame = cap.read()
        print(ret)

        if ret:
            cv2.imshow(windowName,frame)

            #1000/framerate
            #오호 속도가 달라지는구먼
            if cv2.waitKey(33) == 27:
                break
        else:
            break

    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()