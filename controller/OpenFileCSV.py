'''
Created on Nov 2, 2019

@author: diegomota
'''
from PyQt5.QtWidgets import QFileDialog as fd
import os
from controller.Plot import Plot as plt

class OpenFileCSV:   

    def openFileNameDialog(self):
        options = fd.Options()
        options |= fd.DontUseNativeDialog
        myfilename, _filters = fd.getOpenFileName(self,"Escolha um arquivo CSV", "/","CSV Files (*.csv)", options=options)    
        my_fn = myfilename.rstrip(os.sep)
        print(my_fn)
        plt.my_plot(self, myfilename)
        