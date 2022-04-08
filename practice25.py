<<<<<<< HEAD
# Shifting or Translation Operation in Images

# cv2.wrapSffine()

import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():

    # path = "C:\\Users\\1p2h3\\Desktop\\openCV\\output\\"
    # imgpath1 = path + "test.jpg"

    path = "C:\\Users\\User\\Desktop\\misc\\"
    imgpath1 = path + "4.2.01.tiff"

    img1 = cv2.imread(imgpath1 ,1)
    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

    rows,columns,channels = img1.shape
    T = np.float32([[1,0,150],[0,1,-50]])

    print(T)

    output = cv2.warpAffine(img1,T,(columns,rows))

    plt.imshow(output)
    plt.title('Shifted Image')
    plt.show()

=======
##Perspective Transform

#cv2.getAffineTransform() -> cv2.getPerspectiveTransform()

#cv2.warpAffine() -> cv2.warpPerspective()

# Scale
# rotation
# affine
# perspective

# point 3 -> 4

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    path = "C:\\Users\\1p2h3\\Desktop\\openCV\\output\\"
    imgpath1 = path + "test.jpg"
    img1 =cv2.imread(imgpath1,1)
    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
        
    rows,columns,channels = img1.shape
    
    point1 = np.float32([[0,0],[400,0],[0,400],[400,400]])
    point2 = np.float32([[0,0],[500,0],[0,500],[500,500]])

    P = cv2.getPerspectiveTransform(point1,point2)
    
    output = cv2.warpPerspective(img1,P,(300,300))
    
    plt.imshow(output)
    plt.title("chaged Perspective")
    plt.show()
        
>>>>>>> 2d3dca445508f9fda8b59719adc73b8b896b8565
if __name__ == "__main__":
    main()