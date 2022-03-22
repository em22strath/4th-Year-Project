import threading
import time
import RPi.GPIO as GPIO

"""
THIS CODE WAS CREATED FOR THE OPENFLEXURE MICROSCOPE DELTA STAGE SET UP
For this set up, the X,Y,Z direction are defined by a single motor movement
The X,Y,Z direction each have a dedicated function and thread for the positive and negative direction
The motor movement is defined by half stepping. There are 8 cycles in 1 revolution and a gear reduction
of 1/64. For 1 revolution, the code loops 512 times, as 8 x 64 = 512
"""
    
class deltaStage:
    def __init__(self):
        
        GPIO.setmode(GPIO.BCM)

        self.MotorA = [17,18,27,22]
        self.MotorB = [4,25,24,23]
        self.MotorC = [13,12,6,5]
        
        for pin in self.MotorA:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin,False)            
        for pin in self.MotorB:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin,False)           
        for pin in self.MotorC:
            GPIO.setup(pin,GPIO.OUT)
            GPIO.output(pin,False)
        
        self.positiveSequence = [[1,0,0,1],
                                [0,0,0,1],
                                [0,0,1,1],
                                [0,0,1,0],
                                [0,1,1,0],
                                [0,1,0,0],
                                [1,1,0,0],
                                [1,0,0,0]]
        self.negativeSequence = [[1,0,0,0],
                                 [1,1,0,0],
                                 [0,1,0,0],
                                 [0,1,1,0],
                                 [0,0,1,0],
                                 [0,0,1,1],
                                 [0,0,0,1],
                                 [1,0,0,1]]
 
    def XPos_Thread(self,value, currentPosition, newPosition):
        XPos_Thread = threading.Thread(target=self.XPos_Func, args = [value, currentPosition, newPosition])
        XPos_Thread.start()
 
    def XPos_Func(self, value, currentPosition, newPosition):
        Xcounter = int(value)
        fixedXcounter = 0
        multiplecounter = 0
        while fixedXcounter < Xcounter:
            for i in range(256):
                if multiplecounter == 0:
                    for step in range(8): 
                        for pin in range(4): 
                            GPIO.output(self.MotorA[pin], self.positiveSequence[step][pin])
                            GPIO.output(self.MotorB[pin], self.negativeSequence[step][pin])
                            GPIO.output(self.MotorC[pin], self.negativeSequence[step][pin])
                        time.sleep(0.0008)
                elif multiplecounter == 1 or multiplecounter == 2:
                    for step in range(8): 
                        for pin in range(4): 
                            GPIO.output(self.MotorA[pin], self.positiveSequence[step][pin])
                            GPIO.output(self.MotorB[pin], self.negativeSequence[step][pin])
                        time.sleep(0.0008)
                elif multiplecounter == 3 or multiplecounter == 4:
                    for step in range(8): 
                        for pin in range(4): 
                            GPIO.output(self.MotorB[pin], self.negativeSequence[step][pin])
                        time.sleep(0.0008)
                if multiplecounter < 5:
                    multiplecounter = multiplecounter + 1
                else:
                    multiplecounter = 0
            fixedXcounter = fixedXcounter + 1
        newPosition(int(currentPosition) + Xcounter*170)
 
    def XNeg_Thread(self, value, currentPosition, newPosition):
        XNeg_Thread = threading.Thread(target=self.XNeg_Func, args = [value, currentPosition, newPosition])
        XNeg_Thread.start()
 
    def XNeg_Func(self, value, currentPosition, newPosition):
        Xcounter = int(value)
        fixedXcounter = 0
        multiplecounter = 0
        while fixedXcounter < Xcounter:
            for i in range(256):
                if multiplecounter == 0:
                    for step in range(8): 
                        for pin in range(4): 
                            GPIO.output(self.MotorA[pin], self.positiveSequence[step][pin])
                            GPIO.output(self.MotorB[pin], self.negativeSequence[step][pin])
                            GPIO.output(self.MotorC[pin], self.negativeSequence[step][pin])
                        time.sleep(0.0008)
                elif multiplecounter == 1 or multiplecounter == 2:
                    for step in range(8): 
                        for pin in range(4): 
                            GPIO.output(self.MotorA[pin], self.positiveSequence[step][pin])
                            GPIO.output(self.MotorC[pin], self.negativeSequence[step][pin])
                        time.sleep(0.0008)
                elif multiplecounter == 3 or multiplecounter == 4:
                    for step in range(8): 
                        for pin in range(4): 
                            GPIO.output(self.MotorC[pin], self.negativeSequence[step][pin])
                        time.sleep(0.0008)
                if multiplecounter < 5:
                    multiplecounter = multiplecounter + 1
                else:
                    multiplecounter = 0
            fixedXcounter = fixedXcounter + 1
        newPosition(int(currentPosition) - Xcounter*170)
 
    def YPos_Thread(self, value, currentPosition, newPosition):
        YPos_Thread = threading.Thread(target=self.YPos_Func, args = [value, currentPosition, newPosition])
        YPos_Thread.start()
    
    def YPos_Func(self,value, currentPosition, newPosition):
        Ycounter = int(value)
        fixedYcounter = 0
        while fixedYcounter < Ycounter:
            for i in range(256): 
                for step in range(8):
                        for pin in range(4):
                            GPIO.output(self.MotorA[pin], self.negativeSequence[step][pin])
                            GPIO.output(self.MotorB[pin], self.positiveSequence[step][pin])
                            GPIO.output(self.MotorC[pin], self.positiveSequence[step][pin]) 
                        time.sleep(0.0008)
            fixedYcounter = fixedYcounter + 1
        newPosition(int(currentPosition) + Ycounter*170)
 
    def YNeg_Thread(self, value, currentPosition, newPosition):
        YNeg_Thread = threading.Thread(target=self.YNeg_Func, args = [value, currentPosition, newPosition])
        YNeg_Thread.start()
 
    def YNeg_Func(self, value, currentPosition, newPosition):
        Ycounter = int(value)
        fixedYcounter = 0
        while fixedYcounter < Ycounter:
            for i in range(256): 
                for step in range(8): 
                        for pin in range(4): 
                            GPIO.output(self.MotorA[pin], self.negativeSequence[step][pin])
                            GPIO.output(self.MotorB[pin], self.positiveSequence[step][pin])
                            GPIO.output(self.MotorC[pin], self.positiveSequence[step][pin])
                        time.sleep(0.0008) 
            fixedYcounter = fixedYcounter + 1
        newPosition(int(currentPosition) - Ycounter*170)
 
    def ZPos_Thread(self, value, currentPosition, newPosition):
        ZPos_Thread = threading.Thread(target=self.ZPos_Func, args = [value, currentPosition, newPosition])
        ZPos_Thread.start()
 
    def ZPos_Func(self, value, currentPosition, newPosition):
        Zcounter = int(value)
        fixedZcounter = 0
        while fixedZcounter < Zcounter:
             for i in range(16): 
                 for step in range(8): 
                         for pin in range(4):
                             GPIO.output(self.MotorA[pin], self.positiveSequence[step][pin])
                             GPIO.output(self.MotorB[pin], self.positiveSequence[step][pin])
                             GPIO.output(self.MotorC[pin], self.positiveSequence[step][pin])
                         time.sleep(0.0008)
            fixedZcounter = fixedZcounter + 1
        newPosition(int(currentPosition) + Zcounter*10)
 
    def ZNeg_Thread(self, value, currentPosition, newPosition):
        ZNeg_Thread = threading.Thread(target=self.ZNeg_Func, args = [value, currentPosition, newPosition])
        ZNeg_Thread.start()
 
    def ZNeg_Func(self, value, currentPosition, newPosition):
        Zcounter = int(value)
        fixedZcounter = 0
        while fixedZcounter < Zcounter:
            for i in range(16):
                 for step in range(8):
                         for pin in range(4): 
                             GPIO.output(self.MotorA[pin], self.negativeSequence[step][pin])
                             GPIO.output(self.MotorB[pin], self.negativeSequence[step][pin])
                             GPIO.output(self.MotorC[pin], self.negativeSequence[step][pin])
                         time.sleep(0.0008)
            fixedZcounter = fixedZcounter + 1
        newPosition(int(currentPosition) + Zcounter*10)
    
    def RecalibratePosition(self,newPositionXPos,newPositionYPos,newPositionZPos):
        newPositionXPos(0)
        newPositionYPos(0)
        newPositionZPos(0)
        
    def Autofocus_Thread(self, currentPosition, newPosition):
        Autofocus_Thread = threading.Thread(target=self.Autofocus_Func, args = [currentPosition, newPosition])
        Autofocus_Thread.start()
    
    def Autofocus_Func(self, currentPosition, newPosition):
        sharpnessValues = []
        for i in range(50):
            for i in range(16):
                for step in range(8):
                        for pin in range(4):
                            GPIO.output(self.MotorA[pin], self.negativeSequence[step][pin])
                            GPIO.output(self.MotorB[pin], self.negativeSequence[step][pin])
                            GPIO.output(self.MotorC[pin], self.negativeSequence[step][pin]) 
                        time.sleep(0.0008)
        newPosition(int(currentPosition) - 50*10)
        for i in range(100):
            for i in range(16): 
                for step in range(8): 
                        for pin in range(4):
                            GPIO.output(self.MotorA[pin], self.positiveSequence[step][pin])
                            GPIO.output(self.MotorB[pin], self.positiveSequence[step][pin])
                            GPIO.output(self.MotorC[pin], self.positiveSequence[step][pin])
                        time.sleep(0.0008)        
            print(settings.storedSharpness)
            sharpnessValues.append(settings.storedSharpness)
        newPosition(int(currentPosition) + 50*10)
        print('Maximum Sharpness', max(sharpnessValues))
        sharpnessMax = sharpnessValues.index(max(sharpnessValues))
        print('Maximum Sharpness Position', sharpnessMax)
        sharpnessMovement = 100 - (sharpnessMax +1)
        print('Movement back', sharpnessMovement)
        for i in range(sharpnessMovement+10):
            for i in range(16):
                for step in range(8):
                        for pin in range(4):
                            GPIO.output(self.MotorA[pin], self.negativeSequence[step][pin])
                            GPIO.output(self.MotorB[pin], self.negativeSequence[step][pin])
                            GPIO.output(self.MotorC[pin], self.negativeSequence[step][pin]) 
                        time.sleep(0.0008)
        newPosition(int(currentPosition) + 50*10 - ((sharpnessMax+1)*10 + 10))
        for i in range(5):
            for i in range(16): 
                for step in range(8): 
                        for pin in range(4): 
                            GPIO.output(self.MotorC[pin], self.positiveSequence[step][pin])
                        time.sleep(0.0008)
        newPosition(int(currentPosition) + 50*10 - ((sharpnessMax+1)*10 + 5))
        