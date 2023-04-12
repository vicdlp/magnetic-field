# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 15:44:02 2023

@author: quantumlab
"""

from pyqtgraph.Qt import QtGui, QtCore, QtWidgets
import gui as gui
import sys
import pyqtgraph as pg
import collections
import numpy as np
import serial
import log

class DynamicPlotter:

    def __init__(self, ser, plot, channel, sampleinterval=0.001, timewindow=10., size=(600, 1000)):
        # Data stuff
        self.ser = ser
        self.interval = int(sampleinterval * 1000)
        self.bufsize = int(timewindow / sampleinterval)
        self.databuffer = collections.deque([0.0] * self.bufsize, self.bufsize)
        self.x = np.linspace(-timewindow, 0.0, self.bufsize)
        self.y = np.zeros(self.bufsize, dtype=float)
        self.channel = channel
        self.logger = log.log()
        
        # PyQtGraph stuff
        self.plt = plot
        self.plt.setTitle('Champ magnétique en temps réel')
        self.plt.resize(*size)
        self.plt.showGrid(x=True, y=True)
        #self.plt.setXRange(5,20, padding=0)
        self.plt.setLabel('left', 'Champ magnétique', 'µT')
        self.curve = self.plt.plot(self.x, self.y, pen=(255, 0, 0))

        # QTimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateplot)
        self.timer.start(self.interval)
        self.counter = 0
        

    def getdata(self):
        self.counter += 1
        while True:
            try:
                data =  self.ser.readline().decode("utf-8").strip('\r\n').split(" ")
                B = float(data[self.channel-1])
                break
            except:
                continue
            
        log.logdata(np.array([format(float(i), '.2f') for i in data]))
        
        # log.debug(self.logger, np.array([format(float(i), '.2f') for i in data]))
            
                
        return B

    def updateplot(self):
        self.databuffer.append(self.getdata())
        self.y[:] = self.databuffer
        self.curve.setData(self.x, self.y)


class MainWindow(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        
        self.setupUi(self)
        self.plots = []
        i = 1
        for plot in (self.ch1PlotWidget, self.ch2PlotWidget, self.ch3PlotWidget):
            self.plots.append(
                DynamicPlotter(ser, plot, channel = i, sampleinterval=0.001, timewindow=.5)
                )
            i += 1
            
        
        
ser = serial.Serial("COM3", 2000000)
app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
ser.close()
    