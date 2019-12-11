'''
Created on Nov 2, 2019

@author: diegomota
'''
import matplotlib.pyplot as plt
import csv
from numpy import double
 
class Plot:
    
    def my_plot(self, myselected_file):
                
        with open(myselected_file,'r') as csvfile:
            x = []
            y = []

            plots = csv.reader(csvfile, delimiter=';')
            for row in plots:
                x.append(double(row[0]))
                y.append(double(row[1]))   
            plt.plot(x, y, label='CSV')
            plt.xlabel('Tempo milisegundos')
            plt.ylabel('Vetor X do acelerometro')
            # plt.title('Salto 1 TEMPO x Vetor X')
            plt.legend()
            plt.show()
            del x[:], y[:]    
    