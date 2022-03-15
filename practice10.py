# COLOR_BGR2GRAY
# COLOR_BGR2HSV
# COLOR_BGR2RGB

import cv2

def main():
    j = 0
    for filename in dir(cv2):
        if filename.startswith('COLOR_'):
            print(filename)
            j=j+1

    print('There are'+ str((j+1))+'color coversion falgs in openCV')

if __name__=='__main__':
    main()