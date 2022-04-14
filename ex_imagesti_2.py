#이미지 여러장 stitching
#첫번째 네번째 이미지 겹치는 부분이 적을 경우
#이미지 경계 없도록 붙이는 중


import numpy as np
import cv2


def im_move(img, x, y):
    h, w = img.shape[:-1]
    M = np.float32([[1, 0, x], [0, 1, y]])
    result = cv2.warpAffine(img, M, (w, h))
    cv2.imshow('a', result)
    return result


## warpPerspective 될 이미지가 img2
def  matchNhomo(img1,img2):
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(gray1, None)
    kp2, des2 = sift.detectAndCompute(gray2, None)

    bf = cv2.BFMatcher_create()
    matches = bf.match(des1, des2)
    sorted_matches = sorted(matches, key=lambda x: x.distance)

    res = cv2.drawMatches(img1, kp1, img2, kp2, sorted_matches[ :30 ], None, flags=2)
    src = np.float32([ kp1[ m.queryIdx ].pt for m in sorted_matches ]).reshape((-1, 1, 2))
    dst = np.float32([ kp2[ m.trainIdx ].pt for m in sorted_matches ]).reshape((-1, 1, 2))

    H, status = cv2.findHomography(dst, src, cv2.RANSAC, 5.0)
    print(H)
    # cv2.imshow('match', res)

    return H

def subImage(img1,img2):
    img1_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # diff = cv2.absdiff(img1_gray,img2_gray)
    diff = cv2.subtract(img1_gray, img2_gray)

    a,diff_hm= cv2.threshold(diff,60,255,cv2.THRESH_BINARY)
    diff_hm = cv2.bitwise_not(diff_hm)

    # cv2.imshow('이미지 빼기', diff)
    diff_hm = cv2.bitwise_not(diff_hm)
    res = cv2.bitwise_and(img1,img1,mask=diff_hm)

    cv2.imshow('sub', diff)
    cv2.imshow('mask',diff_hm)
    cv2.imshow('subcolor', res)
    return res



path = "C:\\Users\\User\\Desktop\\ssu\\photo\\"
imgpath_lu = path + "lu.jpg"
imgpath_ru = path + "ru.jpg"
imgpath_ld = path + "ld.jpg"
imgpath_rd= path + "rd.jpg"

img_lu =cv2.imread(imgpath_lu,1)
img_ru =cv2.imread(imgpath_ru,1)
img_ld =cv2.imread(imgpath_ld,1)
img_rd =cv2.imread(imgpath_rd,1)


img_lu = cv2.resize(img_lu,dsize=(500,500),interpolation=cv2.INTER_AREA)
img_ru = cv2.resize(img_ru,dsize=(500,500),interpolation=cv2.INTER_AREA)
img_ld = cv2.resize(img_ld,dsize=(500,500),interpolation=cv2.INTER_AREA)
img_rd = cv2.resize(img_rd,dsize=(500,500),interpolation=cv2.INTER_AREA)

H_luru = matchNhomo(img_lu,img_ru)
H_luld = matchNhomo(img_lu,img_ld)
H_lurd = matchNhomo(img_lu,img_rd)


result3 = cv2.warpPerspective(img_ru, H_luru, (img_lu.shape[1] + img_lu.shape[1], img_ru.shape[0]+img_ru.shape[0]))
re4 = cv2.warpPerspective(img_ld, H_luld,(img_lu.shape[1] + img_lu.shape[1], img_ru.shape[0]+img_ru.shape[0]))
H_ldrd = matchNhomo(re4,img_rd)
re5 = cv2.warpPerspective(img_rd, H_lurd,(img_lu.shape[1] + img_lu.shape[1], img_ru.shape[0]+img_ru.shape[0]))
result3[0 : img_lu.shape[0], 0 : img_lu.shape[1]] = img_lu
res4 = subImage(re4,result3)
result3 = cv2.add(result3,res4)
# result3 = cv2.addWeighted(result3, 0.5, re4, 0.5, 0)
# result3 = cv2.addWeighted(result3, 0.5, re4, 0.5, 0)
# result3 = cv2.addWeighted(result3, 0.5, re5, 0.5, 0)
cv2.imshow('result3', result3)
cv2.waitKey()



