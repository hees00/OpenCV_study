
## Logical Operations on Images

# bitwise logical operations
# not
# and
# or
# x-or


import cv2
import matplotlib.pyplot as plt

def main():

    # path = "C:\\Users\\1p2h3\\Desktop\\openCV\\output\\"
    # imgpath1 = path + "test.jpg"

    path = "C:\\Users\\User\\Desktop\\misc\\"
    imgpath1 = path + "4.2.01.tiff"
    imgpath2 = path + "4.1.04.tiff"
    
    img1 = cv2.imread(imgpath1,1)
    img2 = cv2.imread(imgpath2,1)

    img1 = cv2.resize(img1, dsize=(100, 100))
    img2 = cv2.resize(img2, dsize=(100, 100))


    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

    img3 = cv2.bitwise_not(img1)
    img4 = cv2.bitwise_and(img1,img2)
    img5 = cv2.bitwise_or(img1,img2)
    img6 = cv2.bitwise_xor(img1,img2)



    titles=['img1','img2','img not','and','or','xor']
    images=[img1,img2,img3,img4,img5,img6]

    for i in range(6):
        plt.subplot(2, 3, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()

if __name__ == "__main__":
    main()
    

##Rotation Effect on live Webcam Feed 

import cv2
import time

def main():
    # path = "C:\\Users\\1p2h3\\Desktop\\openCV\\output\\"
    # imgpath1 = path + "test.jpg"
    # img1 =cv2.imread(imgpath1,1)
    # img1 = cv2.resize(img1,dsize=(500,500),interpolation=cv2.INTER_AREA)

    windowName="live video"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret= False
        
    rows,columns,channels = frame.shape
    
    angle = 0
    scale = 0.1
    
    while True:
        
        ret,frame = cap.read()
        
        if angle == 360:
            angle = 0
        if scale <2:
            scale = scale + 0.1
        if scale >=2:
            scale = 0.1
            
        R = cv2.getRotationMatrix2D((columns/2,rows/2),angle,scale)
    
        print(R)
    
        output = cv2.warpAffine(frame,R,(columns,rows))
    
        cv2.imshow(windowName,output)
        # angle = angle+1
        time.sleep(0.01)

        if cv2.waitKey(1) ==27:
            break
    
    cv2.destroyWindow(windowName)
        
if __name__ == "__main__":
    main()

