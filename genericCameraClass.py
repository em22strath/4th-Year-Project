# You may need to import more libraries depending on the camera you are using
import time
import threading
from PIL import ImageQt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

"""
THIS CODE WAS CREATED AS A TEMPLATE FOR ANY CAMERA TO BE USED IN THE MODULAR PROCESS
All of the function names and arguments fed into the functions must remain the same. The arguments fed in refer to the GUI, as detailed below:
'cameraLabel' - the picture label that the live feed of the camera is printed to
'fileDefinition' - the text input from the user stating the file name they would like to save under
'timeValue' - the value input for time interval for the timelapse
'captureValue' - the value input for the number of captures for the timelapse
'timelapseRunLabel' - the text label to show that a timelapse in progress
'sharpnessValueLabel' - for printing the sharpness value on screen
"""

"Change the name of the class to correspond with the camera used"
class genericCamera:
    
    "Thread for the camera to run"
    def CameraRunningThreadStart(self, cameraLabel, sharpnessValueLabel):
        cameraThread = threading.Thread(target=self.CameraRunning, args = [cameraLabel, sharpnessValueLabel])
        cameraThread.start()
    
    "Function for the camera to run and print the frames into the picture label in the GUI"
    def CameraRunning(self,cameraLabel, sharpnessValueLabel):
        # Write code here for your own camera
        # It should capture frames from the camera and print them to the picture label, whilst continually
        # updating to show a live feed from the camera embedded in the GUI
        # Every time a frame is captured, the sharpness value of the frame should be found and saved in settings.storedSharpness
        # It should then be printed in the sharpnessValueLabel to be displayed on the GUI
    
    "Thread for images to be captured"
    def ImageCaptureThread(self, cameraLabel, fileDefinition):
        imageCaptureThread = threading.Thread(target=self.ImageCapture, args = [cameraLabel, fileDefinition])
        imageCaptureThread.start()
 
    "Function for capturing images by calling the picture label and reading the file name to save this to"
    def ImageCapture(self, cameraLabel, fileDefinition):
        capture = ImageQt.fromqpixmap(cameraLabel)
        userinput = fileDefinition
        capture.save(userinput + '.png')
    
    "Thread for timelapse capture"
    def TimelapseThread(self, timeValue, captureValue, cameraLabel, fileDefinition, timelapseRunLabel):
        timelapseThread = threading.Thread(target=self.Timelapse, args = [timeValue, captureValue, cameraLabel, fileDefinition, timelapseRunLabel])
        timelapseThread.daemon = True
        timelapseThread.start()
 
    "Function for capturing a timelapse with the chosen capture number, time interval and file name to save this to"
    def Timelapse(self, timeValue, captureValue, cameraLabel, fileDefinition, timelapseRunLabel):
        timestep = 0.001 * timeValue
        capturenumber = captureValue
        timelapseRunLabel("*Timelapse is running*")
        global counter
        counter = 0
        while counter < capturenumber:
            capture = ImageQt.fromqpixmap(cameraLabel)
            counter = counter + 1
            userinput = fileDefinition
            filename = userinput + str(counter) + '.png'
            capture.save(filename)
            time.sleep(timestep)
        timelapseRunLabel("")
        
    "Function for cancelling timelapse after the button has been clicked"
    def TimelapseAbort(self, timelapseRunLabel):
        global counter
        counter = 10000
        timelapseRunLabel("")