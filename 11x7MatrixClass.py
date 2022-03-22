from PyQt5 import QtCore, QtGui, QtWidgets
from matrix11x7 import Matrix11x7

"""
THIS CODE WAS CREATED FOR THE PIMORONI LED 11x7 MATRIX
This contains the code for controlling the LED and GUI to display the user control
"""

class LEDMatrix(object):
    def setupUi(self, MainWindow):
        self.matrix = Matrix11x7()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Brightness = 0.1
        self.checkbox_list = []
        y_pos_init = 20 
        x_pos_init = 20
        y_shift = 20
        x_shift = 20
        for y in range(7):
            for x in range(11):
                temp_box = QtWidgets.QCheckBox(self.centralwidget)
                temp_box.setGeometry(QtCore.QRect(x_pos_init + (x_shift*x), y_pos_init + (y_shift*y), 16, 20))
                temp_box.setText("")
                temp_box.setObjectName("checkBox{}{}".format(x,y))
                self.checkbox_list.append(temp_box)        
        
        self.Matrix_Label = QtWidgets.QLabel(self.centralwidget)
        self.Matrix_Label.setGeometry(QtCore.QRect(90, 170, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Matrix_Label.setFont(font)
        self.Matrix_Label.setObjectName("Matrix_Label")
        self.Brightness_HorizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.Brightness_HorizontalSlider.setGeometry(QtCore.QRect(260, 20, 160, 22))
        self.Brightness_HorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.Brightness_HorizontalSlider.setObjectName("Brightness_HorizontalSlider")
        self.Brightness_Label = QtWidgets.QLabel(self.centralwidget)
        self.Brightness_Label.setGeometry(QtCore.QRect(310, 40, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.Brightness_Label.setFont(font)
        self.Brightness_Label.setObjectName("Matrix_Label_2")
        self.SelectAll_Button = QtWidgets.QPushButton(self.centralwidget)
        self.SelectAll_Button.setGeometry(QtCore.QRect(290, 80, 93, 28))
        self.SelectAll_Button.setObjectName("SelectAll_Button")
        self.DeselectAll_Button = QtWidgets.QPushButton(self.centralwidget)
        self.DeselectAll_Button.setGeometry(QtCore.QRect(290, 120, 93, 28))
        self.DeselectAll_Button.setObjectName("DeselectAll_Button")
        
        self.Brightness_HorizontalSlider.setMaximum(10)
        self.Brightness_HorizontalSlider.setMinimum(0)
        self.Brightness_HorizontalSlider.setTickInterval(1)
        self.Brightness_HorizontalSlider.valueChanged.connect(self.BrightnessValueChanged)

        for index ,i in enumerate(self.checkbox_list):
            i.stateChanged.connect(self.Checkbox_linker(index))
 
        self.SelectAll_Button.clicked.connect(self.SelectAll)
        self.DeselectAll_Button.clicked.connect(self.DeselectAll)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def SelectAll(self):
        for i in self.checkbox_list:
               i.setChecked(True)
                
    def DeselectAll(self):
        for i in self.checkbox_list:
               i.setChecked(False)

    def BrightnessValueChanged(self):
        self.Brightness = 0.1 * self.Brightness_HorizontalSlider.value()
        for i in self.checkbox_list:
            if i.checkState():
                i.setChecked(False)
                i.setChecked(True)
                       
    def Checkbox_linker(self,arg):
    #Allows the checkbox function to be given an argument while returning a function rather than the function result
        def linked_checkbox():
            return self.Checkbox(arg)
        
        return linked_checkbox
        
    def index2xy(self,index):
        y = int(index/11)
        x = index % 11
        return x,y, index
    
    def Checkbox(self,index):
        x,y ,index = self.index2xy(index)
        if self.checkbox_list[index].isChecked() == True:
            self.matrix.set_pixel(x,y,self.Brightness)
        else:
            self.matrix.set_pixel(x,y,0)
        self.matrix.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LED Matrix"))
        self.Matrix_Label.setText(_translate("MainWindow", "11 x 7 Matrix"))
        self.Brightness_Label.setText(_translate("MainWindow", "Brightness"))
        self.SelectAll_Button.setText(_translate("MainWindow", "Select All"))
        self.DeselectAll_Button.setText(_translate("MainWindow", "Deselect All"))

"The window does not to be shown in this code as it is displayed through the run file"
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = LEDMatrix()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
