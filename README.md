# Intruder_Detector
Detect intruders with your webcam. 

Code is actually very raw.
So it's first of the first version EVER. 
-----------------------------------------------------------
-
-      CODE WILL BE UPDATED AND EXPLANATIONS WILL BE ADDED
-      
-----------------------------------------------------------      

###########################################################
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
! WRITE YOUR DESKTOP PATH or JUST THE USER NAME IN THE CODE
                        WHERE?
                          
! AT THE BOTTOM OF THE CODE THERE IS AN IF STATEMENT:
  if abs((sum1-sum2))>10000:
        cv2.imwrite(r'C:/Users/ !!!! /Desktop/intruder.png', prev_frame)     
            EITHER REPLACE !!!! WITH YOUR USERNAME
                        OR
            USE TOTALLY DIFFERENT PATH
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
############################################################                      

How it works?
It simply saves image if a certain amount of change happened in the webcam.



