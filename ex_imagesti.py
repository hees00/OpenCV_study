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
img_rd= cv2.resize(img_rd,dsize=(500,500),interpolation=cv2.INTER_AREA)


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
print(H_luru)
cv2.imshow('match', H_luld)


# surf = cv2.xfeatures2d.SURF_create(400)
# kpsA, desA = surf.detectAndCompute(imageA, None)
# kpsB, desB = surf.detectAndCompute(imageB, None)
#
# bf = cv2.BFMatcher_create()
# matches = bf.knnMatch(desA, desB, k=2)
#
# good = []
# good_without_list = []
#
# for m, n in matches:
#     if m.distance < 0.4 * n.distance:
#         good.append([m])
#         good_without_list.append(m)
#
# np.random.shuffle(good)
# image_match = cv2.drawMatchesKnn(imageA, kpsA, imageB, kpsB, good[:10], flags=2, outImg=imageA)
#
# pts_x =  np.float32([ kpsA[ m.queryIdx ].pt for m in good_without_list ]).reshape((-1, 1, 2))
# pts_y = np.float32([ kpsB[ m.queryIdx ].pt for m in good_without_list ]).reshape((-1, 1, 2))
#
# H, status = cv2.findHomography(pts_x, pts_x, cv2.RANSAC, 5.0)
# print(H)
# cv2.imshow('match', image_match)
# cv2.waitKey()


result3 = cv2.warpPerspective(img_ru, H_luru, (img_lu.shape[1] + img_lu.shape[1], img_ru.shape[0]+img_ru.shape[0]))
re4 = cv2.warpPerspective(img_ld, H_luld,(img_lu.shape[1] + img_lu.shape[1], img_ru.shape[0]+img_ru.shape[0]))
result3[0 : img_lu.shape[0], 0 : img_lu.shape[1]] = img_lu
result3 = cv2.addWeighted(result3, 0.5, re4, 0.5, 0)
cv2.imshow('result3', result3)
cv2.waitKey()




