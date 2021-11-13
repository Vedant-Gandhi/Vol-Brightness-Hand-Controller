import time
import subprocess
import screen_brightness_control as sbc

#Global variable to store the last time FPS was calculated
FPS_last_time=0


def calculateFPS(total_frames=1,last_fps_time=0):
    #Returns the fps

    #Paramters:

    #    total_frames (int):The total frames displayed in the time period
    #    last_fps_time (int):Sets the time as the last fps time for global variable.Works only during the first call

     #Returns:
    #    reverse(int):The calculate fps  
    global FPS_last_time

    if not FPS_last_time:
        FPS_last_time=last_fps_time

    current_time=time.time()

    fps=total_frames/(current_time-FPS_last_time)

    FPS_last_time=current_time
    return int(fps)


def change_volume(level):

    #Paramters:

    #    level (int):The level of the volume to set

     #Returns:
    #    None
    if level >=0 and level <=100:
        subprocess.call(['amixer','-D','pulse','sset','Master',f'{level}%'])


def change_brightness(level):
    #Paramters:

    #    level (int):The level of the brightness to set

     #Returns:
    #    None
    if level >=0 and level <=100:
       sbc.set_brightness(level)

