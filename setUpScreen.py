from PyQt5 import QtCore, QtGui, QtWidgets

"""
THIS CODE WAS CREATED TO DESIGN THE GUI FOR THE START UP SCREEN
"""

class SelectionScreen_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(454, 310)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CameraSelect_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.CameraSelect_comboBox.setGeometry(QtCore.QRect(270, 80, 161, 22))
        self.CameraSelect_comboBox.setObjectName("CameraSelect_comboBox")
        self.ComponentSelectionTitle_Label = QtWidgets.QLabel(self.centralwidget)
        self.ComponentSelectionTitle_Label.setGeometry(QtCore.QRect(20, 10, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setUnderline(True)
        self.ComponentSelectionTitle_Label.setFont(font)
        self.ComponentSelectionTitle_Label.setObjectName("ComponentSelectionTitle_Label")
        self.LEDSelect_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.LEDSelect_comboBox.setGeometry(QtCore.QRect(270, 200, 161, 22))
        self.LEDSelect_comboBox.setObjectName("LEDSelect_comboBox")
        self.StageSelect_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.StageSelect_comboBox.setGeometry(QtCore.QRect(270, 140, 161, 22))
        self.StageSelect_comboBox.setObjectName("StageSelect_comboBox")
        self.Confirm_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Confirm_Button.setGeometry(QtCore.QRect(270, 260, 161, 28))
        self.Confirm_Button.setObjectName("Confirm_Button")
        self.CameraSelect_Label = QtWidgets.QLabel(self.centralwidget)
        self.CameraSelect_Label.setGeometry(QtCore.QRect(20, 70, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setUnderline(False)
        self.CameraSelect_Label.setFont(font)
        self.CameraSelect_Label.setObjectName("CameraSelect_Label")
        self.StageSelect_Label = QtWidgets.QLabel(self.centralwidget)
        self.StageSelect_Label.setGeometry(QtCore.QRect(20, 130, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setUnderline(False)
        self.StageSelect_Label.setFont(font)
        self.StageSelect_Label.setObjectName("StageSelect_Label")
        self.LEDSelect_Label = QtWidgets.QLabel(self.centralwidget)
        self.LEDSelect_Label.setGeometry(QtCore.QRect(20, 190, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setUnderline(False)
        self.LEDSelect_Label.setFont(font)
        self.LEDSelect_Label.setObjectName("LEDSelect_Label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Selection Screen"))
        self.ComponentSelectionTitle_Label.setText(_translate("MainWindow", "COMPONENT SELECTION"))
        self.Confirm_Button.setText(_translate("MainWindow", "Confirm Selection"))
        self.CameraSelect_Label.setText(_translate("MainWindow", "Select the camera module:"))
        self.StageSelect_Label.setText(_translate("MainWindow", "Select the microscope set up:"))
        self.LEDSelect_Label.setText(_translate("MainWindow", "Select the illumination source:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SelectionScreen_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
