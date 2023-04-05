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

class DynamicPlotter:

    def __init__(self, plot, channel, com = "COM3", sampleinterval=0.1, timewindow=10., size=(600, 1000)):
        # Data stuff
        self.ser = serial.Serial(com, 2000000)
        self.interval = int(sampleinterval * 1000)
        self.bufsize = int(timewindow / sampleinterval)
        self.databuffer = collections.deque([0.0] * self.bufsize, self.bufsize)
        self.x = np.linspace(-timewindow, 0.0, self.bufsize)
        self.y = np.zeros(self.bufsize, dtype=float)
        self.channel = channel
        self.ser = serial
        
        # PyQtGraph stuff
        self.plt = plot
        self.plt.setTitle('Champ magnétique en temps réel')
        self.plt.resize(*size)
        self.plt.showGrid(x=True, y=True)
        #self.plt.setXRange(5,20, padding=0)
        self.plt.setLabel('left', 'Champ magnétique', 'µT')
        self.plt.setLabel('bottom', 'Time', 's')
        self.curve = self.plt.plot(self.x, self.y, pen=(255, 0, 0))

        # QTimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateplot)
        self.timer.start(self.interval)

    def getdata(self):
        
        while True:
            try:
                data =  ser.readline().decode("utf-8").strip('\r\n').split(" ")
                B = float(data[self.channel-1])
                break
            except:
                continue
            
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
                DynamicPlotter(plot, channel = i, sampleinterval=0.05, timewindow=8.)
                )
            i += 1

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())

    