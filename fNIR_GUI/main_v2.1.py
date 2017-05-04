
# coding: utf-8

# In[ ]:

# %load Infrascan_v2.1.py

# Form implementation generated from reading ui file 'C:/Users/Anna/Documents/InfraScan-20170425T152025Z-001/infrascan_v2.1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_InfraScan(object):
    def setupUi(self, InfraScan):
        InfraScan.setObjectName(_fromUtf8("InfraScan"))
        InfraScan.resize(712, 548)
        self.centralWidget = QtGui.QWidget(InfraScan)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 931, 661))
        self.tabWidget.setMaximumSize(QtCore.QSize(931, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Oxygen_tab = QtGui.QWidget()
        self.Oxygen_tab.setObjectName(_fromUtf8("Oxygen_tab"))
        self.Fixed_Oxygen = QtGui.QFrame(self.Oxygen_tab)
        self.Fixed_Oxygen.setGeometry(QtCore.QRect(0, 0, 711, 471))
        self.Fixed_Oxygen.setFrameShape(QtGui.QFrame.StyledPanel)
        self.Fixed_Oxygen.setFrameShadow(QtGui.QFrame.Raised)
        self.Fixed_Oxygen.setObjectName(_fromUtf8("Fixed_Oxygen"))
        self.layoutWidget = QtGui.QWidget(self.Fixed_Oxygen)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 401, 421))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.graphicsView = QtGui.QGraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.verticalLayout.addWidget(self.graphicsView)
        self.pushButton = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.label = QtGui.QLabel(self.Fixed_Oxygen)
        self.label.setGeometry(QtCore.QRect(480, 0, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.Fixed_Oxygen)
        self.plainTextEdit.setGeometry(QtCore.QRect(480, 30, 191, 361))
        self.plainTextEdit.setReadOnly(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.pushButton1 = QtGui.QPushButton(self.Fixed_Oxygen)
        self.pushButton1.setGeometry(QtCore.QRect(480, 400, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName(_fromUtf8("pushButton1"))
        self.layoutWidget.raise_()
        self.label.raise_()
        self.plainTextEdit.raise_()
        self.pushButton.raise_()
        self.pushButton.raise_()
        self.tabWidget.addTab(self.Oxygen_tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.graphicsView_2 = QtGui.QGraphicsView(self.tab_2)
        self.graphicsView_2.setGeometry(QtCore.QRect(30, 20, 431, 361))
        self.graphicsView_2.setObjectName(_fromUtf8("graphicsView_2"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.tab_2)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(490, 20, 191, 361))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.graphicsView_3 = QtGui.QGraphicsView(self.tab_3)
        self.graphicsView_3.setGeometry(QtCore.QRect(30, 20, 431, 361))
        self.graphicsView_3.setObjectName(_fromUtf8("graphicsView_3"))
        self.plainTextEdit_3 = QtGui.QPlainTextEdit(self.tab_3)
        self.plainTextEdit_3.setReadOnly(True)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(490, 20, 191, 361))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plainTextEdit_3.setFont(font)
        self.plainTextEdit_3.setObjectName(_fromUtf8("plainTextEdit_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayoutWidget = QtGui.QWidget(self.tab_4)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(29, 19, 651, 431))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.columnView = QtGui.QColumnView(self.gridLayoutWidget)
        self.columnView.setObjectName(_fromUtf8("columnView"))
        self.gridLayout.addWidget(self.columnView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        InfraScan.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(InfraScan)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        InfraScan.setStatusBar(self.statusBar)

        self.retranslateUi(InfraScan)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(InfraScan)

    def retranslateUi(self, InfraScan):
        InfraScan.setWindowTitle(_translate("InfraScan", "InfraScan", None))
        self.pushButton.setText(_translate("InfraScan", "Measure", None))
        self.label.setText(_translate("InfraScan", "Stored Measurements", None))
        self.pushButton1.setText(_translate("InfraScan", "Continuous", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Oxygen_tab), _translate("InfraScan", "Oxygen", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("InfraScan", "Edema", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("InfraScan", "Hematoma", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("InfraScan", "Summary", None))



# In[ ]:

import sys # We need sys so that we can pass argv to QApplication
import os # Need os to pass images to application
import time # for time display
from random import randint # simulate oxygenation values
from PIL import Image, ImageQt

#import infrascannerdesign # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer

class InfrascanApp(QtGui.QMainWindow, Ui_InfraScan):
    
    def __init__(self):

        super(self.__class__, self).__init__()
        
        # initialized state
        self.error_state = 0 # error flag
        self.position = 0 # begin at location 0, frontal left
        self.stored_measurements = [] # list of stored measurements initialized

        self.setupUi(self)  # Defined in design file automatically
        self.image_select()
        self.pushButton.clicked.connect(self.measure)
    
    def reset(self):
        
        # change self.pushButton on click text from "New Measurements" back to "Measure"

        # resets self.position and stored_measurements
        self.position = 0
        self.stored_measurements = []
    
    def image_select(self):
        
        # check error state
        if self.error_state != 0:
            # flip measurement button text to "remeasure"
            # select error image to display
            self.error_select(self.error_state)
            
        # get size of stored_measurements
        numMeas = len(self.stored_measurements)
        
        # original set of images
        orig = "position_img/"
        # alternate set of images
        alt = "/position_img/alternate/"
    
        img_path = alt # set image path
        
        # determine sequence image to show
        if(numMeas >= 8):
            imagePath = (os.getcwd() + img_path + "complete.jpg")
            
            ## TODO: prompt for new patient measurement at this point
            # trigger measurement button text to "New Measurements"
            self.reset()
            
        elif(numMeas == 7):
            imagePath = (os.getcwd() + img_path + "RO.jpg")
        elif(numMeas == 6):
            imagePath = (os.getcwd() + img_path + "LO.jpg")
        elif(numMeas == 5):
            imagePath = (os.getcwd() + img_path + "RP.jpg")
        elif(numMeas == 4):
            imagePath = (os.getcwd() + img_path + "LP.jpg")
        elif(numMeas == 3):
            imagePath = (os.getcwd() + img_path + "RT.jpg")
        elif(numMeas == 2):
            imagePath = (os.getcwd() + img_path + "LT.jpg")
        elif(numMeas == 1):
            imagePath = (os.getcwd() + img_path + "RF.jpg")
        elif(numMeas == 0):
            imagePath = (os.getcwd() + img_path + "LF.jpg")
        
        # use full ABSOLUTE path to the image, not relative
        img = Image.open(imagePath)
        self.display_image(img)

    def display_image(self, img):
        scene = QtGui.QGraphicsScene(self.graphicsView)
        #newGV = QtGui.QGraphicsView(self.graphicsView)
        #self.graphicsView = newGV
        w, h = img.size
        self.imgQ = ImageQt.ImageQt(img)  # we need to hold reference to imgQ, or it will crash
        pixMap = QtGui.QPixmap.fromImage(self.imgQ)
        scene.addPixmap(pixMap)
        #self.graphicsView.fitInView(scene.itemsBoundingRect()) # image scaling pixelated
        self.graphicsView.setScene(scene)
        self.graphicsView.update()
    
    ### TODO: SIMULATE ERROR UNIT TEST
    # def error_simulate:
    #    return
    ###
    
    def error_select(self):
        alt = "/position_img/alternate/"
        img_path = alt # set image path
        if self.error_state == 0:
            pass
        elif self.error_state == 1:
            imagePath = (os.getcwd() + img_path + "err1.jpg")
        elif self.error_state == 2:
            imagePath = (os.getcwd() + img_path + "err2.jpg")           
        elif self.error_state == 3:
            imagePath = (os.getcwd() + img_path + "err3.jpg")
        elif self.error_state == 4:
            imagePath = (os.getcwd() + img_path + "err4.jpg")
        elif self.error_state == 5:
            imagePath = (os.getcwd() + img_path + "err5.jpg")
        elif self.error_state == 6:
            imagePath = (os.getcwd() + img_path + "err6.jpg")
        elif self.error_state == 7:
            imagePath = (os.getcwd() + img_path + "err7.jpg")
                         
        img = Image.open(imagePath)
        self.display_image(img)
                         
        # TODO: check if error resolved
                  
    ###
    
    def pos2str(self):
        # returns a string position given current integer position in sequence of positions
        sequence = ['Left Frontal', 'Right Frontal', 'Left Temporal', 'Right Temporal', 'Left Parietal', 'Right Parietal', 'Left Occipital', 'Right Occipital']
        try:
            sequence[self.position]
        except:
            print('Internal Error: position index exceeded')
            print(self.position)
        return sequence[self.position]
    
    def measure(self):
   
        ### randomO2 HEALTHY TEST USE CASE ONLY 
        # pull oxygenation measurement from probe software
        randomO2 = randint(96,99)
        measurement = randomO2
        ### 
        
        # appends this measurement to stored_measurements
        self.stored_measurements.append(measurement)
        
        meas_text = str(measurement) + "% " + self.pos2str() + " at datetime: " + time.ctime()
        # append measurement text to stored measurements display
        self.plainTextEdit.appendPlainText(meas_text)
        self.plainTextEdit.appendPlainText("") # line spacer for legibility
        #self.plainTextEdit.append(meas_text)
        # sequentially increment to next postition image
        self.image_select()
        self.position = self.position + 1
        
        return

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = InfrascanApp()               # Set the form to be our design
    form.show()                         # Show the form
    app.exec_()                         # Execute the app

    
if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function


# In[ ]:



