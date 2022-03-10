##-----images, Numbers, and NumPy-----##

import cv2
import numpy as np

def main():

    imgpath = "C:\\Users\\User\\Desktop\\misc\\4.1.04.tiff"
    img = cv2.imread(imgpath)

    print(img.dtype)
    # uint8 - unsigned integer 8-bits

    print(img.shape)
    #(256, 256, 3) -> 3차원 행렬로 첫번째 값은 은 행(y) 두번째 값은 열(x)   마지막 값은 BGR-> 이미지 사이즈 256x256,

    print(img.ndim)
    #배열의 차원 수

    print(img.size)


    # cv2.imshow('Lena', img)
    # cv2.waitKey(0)
    # cv2.destroyWindow('Lena')

if __name__ == "__main__":
    main()

    #[125,137,226] = blue green red
    # [ [ [ 115   0  94 ]
    #     [ 103  61  27 ]
    #   [ 104  60  26 ]
    #     ...

    # Gray scale에서  0-black 256-white
