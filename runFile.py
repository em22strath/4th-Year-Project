from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import re
import importlib
import sys
import gc
import time
import runpy
from Ui_MainWindowClass import Ui_MainWindow
from setUpScreen import SelectionScreen_MainWindow

"""
THIS CODE WAS CREATED FOR IMPORTING ALL RELEVANT MODULES AND RUNNING THE SOFTWARE
The configuration file is read and the modules detailed in here are extracted
A component selection screen is shown followed by the main window with the camera and motor
control and a separate window for the LED
"""

with open('Configuration File', 'r') as f:
    file = f.read()
cameraLabelList = re.findall(r'CAMERA LABEL: (.*)', file)
cameraFileNameList = re.findall(r'CAMERA FILE NAME: (.*)', file)
cameraClassList = re.findall(r'CAMERA CLASS NAME: (.*)', file)
stageLabelList = re.findall(r'STAGE LABEL: (.*)', file)
stageFileNameList = re.findall(r'STAGE FILE NAME: (.*)', file)
stageClassList = re.findall(r'STAGE CLASS NAME: (.*)', file)
LEDLabelList = re.findall(r'LED LABEL: (.*)', file)
LEDFileNameList = re.findall(r'LED FILE NAME: (.*)', file)
LEDClassList = re.findall(r'LED CLASS NAME: (.*)', file)

class SelectionScreen(QMainWindow, SelectionScreen_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        for i in range(len(cameraLabelList)):
            self.CameraSelect_comboBox.addItem(cameraLabelList[i])
        for i in range(len(stageLabelList)):
            self.StageSelect_comboBox.addItem(stageLabelList[i])
        for i in range(len(LEDLabelList)):
            self.LEDSelect_comboBox.addItem(LEDLabelList[i])   
        self.Confirm_Button.clicked.connect(lambda : runMainWindow(self.CameraSelect_comboBox.currentIndex(),self.StageSelect_comboBox.currentIndex(),self.LEDSelect_comboBox.currentIndex()))
            
def runMainWindow(cameraIndex, stageIndex, LEDIndex):
    window1.close()
    print(cameraIndex)
    cameraModule = importlib.import_module(cameraFileNameList[cameraIndex])
    cameraClass = getattr(cameraModule, cameraClassList[cameraIndex])
    runMainWindow.cameraInstance = cameraClass()
    stageModule = importlib.import_module(stageFileNameList[stageIndex])
    stageClass = getattr(stageModule, stageClassList[stageIndex])
    runMainWindow.stageInstance = stageClass()
    LEDModule = importlib.import_module(LEDFileNameList[LEDIndex])
    LEDClass = getattr(LEDModule, LEDClassList[LEDIndex])
    class LED(QWidget, LEDClass):
        def __init__(self):
            super().__init__()
            self.setupUi(self)
    print(LEDClass)
    window2 = MainWindow()
    window2.show()
    window3 = LED()
    print(window3)
    window3.show()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
        Setting up the imported classes for use
        """ 
        super().__init__()
        self.setupUi(self)
        self.camera = runMainWindow.cameraInstance
        print(self.camera)
        self.stage = runMainWindow.stageInstance
        print(self.stage)
        gc.disable()
        
        """
        Camera control buttons for camera set up
        """
        self.ActivateCamera_Button.clicked.connect(lambda : self.camera.CameraRunningThreadStart(self.LiveCameraFeed_Label.setPixmap, self.SharpnessValue_Label.setNum))
        self.Autofocus_Button.clicked.connect(lambda : self.stage.Autofocus_Thread(self.ZPos_Label.text(),self.ZPos_Label.setNum))
        self.CaptureImage_Button.clicked.connect(lambda : self.camera.ImageCaptureThread(self.LiveCameraFeed_Label.pixmap(), self.FileDirectory_LineEdit.text()))
        self.StartTimelapse_Button.clicked.connect(lambda : self.camera.TimelapseThread(self.TimeStep_Spinbox.value(), self.CaptureNo_Spinbox.value(), self.LiveCameraFeed_Label.pixmap(),self.FileDirectory_LineEdit.text(), self.TimelapseRun_Label.setText))
        self.StopTimelapse_Button.clicked.connect(lambda : self.camera.TimelapseAbort(self.TimelapseRun_Label.setText))
       
        """
        XYZ coordinate buttons for stage set up
        """
        self.XPos_Button.clicked.connect(lambda : self.stage.XPos_Thread(self.X_ComboBox.currentText(),self.XPos_Label.text(),self.XPos_Label.setNum))
        self.XNeg_Button.clicked.connect(lambda : self.stage.XNeg_Thread(self.X_ComboBox.currentText(),self.XPos_Label.text(),self.XPos_Label.setNum))
        self.YPos_Button.clicked.connect(lambda: self.stage.YPos_Thread(self.Y_ComboBox.currentText(),self.YPos_Label.text(),self.YPos_Label.setNum))
        self.YNeg_Button.clicked.connect(lambda: self.stage.YNeg_Thread(self.Y_ComboBox.currentText(),self.YPos_Label.text(),self.YPos_Label.setNum))
        self.ZPos_Button.clicked.connect(lambda: self.stage.ZPos_Thread(self.Z_ComboBox.currentText(),self.ZPos_Label.text(),self.ZPos_Label.setNum))
        self.ZNeg_Button.clicked.connect(lambda: self.stage.ZNeg_Thread(self.Z_ComboBox.currentText(),self.ZPos_Label.text(),self.ZPos_Label.setNum))
        self.Recalibrate_Button.clicked.connect(lambda: self.stage.RecalibratePosition(self.XPos_Label.setNum,self.YPos_Label.setNum,self.ZPos_Label.setNum))
    
if __name__ == '__main__':
    app = QApplication([])
    window1 = SelectionScreen()
    window1.show()
    app.exit(app.exec_())