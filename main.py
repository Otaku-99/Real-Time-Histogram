from cv2 import COLOR_BGR2GRAY
import numpy as np
import cv2
import matplotlib.pyplot as plt

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    channel = int(input(" Enter the channel number : "))
    while(cap.isOpened()):
        _,frame = cap.read()
        
        if(channel == 1):

            # frame.ravel() convert multi-dimension into 1 dimension
            plt.hist(frame.ravel(),256,[0,256],color='y')
            plt.draw()
            plt.pause(0.5) 
            plt.clf()
            cv2.imshow("original ",frame)

        elif(channel == 2):
            B,G,R = cv2.split(frame)
            zeros = np.zeros(frame.shape[:2], dtype="uint8")
            Red = cv2.merge([zeros, zeros, R])
            Green =  cv2.merge([zeros, G, zeros])
            Blue = cv2.merge([B, zeros, zeros])

            blue_hist = cv2.calcHist([frame], [0], None, [256], [0, 255])
            green_hist = cv2.calcHist([frame], [1], None, [256], [0, 255])
            red_hist = cv2.calcHist([frame], [2], None, [256], [0, 255]) 
            plt.subplot(3, 1, 1)  
            plt.hist(blue_hist,256,[0,256],color='b')
            plt.subplot(3, 1, 2)
            plt.hist(green_hist,256,[0,256],color='g')
            plt.subplot(3, 1, 3)
            plt.hist(red_hist,256,[0,256],color='r')
            plt.draw()
            plt.pause(0.5)
            plt.clf()
            
            cv2.imshow("Blue",Blue)
            cv2.imshow("Green",Green)
            cv2.imshow("Red",Red)
        else:
            print(" no channel selected")
            break
            
        # To visualize for each individual 
        
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
    cap.release() 