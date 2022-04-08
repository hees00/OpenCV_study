import cv2


# path = "C:\\Users\\1p2h3\\Desktop\\openCV\\output\\"
# # # imgpath1 = path + "test1.jpg"
# # # imgpath2 = path + "test2.jpg"

path = "C:\\Users\\User\\Desktop\\ssu\\photo\\"
imgpath1 = path + "test1.jpg"
imgpath2 = path + "test2.jpg"
img1 =cv2.imread(imgpath1,1)
img2 =cv2.imread(imgpath2,1)

cv2.namedWindow('1', cv2.WINDOW_NORMAL)
cv2.imshow('1',img1)
cv2.namedWindow('2', cv2.WINDOW_NORMAL)
cv2.imshow('2',img2)

img1 = cv2.resize(img1,dsize=(500,500),interpolation=cv2.INTER_AREA)
img2 = cv2.resize(img2,dsize=(500,500),interpolation=cv2.INTER_AREA)


#붙일 사진
imgs = [img1,img2]

# 스티칭 객체 생성
stitcher = cv2.Stitcher_create()

# 이미지 스티칭
status, result = stitcher.stitch(imgs)
print(stitcher.estimator())

if status == cv2.Stitcher_OK:
    cv2.namedWindow('output', cv2.WINDOW_NORMAL)
    cv2.imshow('ouput',result)
    cv2.waitKey()
    cv2.destroyAllWindows()
else :
    print(status)