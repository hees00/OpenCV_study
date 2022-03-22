##Blending and transitioning Images 

#addWeighted()
#composite Arithmatic Operation


import numpy as np
import cv2
import matplotlib.pyplot as plt
import time

def main():
    
    path = "C:\\Users\\1p2h3\\Desktop\\openCV\\output\\"
    imgpath1 = path + "test.jpg"
    imgpath2 = path + "test2.jpg"
    
    img1_ = cv2.imread(imgpath1,1)
    img2_ = cv2.imread(imgpath2,1)
    img1 = cv2.cvtColor(img1_, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2_, cv2.COLOR_BGR2RGB)
    
    alpha =0.0
    beta=1.0
    gamma=0
    
    for i in np.linspace(0,1,10):
        alpha = i
        beta = 1 - alpha
        output = cv2.addWeighted(img1_,alpha,img2_,beta,gamma)
        cv2.imshow('Transition',output)
        time.sleep(0.25)
        if cv2.waitKey(1)==27:
            break

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