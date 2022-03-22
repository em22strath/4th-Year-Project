from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import threading
import sip
import settings
from PIL import ImageQt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

"""
THIS CODE WAS CREATED FOR THE RASPBERRY PI CAMERA
It uses the openCV library to capture frames from the camera and print them to a label in the GUI
"""

class piCamera():        
    def CameraRunningThreadStart(self,cameraLabel,sharpnessValueLabel):
        cameraThread = threading.Thread(target=self.CameraRunning, args = [cameraLabel,sharpnessValueLabel])
        cameraThread.start()
        
    def CameraRunning(self,cameraLabel,sharpnessValueLabel):
        camera = PiCamera()
        camera.rotation = 180
        camera.resolution = (600,400)
        rawCapture = PiRGBArray(camera)
        time.sleep(0.1)
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            image = frame.array
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            settings.storedSharpness = cv2.Laplacian(image, cv2.CV_64F).var()
            sharpnessValueLabel(settings.storedSharpness)
            imageDisplay = QtGui.QImage(image, image.shape[1], image.shape[0], QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(imageDisplay)
            cameraLabel(pixmap)
            rawCapture.truncate(0)
 
    def ImageCaptureThread(self, cameraLabel, fileDefinition):
        imageCaptureThread = threading.Thread(target=self.ImageCapture, args = [cameraLabel, fileDefinition])
        imageCaptureThread.start()
 
    def ImageCapture(self, cameraLabel, fileDefinition):
        capture = ImageQt.fromqpixmap(cameraLabel)
        userinput = fileDefinition
        capture.save(userinput + '.png')
    
    def TimelapseThread(self, timeValue, captureValue, cameraLabel, fileDefinition, timelapseRunLabel):
        timelapseThread = threading.Thread(target=self.Timelapse, args = [timeValue, captureValue, cameraLabel, fileDefinition, timelapseRunLabel])
        timelapseThread.daemon = True
        timelapseThread.start()
 
    def Timelapse(self, timeValue, captureValue, cameraLabel, fileDefinition, timelapseRunLabel):
        timestep = 0.001 * timeValue
        capturenumber = captureValue
        timelapseRunLabel("*Timelapse is running*")
        global counter
        counter = 0
        while counter < capturenumber:
            print('start')
            capture = ImageQt.fromqpixmap(cameraLabel)
            counter = counter + 1
            userinput = fileDefinition
            filename = userinput + str(counter) + '.png'
            capture.save(filename)
            time.sleep(timestep)
            print('end')
        timelapseRunLabel("")
            
    def TimelapseAbort(self, timelapseRunLabel):
        global counter
        counter = 10000
        timelapseRunLabel("")