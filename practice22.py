##Rotating an Imag

# cv2.warpAffine()
# cv2.getRotationMatrix2D()

import cv2
import matplotlib.pyplot as plt

def main():
    path = "C:\\Users\\1p2h3\\Desktop\\openCV\\output\\"
    imgpath1 = path + "test.jpg"
    img1 =cv2.imread(imgpath1,1)
    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    
    rows,columns,channels = img1.shape
    
    R = cv2.getRotationMatrix2D((columns/2,rows/2),0,0.5)
    
    print(R)
    
    output = cv2.warpAffine(img1,R,(columns,rows))
    
    plt.imshow(output)
    plt.title("ratated image")
    plt.show()
    
if __name__ == "__main__":
    main()