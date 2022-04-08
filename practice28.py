##Adaptive Thresholding  

import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "C:\\Users\\1p2h3\\Desktop\\openCV\\output\\"
    imgpath1 = path + "test.jpg"
    img1 =cv2.imread(imgpath1,0)
    # img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
  
   #11 -> 23 -> 73
    block_size = 513
    constant = 2
    th1=cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,block_size,constant)
    th2=cv2.adaptiveThreshold(img1,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,block_size,constant)

    ouput = [img1,th1,th2]
    titles = ["original",'Mean Adaptive','gaussian adaptive']
    
    for i in range(3):
        plt.subplot(2,3,i+1)
        plt.imshow(ouput[i],cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
if __name__ == "__main__":
    main()