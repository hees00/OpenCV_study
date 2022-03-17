#webcam image capture

import cv2
import matplotlib.pyplot as plt

def main():
    cap = cv2.VideoCapture(0)
    #0-default camera , 파일 경로쓰면 동영상 파일에서 읽을 수 있음

    if cap.isOpened():
        ret, frame = cap.read()
        print(ret)
        print(frame)
        img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    else:
        ret = False

    plt.imshow(img1)
    plt.title('webcam')
    plt.xticks([])
    plt.yticks([])
    plt.show()

    cap.release()

if __name__ == "__main__":
    main()