from PyQt5 import QtCore, QtGui, QtWidgets
import time
import RPi.GPIO as GPIO
from gpiozero import PWMLED

"""
THIS CODE WAS CREATED FOR A BASIC 3.2V WHITE LED
This contains the code for controlling the LED and GUI to display the user control
"""

class basicLED(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 160)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Brightness = 0.1
        self.Brightness_HorizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.Brightness_HorizontalSlider.setGeometry(QtCore.QRect(20, 20, 160, 22))
        self.Brightness_HorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.Brightness_HorizontalSlider.setObjectName("Brightness_HorizontalSlider")
        self.Brightness_Label = QtWidgets.QLabel(self.centralwidget)
        self.Brightness_Label.setGeometry(QtCore.QRect(75, 40, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.Brightness_Label.setFont(font)
        self.Brightness_Label.setObjectName("Matrix_Label_2")
        self.On_Button = QtWidgets.QPushButton(self.centralwidget)
        self.On_Button.setGeometry(QtCore.QRect(70, 80, 60, 28))
        self.On_Button.setObjectName("On_Button")
        self.Off_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Off_Button.setGeometry(QtCore.QRect(70, 120, 60, 28))
        self.Off_Button.setObjectName("Off_Button")
        
        self.Brightness_HorizontalSlider.setMaximum(10)
        self.Brightness_HorizontalSlider.setMinimum(0)
        self.Brightness_HorizontalSlider.setTickInterval(1)
        self.Brightness_HorizontalSlider.valueChanged.connect(self.BrightnessValueChanged)
        
        self.On_Button.clicked.connect(self.On)
        self.Off_Button.clicked.connect(self.Off)
        
        self.led = PWMLED(18)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def On(self):
        self.led.on()
                
    def Off(self):
        self.led.off()

    def BrightnessValueChanged(self):
        self.Brightness = 0.1 * self.Brightness_HorizontalSlider.value()
        self.led.value = self.Brightness
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LED"))
        self.Brightness_Label.setText(_translate("MainWindow", "Brightness"))
        self.On_Button.setText(_translate("MainWindow", "On"))
        self.Off_Button.setText(_translate("MainWindow", "Off"))

"The window does not to be shown in this code as it is displayed through the run file"
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = basicLED()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
