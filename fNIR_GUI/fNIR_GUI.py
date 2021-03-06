import PyQt5
import ICP
import sys
import atexit
import numpy as np
import pyqtgraph as pg

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget,QToolTip,QPushButton,QApplication, QMainWindow, QGridLayout, QGroupBox,QDesktopWidget, QMenuBar, QMainWindow, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject, QThread, QTimer

class fNIR_GUI(QMainWindow):

	def __init__(self):
		super().__init__()
		self.initUI()


	def initUI(self):

		self.ylin = np.random.normal(size=300)
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		#fileMenu.addAction(pass)
		self.inOxy = 0
		self.grid = QGridLayout(self)
		self.mainWind = QGroupBox(self)

		self.mainWind.setLayout(self.grid)
		self.mainWind.move(5,25)
		butt0 = QPushButton('Hematoma')
		butt1 = QPushButton('Local Oxygenation')
		butt1.clicked.connect(self.showOxy)
		butt2 = QPushButton('Edema')
		butt3 = QPushButton('Display All')

		self.grid.addWidget(butt0,0,0)
		self.grid.addWidget(butt1,1,0)
		self.grid.addWidget(butt2,2,0)
		self.grid.addWidget(butt3,0,1,3,1)
		self.setGeometry(50,50,1500,750)	
		self.setWindowTitle('Infrascanner 3000')
		self.sSize = QtCore.QSize()

		self.timerSize = QTimer()
		self.timerSize.timeout.connect(self.updateSize)
		self.timerSize.start(1)

		self.show()


	def showOxy(self):
		
		self.xlin = np.linspace(1,300,300)

		QWidget().setLayout(self.grid)
		oxyGrid = QGridLayout(self)
		self.plot0 = pg.PlotWidget()
		self.oxygroup2 = QGroupBox()
		oxyGrid2 = QGridLayout(self)
		self.oxygroup2.setLayout(oxyGrid2)
		self.mainWind.setLayout(oxyGrid)

		self.running = 0
		self.paused = 0
		
		butt4 = QPushButton('Start Measurement')	
		butt5 = QPushButton('Pause Measurement')
		butt6 = QPushButton('Clear Graph')

		butt4.clicked.connect(self.strMeas)
		butt5.clicked.connect(self.pseMeas)
		butt6.clicked.connect(self.clrGraph)

		oxyGrid2.addWidget(butt4,0,0)
		oxyGrid2.addWidget(butt5,0,1)
		oxyGrid2.addWidget(butt6,0,2)

		oxyGrid.addWidget(self.plot0,0,0)
		oxyGrid.addWidget(self.oxygroup2,0,1)

		self.inOxy = 1

		self.plot0.plot(self.xlin,self.ylin)
		self.plot0.setLimits(xMin=0,xMax=300,yMin=-3,yMax=3)

		self.timerPlot = QTimer()
		self.timerPlot.timeout.connect(self.updatePlot)

		self.show()

	def updateSize(self):
		self.screenShape = QDesktopWidget().screenGeometry()
		self.mainWind.resize(self.frameGeometry().width()-25, self.frameGeometry().height()-65)

		if (self.inOxy==1):
			self.plot0.move(5,5)
			self.plot0.resize(self.frameGeometry().width()/2-10, self.frameGeometry().height()-75)

			self.oxygroup2.move(self.frameGeometry().width()/2, 5)
			self.oxygroup2.resize(self.frameGeometry().width()/2-30, self.frameGeometry().height()-75)

	def updatePlot(self):
		if(self.inOxy==1):

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

	def clrGraph(self):
		self.plot0.clear()


def main():
    
	app = QApplication(sys.argv)

	ex = fNIR_GUI()
	
	sys.exit(app.exec_())

		


if __name__ == '__main__':
	main()
    	
