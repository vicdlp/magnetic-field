

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, setConfigOption

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(845, 727)
        setConfigOption('background', 'w')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(360, 0, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.labelCh1 = QtWidgets.QLabel(self.centralwidget)
        self.labelCh1.setGeometry(QtCore.QRect(20, 120, 31, 51))
        self.labelCh1.setObjectName("labelCh1")
        self.labelCh2 = QtWidgets.QLabel(self.centralwidget)
        self.labelCh2.setGeometry(QtCore.QRect(20, 320, 31, 51))
        self.labelCh2.setObjectName("labelCh2")
        self.labelCh3 = QtWidgets.QLabel(self.centralwidget)
        self.labelCh3.setGeometry(QtCore.QRect(20, 520, 31, 51))
        self.labelCh3.setObjectName("labelCh3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 70, 741, 561))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ch1PlotWidget = PlotWidget(self.widget)
        self.ch1PlotWidget.setObjectName("ch1PlotWidget")
        self.gridLayout.addWidget(self.ch1PlotWidget, 0, 0, 1, 1)
        self.ch2PlotWidget = PlotWidget(self.widget)
        self.ch2PlotWidget.setObjectName("ch2PlotWidget")
        self.gridLayout.addWidget(self.ch2PlotWidget, 1, 0, 1, 1)
        self.ch3PlotWidget = PlotWidget(self.widget)
        self.ch3PlotWidget.setObjectName("ch3PlotWidget")
        self.gridLayout.addWidget(self.ch3PlotWidget, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitle.setText(_translate("MainWindow", "Données LSM303DLHC"))
        self.labelCh1.setText(_translate("MainWindow", "Bx"))
        self.labelCh2.setText(_translate("MainWindow", "By"))
        self.labelCh3.setText(_translate("MainWindow", "Bz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())