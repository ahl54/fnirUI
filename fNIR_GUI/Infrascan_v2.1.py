# -*- coding: utf-8 -*-

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

