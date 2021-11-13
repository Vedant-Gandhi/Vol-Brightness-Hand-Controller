import cv2 as cv
import mediapipe as mp
import time;


#Provides functionalities that help in hand detection and tracking
class HandTracker:
    def __init__(self):
        #The module that provides the hand detection
        self.hand_module=mp.solutions.hands

        #Instance of hand detector and tracker
        self.mp_hand_processor=self.hand_module.Hands()

    
    #Detects the hand coordinates and returns a list of x ad y coordinates at every point 
    def detect_hand_coords(self,image):

        width,height=image.shape[1],image.shape[0]
        detection=self.mp_hand_processor.process(image)

        coords_tuple=[]

        if detection.multi_hand_landmarks:

            for landmark in detection.multi_hand_landmarks:

                for coord in landmark.landmark:

                    coords_tuple.append([int(coord.x*width),int(coord.y*height)])

        return coords_tuple
        
    #Detects and mark the hand in the frame
    def mark_detections(self,image):
        detection=self.mp_hand_processor.process(image)

        if detection.multi_hand_landmarks:

            for landmark in detection.multi_hand_landmarks:

                mp.solutions.drawing_utils.draw_landmarks(image,landmark,self.hand_module.HAND_CONNECTIONS)
            
        return image


def main():    
    vidCapture=cv.VideoCapture(0)
    handDetector=HandTracker()
    windowName="Live Detection"

    def getFps(frameCount=1,lastTime=0):
        currentTime=time.time()
        return (frameCount/(currentTime-lastTime),currentTime)

    lastTime=0
    while True:
        success,frame=vidCapture.read()
        if  success:
            frame=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
            handDetector.mark_detections(frame)
            currentFPS=getFps(lastTime=lastTime)
            lastTime=currentFPS[1]
            frame=cv.flip(frame,1)
            cv.putText(frame,str(int(currentFPS[0])),(10,70),cv.FONT_HERSHEY_TRIPLEX,1,(0,0,0),3,cv.LINE_8)
            cv.imshow(windowName,frame)
            cv.waitKey(1)
            if cv.getWindowProperty(windowName, cv.WND_PROP_VISIBLE) <1:
                break
        else:
            print("Unable to fetch video frame.Crashed")
            break

if __name__ == 'main':
    main()