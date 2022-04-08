<<<<<<< HEAD
## Computing Negative of an Image   
=======
##Rotating an Imag

# cv2.warpAffine()
# cv2.getRotationMatrix2D()
>>>>>>> 2d3dca445508f9fda8b59719adc73b8b896b8565

import cv2
import matplotlib.pyplot as plt

def main():
<<<<<<< HEAD

    # path = "C:\\Users\\1p2h3\\Desktop\\openCV\\output\\"
    # imgpath1 = path + "test.jpg"

    path = "C:\\Users\\User\\Desktop\\misc\\"
    imgpath1 = path + "4.2.06.tiff"
    
    img=cv2.imread(imgpath1,1)
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img3 = abs(255-img1)
    img4 = abs(255 - img2)


    titles=['color','grayscale','color negative','grayscale-nagative']
    images=[img1,img2,img3,img4]
    
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
    plt.imshow(images[2])
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
    
=======
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
>>>>>>> 2d3dca445508f9fda8b59719adc73b8b896b8565
