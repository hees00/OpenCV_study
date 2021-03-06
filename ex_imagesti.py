#이미지 여러장 stitching


import numpy as np
import cv2


def im_move(img, x, y):
    h, w = img.shape[:-1]
    M = np.float32([[1, 0, x], [0, 1, y]])
    result = cv2.warpAffine(img, M, (w, h))
    cv2.imshow('a', result)
    return result


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


grayA = cv2.cvtColor(img_lu, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(img_ru, cv2.COLOR_BGR2GRAY)
grayC = cv2.cvtColor(img_ld, cv2.COLOR_BGR2GRAY)
grayD = cv2.cvtColor(img_rd, cv2.COLOR_BGR2GRAY)


sift = cv2.xfeatures2d.SIFT_create()
kpA, desA = sift.detectAndCompute(grayA, None)
kpB, desB = sift.detectAndCompute(grayB, None)
kpC, desC = sift.detectAndCompute(grayC, None)
kpD, desD = sift.detectAndCompute(grayD, None)

bf = cv2.BFMatcher_create()
matches_luru = bf.match(desA, desB)
matches_luld = bf.match(desA, desC)
matches_lurd = bf.match(desA, desD)


sorted_matches_1 = sorted(matches_luru, key=lambda x: x.distance)
sorted_matches_2 = sorted(matches_luld, key=lambda x: x.distance)
sorted_matches_3 = sorted(matches_lurd, key=lambda x: x.distance)


#왼쪽위 오른쪽 매칭 호모그래피 찾기
res_luru = cv2.drawMatches(img_lu, kpA, img_ru, kpB, sorted_matches_1[ :30 ], None, flags=2)
src_luru = np.float32([ kpA[ m.queryIdx ].pt for m in sorted_matches_1 ]).reshape((-1, 1, 2))
dst_luru = np.float32([ kpB[ m.trainIdx ].pt for m in sorted_matches_1 ]).reshape((-1, 1, 2))

H_luru, status = cv2.findHomography(dst_luru, src_luru, cv2.RANSAC, 5.0)
print(H_luru)
cv2.imshow('match', res_luru)


#왼쪽위 왼쪽 아래 호모그래피 찾기
res_luld = cv2.drawMatches(img_lu, kpA, img_ld, kpC, sorted_matches_2[ :30 ], None, flags=2)
src_luld = np.float32([ kpA[ m.queryIdx ].pt for m in sorted_matches_2 ]).reshape((-1, 1, 2))
dst_luld = np.float32([ kpC[ m.trainIdx ].pt for m in sorted_matches_2 ]).reshape((-1, 1, 2))

H_luld, status = cv2.findHomography(dst_luld, src_luld, cv2.RANSAC, 5.0)
print(H_luld)
cv2.imshow('match', H_luld)

#왼쪽위 오른쪽 아래 호모그래피 찾기
res_lurd = cv2.drawMatches(img_lu, kpA, img_rd, kpD, sorted_matches_3[ :10], None, flags=2)
src_lurd = np.float32([ kpA[ m.queryIdx ].pt for m in sorted_matches_3 ]).reshape((-1, 1, 2))
dst_lurd = np.float32([ kpD[ m.trainIdx ].pt for m in sorted_matches_3 ]).reshape((-1, 1, 2))

H_lurd, status = cv2.findHomography(dst_lurd, src_lurd, cv2.RANSAC, 5.0)
print(H_lurd)
cv2.imshow('match', res_lurd)



result3 = cv2.warpPerspective(img_ru, H_luru, (img_lu.shape[1] + img_lu.shape[1], img_ru.shape[0]+img_ru.shape[0]))
re4 = cv2.warpPerspective(img_ld, H_luld,(img_lu.shape[1] + img_lu.shape[1], img_ru.shape[0]+img_ru.shape[0]))
re5 = cv2.warpPerspective(img_rd,H_lurd,(img_lu.shape[1] + img_lu.shape[1], img_ru.shape[0]+img_ru.shape[0]))
# result3[0 : img_lu.shape[0], 0 : img_lu.shape[1]] = img_lu
# result3 = cv2.addWeighted(result3, 0.5, re4, 0.5, 0)
# result3 = cv2.addWeighted(result3, 0.5, re5, 0.5, 0)
cv2.imshow('result3', re5)
cv2.waitKey()




