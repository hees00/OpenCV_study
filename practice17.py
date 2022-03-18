#Displaying Multiple Images with Matplotlib 

import cv2
import matplotlib.pyplot as plt

def main():
    
   
    
    path = "C:\\Users\\1p2h3\\Desktop\\openCV\\output\\"
    imgpath1 = path + "test.jpg"
    imgpath2 = path + "test2.jpg"
    
    img1 = cv2.imread(imgpath1,1)
    img2 = cv2.imread(imgpath2,1)

    #bgr을 rgb 배열로 바꿔줌
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    
    titles = ['image title1','image title2']
    images= [img1,img2]
    
    for i in range(2):
        plt.subplot(1, 2, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()


if __name__ == "__main__":
    main()