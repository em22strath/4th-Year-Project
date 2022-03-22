# You may need to import more libraries depending on the motors you are using
import threading
import time
import settings

"""
THIS CODE WAS CREATED AS A TEMPLATE FOR ANY MOTOR SET UP TO TRANSLATE THE STAGE IN THE X,Y AND Z DIRECTION
All of the function names and arguments fed into the functions must remain the same. The arguments fed in refer to the GUI, as detailed below:
'value' - the user input step value, this same variable is used for all directions
'currentPosition' - the on screen value for steps taken in the direction
'newPosition' - the on screen value for new steps taken in the direction
'newPositionXPos' - the one screen value for steps taken in the x direction
'newPositionYPos' - the one screen value for steps taken in the y direction
'newPositionZPos' - the one screen value for steps taken in the z direction
"""

"Change the name of the class to correspond with the stage set up"
class genericStage:
    
    "Function for defining motors and setting them up"
    def __init__(self):
        # Write code here for your own motors
 
    "Thread for positive X movement"
    def XPos_Thread(self,value, currentPosition, newPosition):
        XPos_Thread = threading.Thread(target=self.XPos_Func, args = [value, currentPosition, newPosition])
        XPos_Thread.start()
 
    "Function for positive X movement"
    def XPos_Func(self, value, currentPosition, newPosition):
        Xcounter = int(value)
        fixedXcounter = 0
        while fixedXcounter < Xcounter:
            # Write code here to move the stage in the positive X direction for one step
            fixedXcounter = fixedXcounter + 1
        newPosition(int(currentPosition) + Xcounter*10) # Position may require calibration

    "Thread for negative X movement"
    def XNeg_Thread(self, value, currentPosition, newPosition):
        XNeg_Thread = threading.Thread(target=self.XNeg_Func, args = [value, currentPosition, newPosition])
        XNeg_Thread.start()
 
    "Function for negative X movement"
    def XNeg_Func(self, value, currentPosition, newPosition):
        Xcounter = int(value)
        fixedXcounter = 0
        while fixedXcounter < Xcounter:
            # Write code here to move the stage in the negative X direction for one step
            fixedXcounter = fixedXcounter + 1
        newPosition(int(currentPosition) - Xcounter*10) # Position may require calibration

    "Thread for positive Y movement"
    def YPos_Thread(self, value, currentPosition, newPosition):
        YPos_Thread = threading.Thread(target=self.YPos_Func, args = [value, currentPosition, newPosition])
        YPos_Thread.start()
    
    "Function for positive Y movement"
    def YPos_Func(self,value, currentPosition, newPosition):
        Ycounter = int(value)
        fixedYcounter = 0
        while fixedYcounter < Ycounter:
            # Write code here to move the stage in the positive Y direction for one step
            fixedYcounter = fixedYcounter + 1
        newPosition(int(currentPosition) + Ycounter*10) # Position may require calibration
 
    "Thread for negative Y movement"
    def YNeg_Thread(self, value, currentPosition, newPosition):
        YNeg_Thread = threading.Thread(target=self.YNeg_Func, args = [value, currentPosition, newPosition])
        YNeg_Thread.start()

    "Function for negative Y movement"
    def YNeg_Func(self, value, currentPosition, newPosition):
        Ycounter = int(value)
        fixedYcounter = 0
        while fixedYcounter < Ycounter: 
            # Write code here to move the stage in the negative Y direction for one step
            fixedYcounter = fixedYcounter + 1
        newPosition(int(currentPosition) - Ycounter*10) # Position may require calibration

    "Thread for positive Z movement"
    def ZPos_Thread(self, value, currentPosition, newPosition):
        ZPos_Thread = threading.Thread(target=self.ZPos_Func, args = [value, currentPosition, newPosition])
        ZPos_Thread.start()

    "Function for positive Z movement"
    def ZPos_Func(self, value, currentPosition, newPosition):
        Zcounter = int(value)
        fixedZcounter = 0
        while fixedZcounter < Zcounter:
            # Write code here to move the stage in the positive Z direction for one step
            fixedZcounter = fixedZcounter + 1
        newPosition(int(currentPosition) + Zcounter*10) # Position may require calibration

    "Thread for negative Z movement"
    def ZNeg_Thread(self, value, currentPosition, newPosition):
        ZNeg_Thread = threading.Thread(target=self.ZNeg_Func, args = [value, currentPosition, newPosition])
        ZNeg_Thread.start()
 
    "Function for negative Z movement"
    def ZNeg_Func(self, value, currentPosition, newPosition):
        Zcounter = int(value)
        fixedZcounter = 0
        while fixedZcounter < Zcounter:
            # Write code here to move the stage in the negative Z direction for one step
            fixedZcounter = fixedZcounter + 1
        newPosition(int(currentPosition) - Zcounter*10) # Position may require calibration
 
    "Function for resetting all position values on screen to zero"
    def RecalibratePosition(self,newPositionXPos,newPositionYPos,newPositionZPos):
        newPositionXPos(0)
        newPositionYPos(0)
        newPositionZPos(0)
    
    "Thread for autofocussing"
    def Autofocus_Thread(self, currentPosition, newPosition):
        Autofocus_Thread = threading.Thread(target=self.Autofocus_Func, args = [currentPosition, newPosition])
        Autofocus_Thread.start()

    "Function for autofocussing"
    "Ranges may be changed by the user depending how far the autofocussing scans and may need calibrating in the last steps"
    def Autofocus_Func(self, currentPosition, newPosition):
        sharpnessValues = []
        for i in range(50):
        # Write code here to move the stage in the negative Z direction for one step
        newPosition(int(currentPosition) - 50*10) # Position may require calibration
        for i in range(100):
        # Write code here to move the stage in the positive Z direction for one step
        print(settings.storedSharpness)
        sharpnessValues.append(settings.storedSharpness)
        newPosition(int(currentPosition) + 50*10) # Position may require calibration
        print('Maximum Sharpness', max(sharpnessValues))
        sharpnessMax = sharpnessValues.index(max(sharpnessValues))
        print('Maximum Sharpness Position', sharpnessMax)
        sharpnessMovement = 100 - (sharpnessMax +1)
        print('Movement back', sharpnessMovement)
        for i in range(sharpnessMovement+10):
        # Write code here to move the stage in the negative Z direction for one step
        newPosition(int(currentPosition) + 50*10 - ((sharpnessMax+1)*10 + 10)) # Position may require calibration
        for i in range(5):
        # Write code here to move the stage in the positive Z direction for one step
        newPosition(int(currentPosition) + 50*10 - ((sharpnessMax+1)*10 + 5)) # Position may require calibration
        