import cv2



def main():
    cap1 = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture(1)

    if (cap1.isOpened() & cap2.isOpened()):
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        cut = 1
    elif (cap1.isOpened()):
        ret2 = False
        ret1 = True
        print("cap2 안켜짐")
    elif (cap2.isOpened()):
        ret1 = False
        ret2 = True
        print("cap1 안켜짐")
    else:
        ret2 = False
        ret1 = False
        print("둘 다 안켜짐")


    while (ret1 and ret2):
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        frame1 = cv2.resize(frame1, dsize=(500, 500), interpolation=cv2.INTER_AREA)
        frame2 = cv2.resize(frame2, dsize=(500, 500), interpolation=cv2.INTER_AREA)

        # cv2.namedWindow('1', cv2.WINDOW_NORMAL)
        cv2.imshow('1',frame1)
        # cv2.namedWindow('2', cv2.WINDOW_NORMAL)
        cv2.imshow('2',frame2)

        frame1 = cv2.resize(frame1,dsize=(500,500),interpolation=cv2.INTER_AREA)
        frame2 = cv2.resize(frame2,dsize=(500,500),interpolation=cv2.INTER_AREA)


        #붙일 사진
        imgs = [frame1,frame2]

        # 스티칭 객체 생성
        stitcher = cv2.createStitcher()

        # 이미지 스티칭
        status, result = stitcher.stitch(imgs)
        # print(stitcher.estimator())

        if status == cv2.Stitcher_OK:
            # cv2.namedWindow('output', cv2.WINDOW_NORMAL)
            cv2.imshow('ouput',result)
            cv2.waitKey()
            cv2.destroyAllWindows()
        else :
            print(status)
            break

    cap1.release()
    cap2.release()


if __name__ == "__main__":
    main()