<<<<<<< HEAD
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
    
=======
##Affine Transformations

#cv2.getAffineTransform()
#cv2.warpAffine()

# point 1 ->o1
# 2 -> o2
# 3 -> o3


import cv2
import time
import numpy as np
import matplotlib.pyplot as plt

def main():
    path = "C:\\Users\\1p2h3\\Desktop\\openCV\\output\\"
    imgpath1 = path + "test.jpg"
    img1 =cv2.imread(imgpath1,1)
    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
        
    rows,columns,channels = img1.shape
    
    point1 = np.float32([[100,100],[300,100],[100,300]])
    point2 = np.float32([[200,150],[400,150],[400,300]]) 

    A = cv2.getAffineTransform(point1,point2)
    
    output = cv2.warpAffine(img1,A,(columns,rows))
    
    plt.imshow(output)
    plt.title("transformed Image")
    plt.show()
        
if __name__ == "__main__":
    main()
>>>>>>> 2d3dca445508f9fda8b59719adc73b8b896b8565
