## Scaling Operation on an Image

# cv2.resize(img1, None,fx=1,fy=1,interpolaton = cv2.LINEAR)


# interpolaton method - 이거에 따라 픽셀 수, 속도,화질 달라지는 듯
# INTER_LINEAR
# INTER_NEAREST
# INTER_AREA - shrinking
# INTER_CUBIC - zooming 4x4
# INTER_LANCZ0S4 8x8

# scaling / resizing = shrinking(scaling down)/zooming (scaling up)



import cv2
import matplotlib.pyplot as plt

def main():

    # path = "C:\\Users\\1p2h3\\Desktop\\openCV\\output\\"
    # imgpath1 = path + "test.jpg"

    path = "C:\\Users\\User\\Desktop\\misc\\"
    imgpath1 = path + "4.2.01.tiff"
    
    img1 = cv2.imread(imgpath1,1)
    
    output =  cv2.resize(img1, None,fx=0.5,fy=1.5,interpolation = cv2.INTER_AREA)

    cv2.imshow('OUTPUT',output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
    
