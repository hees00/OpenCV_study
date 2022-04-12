import numpy as np
import cv2

# path = "C:\\Users\\User\\Desktop\\ssu\\photo\\"
# imgpath1 = path + "lu.jpg"
# imgpath2 = path + "ru.jpg"

def main():
    cap1 = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture(1)

    if (cap1.isOpened() & cap2.isOpened()):
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()
        cut = 1
    elif(cap1.isOpened()):
        ret2 = False
        print("cap2 안켜짐")
    elif(cap2.isOpened()):
        ret1 = False
        print("cap1 안켜짐")
    else:
        ret2 = False
        ret1 = False
        print("둘 다 안켜짐")



    while (ret1 & ret2):
        ret1, frame1 = cap1.read()
        ret2, frame2 = cap2.read()

        frame1 = cv2.resize(frame1, dsize=(500, 500), interpolation=cv2.INTER_AREA)
        frame2 = cv2.resize(frame2, dsize=(500, 500), interpolation=cv2.INTER_AREA)

        cv2.imshow("video1", frame1)
        cv2.imshow("video2", frame2)

        if cut == 1:
            gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

            surf = cv2.xfeatures2d.SURF_create(400)
            kpsA, desA = surf.detectAndCompute(gray1, None)
            kpsB, desB = surf.detectAndCompute(gray2, None)

            bf = cv2.BFMatcher_create()
            matches = bf.knnMatch(desA, desB, k=2)

            good = []
            good_without_list = []

            for m, n in matches:
                if m.distance < 0.4 * n.distance:
                    good.append([m])
                    good_without_list.append(m)

            np.random.shuffle(good)
            image_match = cv2.drawMatchesKnn(frame1, kpsA, frame2, kpsB, good[:30], flags=2, outImg=frame1)
            cv2.imshow('match', image_match)

            pts_x =  np.float32([ kpsA[m.queryIdx].pt for m in good_without_list]).reshape((-1, 1, 2))
            pts_y = np.float32([ kpsB[m.trainIdx].pt for m in good_without_list]).reshape((-1, 1, 2))

            H, status = cv2.findHomography(pts_y, pts_x, cv2.RANSAC, 5.0)
            print(H)
            cut = 0

        output = cv2.warpPerspective(frame2, H, (frame1.shape[1] + frame2.shape[1], frame1.shape[0]))
        output[ 0: frame1.shape[ 0 ], 0: frame1.shape[ 1 ]] = frame1

        cv2.imshow("output", output)

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    cap1.release()
    cap2.release()




if __name__ == "__main__":
    main()


