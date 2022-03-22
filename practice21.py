##Splitting and Merging channels of a color image  

# Color various channels
# Greyscale/B&W = single channel
# RGB/BGR
# HSV = Hue Saturation Value
# CMY = CYAN Magenta Yellow
# CMYK = CYAN Magenta Yellow Key

# cv2.split()
# cv2.merge()

import cv2
import matplotlib.pyplot as plt

def main():

    path = "C:\\Users\\1p2h3\\Desktop\\openCV\\output\\"
    imgpath1 = path + "test.jpg"
    
    img=cv2.imread(imgpath1,1)
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    r,g,b=cv2.split(img1)
    
    titles=['original Image','red','green','blue']
    images=[cv2.merge((r,g,b)),r,g,b]
    
    plt.subplot(2, 2, 1)
    plt.imshow(images[0])
    plt.title(titles[0])
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2, 2, 2)
    plt.imshow(images[1],cmap='gray')
    plt.title(titles[1])
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2, 2, 3)
    plt.imshow(images[2],cmap='gray')
    plt.title(titles[2])
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(2, 2, 4)
    plt.imshow(images[3],cmap='gray')
    plt.title(titles[3])
    plt.xticks([])
    plt.yticks([])
    
    plt.show()
    
    
if __name__ == "__main__":
    main()
    
