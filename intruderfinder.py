import os
import cv2
import numpy as np

def frame_difference(prev_frame, cur_frame, next_frame):

    diff_frames_1 = cv2.absdiff(next_frame,cur_frame)
    diff_frames_2=cv2.absdiff(cur_frame,prev_frame)

    return cv2.bitwise_and(diff_frames_1,diff_frames_2)

def get_frame(cap):
    _, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
##    (thresh, blackAndWhiteImage) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
##we can make canny with this(canny but have errors)
    return gray
#takes file name as string input and adds .jpg
raw=str(input("How should i name your file"))
raw=raw+".jpg" #adding .jpg
path = os.getcwd() #path of our program
if __name__=='__main__':

    cap = cv2.VideoCapture(0)

    prev_frame = get_frame(cap)

    cur_frame = get_frame(cap)

    next_frame = get_frame(cap)
while True:
    a=frame_difference(prev_frame,cur_frame, next_frame)
#    cv2.imshow('Object Movement',a)
    prev_frame = cur_frame
    cur_frame = next_frame
    sum1=int(np.sum(a)) 
    next_frame = get_frame(cap)
    key = cv2.waitKey(1)
    if key == 27:
        break
    if (sum1)>10000:
        cv2.imwrite(os.path.join(path , raw), prev_frame)
        print("Intruder Found")
    key = cv2.waitKey(1)
    if key == 27:
        break
