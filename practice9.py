# colorspace-gray,bgr,rgb,hsv,cmy,cmyk

import cv2
import matplotlib.pyplot as plt

def main():

    imgpath = "C:\\Users\\User\\Desktop\\misc\\4.1.04.tiff"
    img = cv2.imread(imgpath,1)

    #bgr을 rgb 배열로 바꿔줌
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    #v2.imread -> BGR but plt.imshow -> rgb
    plt.imshow(img)
    plt.title('color image with bgr')
    plt.xticks([])
    plt.yticks([])
    plt.show()

    plt.imshow(img1)
    plt.title('color image with rgb')
    plt.xticks([ ])
    plt.yticks([ ])
    plt.show()

if __name__ == "__main__":
    main()