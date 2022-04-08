import numpy as np
import cv2

path = "C:\\Users\\User\\Desktop\\ssu\\photo\\"
imgpath1 = path + "lu.jpg"
imgpath2 = path + "ru.jpg"

imageA =cv2.imread(imgpath1,1)
imageB =cv2.imread(imgpath2,1)

imageA = cv2.resize(imageA,dsize=(500,500),interpolation=cv2.INTER_AREA)
imageB = cv2.resize(imageB,dsize=(500,500),interpolation=cv2.INTER_AREA)

grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

#특징점 검출 객체 생성
sift = cv2.xfeatures2d.SIFT_create()

#특징점 검출
kpA, desA = sift.detectAndCompute(grayA, None)
kpB, desB = sift.detectAndCompute(grayB, None)


#특징점 매칭
bf = cv2.BFMatcher_create()
matches = bf.match(desA, desB)
sorted_matches = sorted(matches, key=lambda x: x.distance)
res = cv2.drawMatches(imageA, kpA, imageB, kpB, sorted_matches[ :30 ], None, flags=2)

#hompgraphy 검출
src = np.float32([ kpA[ m.queryIdx ].pt for m in sorted_matches ]).reshape((-1, 1, 2))
dst = np.float32([ kpB[ m.trainIdx ].pt for m in sorted_matches ]).reshape((-1, 1, 2))
H, status = cv2.findHomography(dst, src, cv2.RANSAC, 5.0)


print(H)
cv2.imshow('match', res)
cv2.waitKey()


#합쳐주기
result3 = cv2.warpPerspective(imageB, H, (imageA.shape[1] + imageB.shape[1], imageA.shape[0]))
result3[0 : imageA.shape[0], 0 : imageA.shape[1]] = imageA
cv2.imshow('result3', result3)
cv2.waitKey()




