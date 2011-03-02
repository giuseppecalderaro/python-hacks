# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created: Tue Mar  1 23:54:42 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 781, 471))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.StartButton = QtGui.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(660, 510, 114, 32))
        self.StartButton.setObjectName(_fromUtf8("StartButton"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 490, 321, 23))
        self.progressBar.setProperty(_fromUtf8("value"), 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.selectBox = QtGui.QGroupBox(self.centralwidget)
        self.selectBox.setGeometry(QtCore.QRect(530, 490, 120, 80))
        self.selectBox.setTitle(_fromUtf8(""))
        self.selectBox.setObjectName(_fromUtf8("selectBox"))
        self.radioCPU = QtGui.QRadioButton(self.selectBox)
        self.radioCPU.setGeometry(QtCore.QRect(10, 10, 102, 21))
        self.radioCPU.setObjectName(_fromUtf8("radioCPU"))
        self.radioGPU = QtGui.QRadioButton(self.selectBox)
        self.radioGPU.setGeometry(QtCore.QRect(10, 40, 102, 21))
        self.radioGPU.setObjectName(_fromUtf8("radioGPU"))
        self.infoBox = QtGui.QGroupBox(self.centralwidget)
        self.infoBox.setGeometry(QtCore.QRect(339, 490, 181, 80))
        self.infoBox.setTitle(_fromUtf8(""))
        self.infoBox.setObjectName(_fromUtf8("infoBox"))
        self.labelRows = QtGui.QLabel(self.infoBox)
        self.labelRows.setGeometry(QtCore.QRect(10, 0, 101, 20))
        self.labelRows.setObjectName(_fromUtf8("labelRows"))
        self.labelColumns = QtGui.QLabel(self.infoBox)
        self.labelColumns.setGeometry(QtCore.QRect(10, 20, 101, 20))
        self.labelColumns.setObjectName(_fromUtf8("labelColumns"))
        self.labelTime = QtGui.QLabel(self.infoBox)
        self.labelTime.setGeometry(QtCore.QRect(10, 40, 101, 20))
        self.labelTime.setObjectName(_fromUtf8("labelTime"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionStart = QtGui.QAction(MainWindow)
        self.actionStart.setObjectName(_fromUtf8("actionStart"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.StartButton.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.radioCPU.setText(QtGui.QApplication.translate("MainWindow", "CPU", None, QtGui.QApplication.UnicodeUTF8))
        self.radioGPU.setText(QtGui.QApplication.translate("MainWindow", "GPU/CUDA", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRows.setText(QtGui.QApplication.translate("MainWindow", "Rows: -", None, QtGui.QApplication.UnicodeUTF8))
        self.labelColumns.setText(QtGui.QApplication.translate("MainWindow", "Columns: -", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTime.setText(QtGui.QApplication.translate("MainWindow", "Time: -", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))

