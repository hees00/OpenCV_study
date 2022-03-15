import cv2

def main():

    # imgpath = "C:\\Users\\User\\Desktop\\misc\\4.1.04.tiff"
    imgpath = "C:\\Users\\1p2h3\\Desktop\\openCV\\photo\\bingsu.tiff"
    img = cv2.imread(imgpath)

    cv2.namedWindow('Lena',cv2.WINDOW_AUTOSIZE)
    ##cv2.imshow('윈도우 이름', 이미지) 윈도우 창에 이미지 보여줌
    cv2.imshow('Lena', img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')

    # 추가) 창관리 메소드
    # cv2.movewWindow('윈도우이름',x좌표,y좌표)  # 창 위치 변경
    # cv2.resizeWindow('윈도우 이름', 100, 100)   # 창 크기 변경
    # cv2.destroyAllWindows()  # 모든 창 닫기

    #그외에도 마우스처리나 키보드 처리 가능능

if __name__ == "__main__":
    main()