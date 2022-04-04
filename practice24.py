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