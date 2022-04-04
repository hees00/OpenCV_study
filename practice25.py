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
        
if __name__ == "__main__":
    main()