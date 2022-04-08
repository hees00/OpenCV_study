##Thresholding and basic Segmentation 

# segmentation - dividing the image into various regions

# thresholding  - cv2.threshole(img,th,max_val,algo)

import cv2
import matplotlib.pyplot as plt

def main():
    path = "C:\\Users\\1p2h3\\Desktop\\openCV\\output\\"
    imgpath1 = path + "test.jpg"
    img1 =cv2.imread(imgpath1,1)
    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
  
    
    th = 127
    max_val = 255
    
    ret,o1=cv2.threshold(img1,th,max_val,cv2.THRESH_BINARY)
    ret,o2=cv2.threshold(img1,th,max_val,cv2.THRESH_BINARY_INV)
    ret,o3=cv2.threshold(img1,th,max_val,cv2.THRESH_TOZERO)
    ret,o4=cv2.threshold(img1,th,max_val,cv2.THRESH_TOZERO_INV)
    ret,o5=cv2.threshold(img1,th,max_val,cv2.THRESH_TRUNC)
    
    ouput = [img1,o1,o2,o3,o4,o5]
    titles = ["original",'binary','binary inv','zero','zero inv','turnc']
    
    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.imshow(ouput[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
if __name__ == "__main__":
    main()