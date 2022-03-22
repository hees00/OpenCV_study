##Trackbar Image Blending App  

from configparser import Interpolation
from queue import Empty
import numpy as np
import cv2
import matplotlib.pyplot as plt
import time

def emptyFunction():
    pass

def main():
    
    path = "C:\\Users\\1p2h3\\Desktop\\openCV\\output\\"
    imgpath1 = path + "test.jpg"
    imgpath2 = path + "test2.jpg"
    
    img1 = cv2.imread(imgpath1,1)
    img2 = cv2.imread(imgpath2,1)
    
    img1Re = cv2.resize(img1,dsize=(500,500),interpolation=cv2.INTER_AREA)
    img2Re = cv2.resize(img2,dsize=(500,500),interpolation=cv2.INTER_AREA)

    output = cv2.addWeighted(img1Re,0.5,img2Re,0.5,0)
    
    windowName ="Transition Demo"
    cv2.namedWindow(windowName)
    
    cv2.createTrackbar('Alpha',windowName,0,10, emptyFunction)
    
    while(True):
        cv2.imshow(windowName,output)
        
        if cv2.waitKey(1)==27:
            break
        
        alpha = cv2.getTrackbarPos('Alpha',windowName)/10
        beta = 1 - alpha
        
        output = cv2.addWeighted(img1Re,alpha,img2Re,beta,0)
        
        print(alpha,beta)
    

    cv2.destroyAllWindows()
    
    #output=img1*alpha+img2*beta+gamma
    #alpha+beta = 1
    

    # titles= ['img1','img2','weighted addition']
    # images= [img1,img2,output]
    
    # for i in range(len(titles)):
    #     plt.subplot(1, len(titles), i+1)
    #     plt.imshow(images[i])
    #     plt.title(titles[i])
    #     plt.xticks([])
    #     plt.yticks([])
        
    # plt.show()


if __name__ == "__main__":
    main()