import cv2

def main():

    # imgpath = "C:\\Users\\User\\Desktop\\misc\\4.1.04.tiff"
    imgpath = "C:\\Users\\1p2h3\\Desktop\\openCV\\photo\\bingsu.tiff"
    img = cv2.imread(imgpath,0)
    ## flag- 옵션 1-color 0-Graysacale -1 - alphachannel까지 포함

    #저장할 파일 경로
    outpath="C:\\Users\\1p2h3\\Desktop\\openCV\\photo\\output.jpg"
    
    #이미지 저장
    cv2.imwrite(outpath, img)

    cv2.imshow('Lena', img)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')

    
    
    

if __name__ == "__main__":
    main()