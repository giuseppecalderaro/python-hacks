# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created: Thu Feb 24 22:22:39 2011
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
        self.CpuButton = QtGui.QPushButton(self.centralwidget)
        self.CpuButton.setGeometry(QtCore.QRect(160, 510, 114, 32))
        self.CpuButton.setObjectName(_fromUtf8("CpuButton"))
        self.CpuButton.setDisabled(True)
        self.GpuButton = QtGui.QPushButton(self.centralwidget)
        self.GpuButton.setGeometry(QtCore.QRect(500, 510, 114, 32))
        self.GpuButton.setObjectName(_fromUtf8("GpuButton"))
        self.GpuButton.setDisabled(True)
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(270, 490, 231, 23))
        self.progressBar.setProperty(_fromUtf8("value"), 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.progressBar.setMinimum(0)
        self.progressBar.setHidden(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionCPU = QtGui.QAction(MainWindow)
        self.actionCPU.setObjectName(_fromUtf8("actionCPU"))
        self.actionGPU = QtGui.QAction(MainWindow)
        self.actionGPU.setObjectName(_fromUtf8("actionGPU"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.CpuButton.setText(QtGui.QApplication.translate("MainWindow", "CPU", None, QtGui.QApplication.UnicodeUTF8))
        self.GpuButton.setText(QtGui.QApplication.translate("MainWindow", "GPU", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCPU.setText(QtGui.QApplication.translate("MainWindow", "CPU", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGPU.setText(QtGui.QApplication.translate("MainWindow", "GPU", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))

