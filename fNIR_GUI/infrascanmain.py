
# coding: utf-8

# In[1]:

# %load infrascandesign.py

# Form implementation generated from reading ui file 'C:/Users/Anna/Documents/InfraScan-20170425T152025Z-001/infrascan.ui'
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
        InfraScan.resize(921, 665)
        self.centralWidget = QtGui.QWidget(InfraScan)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 931, 661))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Oxygen_tab = QtGui.QWidget()
        self.Oxygen_tab.setObjectName(_fromUtf8("Oxygen_tab"))
        self.select_oxygen_type = QtGui.QComboBox(self.Oxygen_tab)
        self.select_oxygen_type.setEnabled(True)
        self.select_oxygen_type.setGeometry(QtCore.QRect(160, 30, 581, 56))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.select_oxygen_type.setFont(font)
        self.select_oxygen_type.setAcceptDrops(False)
        self.select_oxygen_type.setAutoFillBackground(True)
        self.select_oxygen_type.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.select_oxygen_type.setObjectName(_fromUtf8("select_oxygen_type"))
        self.select_oxygen_type.addItem(_fromUtf8(""))
        self.Fixed_Oxygen = QtGui.QFrame(self.Oxygen_tab)
        self.Fixed_Oxygen.setGeometry(QtCore.QRect(0, 110, 911, 471))
        self.Fixed_Oxygen.setFrameShape(QtGui.QFrame.StyledPanel)
        self.Fixed_Oxygen.setFrameShadow(QtGui.QFrame.Raised)
        self.Fixed_Oxygen.setObjectName(_fromUtf8("Fixed_Oxygen"))
        self.layoutWidget = QtGui.QWidget(self.Fixed_Oxygen)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 70, 411, 25))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtGui.QFrame.Plain)
        self.label_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtGui.QFrame.Plain)
        self.label_3.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.layoutWidget1 = QtGui.QWidget(self.Fixed_Oxygen)
        self.layoutWidget1.setGeometry(QtCore.QRect(140, 150, 811, 89))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_7 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_7.setFrameShadow(QtGui.QFrame.Plain)
        self.label_7.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_2.addWidget(self.label_7)
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtGui.QFrame.Plain)
        self.label_4.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.layoutWidget2 = QtGui.QWidget(self.Fixed_Oxygen)
        self.layoutWidget2.setGeometry(QtCore.QRect(180, 270, 681, 25))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setMargin(11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_8 = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_8.setFrameShadow(QtGui.QFrame.Plain)
        self.label_8.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_3.addWidget(self.label_8)
        self.label_5 = QtGui.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_5.setFrameShadow(QtGui.QFrame.Plain)
        self.label_5.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.layoutWidget3 = QtGui.QWidget(self.Fixed_Oxygen)
        self.layoutWidget3.setGeometry(QtCore.QRect(230, 340, 431, 25))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setMargin(11)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_9 = QtGui.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_9.setFrameShadow(QtGui.QFrame.Plain)
        self.label_9.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_4.addWidget(self.label_9)
        self.label_6 = QtGui.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_6.setFrameShadow(QtGui.QFrame.Plain)
        self.label_6.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_4.addWidget(self.label_6)
        self.layoutWidget4 = QtGui.QWidget(self.Fixed_Oxygen)
        self.layoutWidget4.setGeometry(QtCore.QRect(201, 0, 401, 421))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.dial = QtGui.QDial(self.layoutWidget4)
        self.dial.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.dial.setMaximum(99)
        self.dial.setSingleStep(13)
        self.dial.setPageStep(13)
        self.dial.setProperty("value", 0)
        self.dial.setSliderPosition(0)
        self.dial.setTracking(True)
        self.dial.setInvertedAppearance(False)
        self.dial.setInvertedControls(False)
        self.dial.setWrapping(False)
        self.dial.setNotchTarget(13.0)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName(_fromUtf8("dial"))
        self.verticalLayout.addWidget(self.dial)
        self.pushButton_2 = QtGui.QPushButton(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        self.label = QtGui.QLabel(self.Fixed_Oxygen)
        self.label.setGeometry(QtCore.QRect(690, -20, 331, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.Fixed_Oxygen)
        self.plainTextEdit.setGeometry(QtCore.QRect(710, 30, 191, 271))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.tabWidget.addTab(self.Oxygen_tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        InfraScan.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(InfraScan)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        InfraScan.setStatusBar(self.statusBar)

        self.retranslateUi(InfraScan)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(InfraScan)

    def retranslateUi(self, InfraScan):
        InfraScan.setWindowTitle(_translate("InfraScan", "InfraScan", None))
        #self.select_oxygen_type.setCurrentText(_translate("InfraScan", "Fixed Oxygen Measurement", None))
        self.select_oxygen_type.setItemText(0, _translate("InfraScan", "Fixed Oxygen Measurement", None))
        self.label_2.setText(_translate("InfraScan", "Left Frontal", None))
        self.label_3.setText(_translate("InfraScan", "Right Frontal", None))
        self.label_7.setText(_translate("InfraScan", "Left Temporal", None))
        self.label_4.setText(_translate("InfraScan", "Right Temporal", None))
        self.label_8.setText(_translate("InfraScan", "Left Parietal", None))
        self.label_5.setText(_translate("InfraScan", "Right Parietal", None))
        self.label_9.setText(_translate("InfraScan", "Left Occiptal", None))
        self.label_6.setText(_translate("InfraScan", "Right Occiptal", None))
        self.pushButton.setText(_translate("InfraScan", "Measure", None))
        self.pushButton_2.setText(_translate("InfraScan", "Process Measurements", None))
        self.label.setText(_translate("InfraScan", "Stored Measurements", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Oxygen_tab), _translate("InfraScan", "Oxygen", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("InfraScan", "Edema", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("InfraScan", "Hematoma", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("InfraScan", "Summary", None))



# In[2]:

import sys # We need sys so that we can pass argv to QApplication

#import infrascannerdesign # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer

class InfrascanApp(QtGui.QMainWindow, Ui_InfraScan):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the infrascannerdesign.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = InfrascanApp()            # We set the form to be our design
    form.show()                         # Show the form
    app.exec_()                         # and execute the app

    
if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function


# In[ ]:



