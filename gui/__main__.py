'''
Created on Oct 30, 2019

@author: diegomota
'''
from PyQt5.QtCore import pyqtSlot
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from gui.PlotCanvas import PlotCanvas
from controller.OpenFileCSV import OpenFileCSV as ofcsv

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.title = 'Athletech 2.0'
        self.width = 640
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        plotcanvas = PlotCanvas(self, width=5, height=4)

        button = QPushButton('Abrir arquivo CVS', self)
        button.setToolTip('Clique para abrir arquivo')
        button.move(500,0)
        button.resize(140,100)
        button.clicked.connect(self.on_click)  
        
        filelabel = QLabel(self)
        filelabel.move(500,100)
        filelabel.setText('ex')
        filelabel.show()

        self.show()

    @pyqtSlot()
    def on_click(self):
        ofcsv.openFileNameDialog(self)
    
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
