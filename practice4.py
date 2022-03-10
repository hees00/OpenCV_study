##--Drawing Geometric Shapes--##

import cv2
import numpy as np

def main():
    brown=(8, 92, 165)
    # ##도형 그릴 캔버스 만들기
    # #numpy.zeros(shape,dtype)
    # img1 = np.zeros((512,512,3), np.uint8)
    #
    # ##선##
    # #cv2.line(이미지 파일,시작좌표,종료좌표,섹싱,선두께)
    # cv2.line(img1,(0,99),(99,0), (255,0,0), 2)
    #
    # # cv2.rectangle(이미지 파일,시작좌표,종료좌표,섹싱,선두께)
    # #선두께에 -1 주면 도형 안이 채워짐
    # cv2.rectangle(img1,(40,60),(80,70),(0,255,0),2)
    #
    # #cv2.circle(img, center, radian, color, thickness)
    # cv2.circle(img1, (60, 60), 10, (0, 0, 255), 1)
    #
    # #cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color[, thickness[, lineType[, shift]]])
    # #axes-중심에서 가장 먼거리와 짧은 거리, angle-타원의 기울기 각
    # #시작각도 끝나는 각도는 좌표평면 기준 반시계방향인듯
    # cv2.ellipse(img1, (160, 260),(50,20),0,0,360,(127, 127, 127), -1)
    #
    # ##다각형##
    # #cv2.polylines(img, pts, isClosed, color, thickness)
    # points = np.array([[80,2],[125,40],[179,19],[230,5],[30,50]],np.int32)
    # points = points.reshape((-1,1,2))
    # cv2.polylines(img1, [points], True, (0,255,255))
    #
    # text1 = 'Test Text'
    # cv2.putText(img1,text1,(100,100),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0))

    img2 = np.zeros((512, 512, 3), np.uint8)
    cv2.circle(img2, (256, 225), 60, brown, -1)
    cv2.circle(img2, (210, 180), 20, brown, -1)
    cv2.circle(img2, (302, 180), 20, brown, -1)

    points = np.array([[ 230, 275 ], [ 282, 305 ], [ 282, 275 ], [ 230, 305 ]], np.int32)
    points = points.reshape((-1,1,2))
    cv2.polylines(img2, [ points ], True, (0, 0, 255),5)
    cv2.putText(img2, "TeddyBear", (100, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, (256, 256, 256))


    cv2.imshow('Lena', img2)
    cv2.waitKey(0)
    cv2.destroyWindow('Lena')

if __name__ == "__main__":
    main()

