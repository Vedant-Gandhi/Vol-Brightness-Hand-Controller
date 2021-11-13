import HandTracker as ht
import cv2 as cv2
import numpy as np
import utils


frameWidth,frameHeight=640,480 #The width and height of the frame being processed
min_constant_threshold=20  #The minimum constant threshold that must be there to determine of the motion is vertical or horizontal
max_finger_distance=150 #The maximum finger distance so that the max value of the feature is set
min_finger_distance=50 #The minimum finger distance so that the min value of the feature is set

vidCap=cv2.VideoCapture(0)

#Set the frame width and height
vidCap.set(3,frameWidth) 
vidCap.set(4,frameHeight)


hTracker=ht.HandTracker()

while True:

    frame_read_sucess,frame=vidCap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)


    landmark_detections=hTracker.detect_hand_coords(frame)
    hTracker.mark_detections(frame) #Mark the hand detections on frame

    if landmark_detections:
         x1,y1=landmark_detections[4][0],landmark_detections[4][1] # The tip of thumb
         x2,y2=landmark_detections[8][0],landmark_detections[8][1] # The tip of index finger
         
         x_dist=x1-x2  # The change in x
         y_dist=y1-y2 # The change in y

         distance=((x2-x1) ** 2 + (y2-y1) **2) ** 0.5 # The distance between two fingers


         mapped_number=np.interp(distance,[min_finger_distance,max_finger_distance],[0,100]) # Get the interpolation projected in the range i.e maps the number falling between min_finger_distance and max_finger_distance to fall in between 0 and 100

         #If the motion is vertical then change the brightness
         if x_dist < min_constant_threshold and (y_dist >min_finger_distance and y_dist < max_finger_distance):
              utils.change_brightness(mapped_number)

          # If the motion is horizontal change the volume
         elif  y_dist < min_constant_threshold and (x_dist >min_finger_distance and x_dist < max_finger_distance):
              utils.change_volume(mapped_number)



   # Calculate the FPS
    fps=utils.calculateFPS()
    cv2.putText(frame,"FPS:"+str(int(fps)),(10,70),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),3)
    cv2.imshow("Vol Increase",frame)
    cv2.waitKey(1)
    if cv2.getWindowProperty("Vol Increase", cv2.WND_PROP_VISIBLE) <1:
            break
     