##Otsu's Binarization Thresholding   


import cv2
import matplotlib.pyplot as plt

def main():
    path = "C:\\Users\\1p2h3\\Desktop\\openCV\\output\\"
    imgpath1 = path + "4.1.04.jpg"
    img1 =cv2.imread(imgpath1,0)
    # img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
  
    
    th = 0
    max_val = 255
    
    ret,o1=cv2.threshold(img1,th,max_val,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    ret,o2=cv2.threshold(img1,th,max_val,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    ret,o3=cv2.threshold(img1,th,max_val,cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
    ret,o4=cv2.threshold(img1,th,max_val,cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)
    ret,o5=cv2.threshold(img1,th,max_val,cv2.THRESH_TRUNC + cv2.THRESH_OTSU)
    
    ouput = [img1,o1,o2,o3,o4,o5]
    titles = ["original",'binary','binary inv','zero','zero inv','turnc']
    
    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.imshow(ouput[i],cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
if __name__ == "__main__":
    main()