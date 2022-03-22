##Arithmetic Operations on Images 
#7m22

# Images <--> numbers

# addition +
# subtraction - 
# division /
# multiplication *

from ast import Sub
from turtle import title
import cv2
import matplotlib.pyplot as plt

def main():
    
    path = "C:\\Users\\1p2h3\\Desktop\\openCV\\output\\"
    imgpath1 = path + "test.jpg"
    imgpath2 = path + "test2.jpg"
    
    img1 = cv2.imread(imgpath1,1)
    img2 = cv2.imread(imgpath2,1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    add= img1 + 50
    
    sub1= img1 - 50
    sub2= 50 - img1
    mult=img1 * 2
    div=img1 / 2
    
    # titles = ['image title1','image title2','add','sub','sub2']
    titles= ['img1','img2','mult','div']
    images= [img1,img2,mult,div]
    
    for i in range(len(titles)):
        plt.subplot(1, len(titles), i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()


if __name__ == "__main__":
    main()