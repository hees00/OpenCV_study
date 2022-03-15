#matplotlib--custom library - 데이터 시각화 라이브러리
# ggplot도 있음
# matplotlib.pyplot은 matlab과 비슷하세 동작

import cv2
import matplotlib.pyplot as plt

def main():

    imgpath = "C:\\Users\\User\\Desktop\\misc\\4.1.04.tiff"
    img = cv2.imread(imgpath,0)

    #이미지 표시
    plt.imshow(img, cmap='gray')
    plt.title('gray Colormap')
    #눈금표시
    plt.xticks([])
    plt.yticks([])
    plt.show()

    plt.imshow(img)
    plt.title('default Colormap')
    plt.xticks([ ])
    plt.yticks([ ])
    plt.show()

if __name__ == "__main__":
    main()