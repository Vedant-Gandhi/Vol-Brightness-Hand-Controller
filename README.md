# Vol-Brightness-Hand-Controller

This project is created in python with an aim of controlling the system volume and brightness using hand motion.

When the index finger and thumb are moving in vertical direction the brightness changes and when they are moving in horizontal direction it changes the volume.

It is very exiciting project for image processing.It uses various libraries such as OpenCV,MediaPipe,etc.

# Files
1. main.py - Run this file to start the controller.
2. utils.py - Provides the utility functions for misc tasks.
3. HandTracker.py - Provides the module for providing the hand tracking and detection.

# Issues
1. The values are sensitive to hand movement.So it sometimes misinterprets between calculation for vertical motion and horizontal motion.
2. The FPS drops very low on CPU which needs to be enhanced.
3. Finding some good module for volume control on cross platform.
4. Currently volume works only on Linux.Needs to be activated for other platforms too.Volume will not work on Windows and working on MacOS is not determined.

# Tested on Manjaro Linux with Linux Kernel 5.10

Tune in with different values for constant threshold and finger distances for changing the accuracy and sensitivity.
