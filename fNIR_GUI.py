import PyQt5
import ICP
import sys
import atexit
import numpy as np
import pyqtgraph as pg

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget,QToolTip,QPushButton,QApplication, QMainWindow, QGridLayout, QGroupBox,QDesktopWidget, QMenuBar, QMainWindow, QMessageBox, QAction
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject, QThread, QTimer

class fNIR_GUI(QMainWindow):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		self.pathlength = 13 # about 13cm by jiang
		self.DPF = 6.52 # by zhao

		self.ylin = np.random.normal(size=300)
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		menuHome = QAction('Home',self)
		menuHome.triggered.connect(self.showStart)
		fileMenu.addAction(menuHome)
		
		self.inOxy = 0
		self.inStart=0

		self.setGeometry(50,50,1500,750)	
		self.setWindowTitle('Infrascanner 3000')
		self.sSize = QtCore.QSize()

		self.timerSize = QTimer()
		self.timerSize.timeout.connect(self.updateSize)
		
		self.mainWind = QGroupBox(self)

		self.mainWind.move(5,25)
		self.butt0 = QPushButton('Hematoma',self.mainWind)
		self.butt1 = QPushButton('Local Oxygenation',self.mainWind)
		self.butt1.clicked.connect(self.showOxy)
		self.butt2 = QPushButton('Edema',self.mainWind)
		self.butt3 = QPushButton('Display All',self.mainWind)

		self.homeButtFont = QFont()
		self.homeButtFont.setPointSize(36)

		self.butt0.setFont(self.homeButtFont)
		self.butt1.setFont(self.homeButtFont)
		self.butt2.setFont(self.homeButtFont)
		self.butt3.setFont(self.homeButtFont)

		# TODO: remove when data collection functions work
		self.xlin = np.linspace(1,300,300)

		self.plot0 = pg.PlotWidget(self.mainWind)
		self.oxygroup2 = QGroupBox(self.mainWind)
		oxyGrid2 = QGridLayout()
		self.oxygroup2.setLayout(oxyGrid2)

		self.running = 0
		self.paused = 0
		
		butt4 = QPushButton('Start',self.mainWind)	
		butt5 = QPushButton('Pause',self.mainWind)
		butt6 = QPushButton('Stop',self.mainWind)
		butt7 = QPushButton('Clear',self.mainWind)

		butt4.clicked.connect(self.strMeas)
		butt5.clicked.connect(self.pseMeas)
		butt6.clicked.connect(self.stpMeas)
		butt7.clicked.connect(self.clrGraph)

		self.oxyButtFont = QFont()
		self.oxyButtFont.setPointSize(24)

		butt4.setFont(self.oxyButtFont)
		butt5.setFont(self.oxyButtFont)
		butt6.setFont(self.oxyButtFont)
		butt7.setFont(self.oxyButtFont)

		oxyGrid2.addWidget(butt4,0,0)
		oxyGrid2.addWidget(butt5,0,1)
		oxyGrid2.addWidget(butt6,0,2)
		oxyGrid2.addWidget(butt7,0,3)

		self.plot0.setLimits(xMin=0,xMax=300,yMin=-0,yMax=100)

		self.timerPlot = QTimer()
		self.timerPlot.timeout.connect(self.updatePlot)

		self.show()
		self.showStart()

	def showStart(self):
		self.timerPlot.stop()
		self.timerSize.start(1)
		self.butt0.show()
		self.butt1.show()
		self.butt2.show()
		self.butt3.show()

		self.plot0.hide()
		self.oxygroup2.hide()

		self.inOxy = 0
		self.inStart=1

	def showOxy(self):
		self.butt0.hide()
		self.butt1.hide()
		self.butt2.hide()
		self.butt3.hide()

		self.oxygroup2.show()
		self.plot0.show()

		self.inOxy = 1
		self.inStart = 0

	def updateSize(self):
		self.screenShape = QDesktopWidget().screenGeometry()
		self.mainWind.resize(self.frameGeometry().width()-25, self.frameGeometry().height()-65)

		if(self.inOxy == 0):
			self.butt0.resize(self.frameGeometry().width()/2-20,self.frameGeometry().height()/3-30)
			self.butt1.resize(self.frameGeometry().width()/2-20,self.frameGeometry().height()/3-30)
			self.butt2.resize(self.frameGeometry().width()/2-20,self.frameGeometry().height()/3-30)
			self.butt3.resize(self.frameGeometry().width()/2-20,self.frameGeometry().height()-75)

			self.butt0.move(5,5)
			self.butt1.move(5,self.frameGeometry().height()/3-17.5)
			self.butt2.move(5,self.frameGeometry().height()*2/3-40)
			self.butt3.move((self.frameGeometry().width()/2-10),5)

		if (self.inOxy==1):
			self.plot0.move(5,5)
			self.plot0.resize(self.frameGeometry().width()/2-10, self.frameGeometry().height()-75)

			self.oxygroup2.move(self.frameGeometry().width()/2, 5)
			self.oxygroup2.resize(self.frameGeometry().width()/2-30, self.frameGeometry().height()-75)

	def updatePlot(self):

		self.ylin[0:299]=self.ylin[1:300]
		self.ylin[299] = np.random.normal(size=1)
		#self.ylin[299] = myICP.pollData()

		self.plot0.clear()
		self.plot0.plot(self.xlin,self.ylin)

	def strMeas(self):
		
		if((self.running==0)&(self.paused==0)):
			self.myICP = ICP.ICP()
			if(self.myICP.serCon==1):
				self.myICP.sayHello()
				self.myICP.measSettings()
			else:
				self.alertUser = QMessageBox()
				self.alertUser.setText("Could not connect to Infrascanner 3000")
				self.alertUser.setIcon(3)
				self.alertUser.setWindowTitle("Error")
				self.alertUser.exec_()

		elif (self.paused==1):
			self.timerPlot.start(1000)
			self.paused=0
			self.running=1

	def pseMeas(self):
		if(self.running ==1):
			self.timerPlot.stop()
			self.paused = 1

	def stpMeas(self):
		if(self.running ==1|self.paused==1):
			self.timerPlot.stop()
			self.paused = 0
			self.running = 0
			self.myICP.sayBye()

	def clrGraph(self):
		self.plot0.clear()

	def calcAbsorbance(self):
		pass

	def calcOxSat(self,A1,A2,A3):
		concHBR = (a1R*A1+a2R*A2+a3R*A3)/self.pathlength
		concHBO = (a1O*A1+a2O*A2+a3O*A3)/self.pathlength



def main():
    
	app = QApplication(sys.argv)

	ex = fNIR_GUI()
	
	sys.exit(app.exec_())

		


if __name__ == '__main__':
	main()
    	
