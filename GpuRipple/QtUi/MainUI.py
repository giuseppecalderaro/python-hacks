# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:/Users/giuseppe/pyhacks/GpuRipple/QtUi/MainUI.ui'
#
# Created: Mon Mar 07 21:22:12 2011
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
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 781, 481))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.playButton = QtGui.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(710, 500, 75, 23))
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.stopButton = QtGui.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(710, 530, 75, 23))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.GpuSyncBox = QtGui.QCheckBox(self.centralwidget)
        self.GpuSyncBox.setGeometry(QtCore.QRect(20, 500, 91, 16))
        self.GpuSyncBox.setObjectName(_fromUtf8("GpuSyncBox"))
        self.SyncedBox = QtGui.QCheckBox(self.centralwidget)
        self.SyncedBox.setGeometry(QtCore.QRect(20, 520, 91, 16))
        self.SyncedBox.setObjectName(_fromUtf8("SyncedBox"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.playButton.setText(QtGui.QApplication.translate("MainWindow", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.GpuSyncBox.setText(QtGui.QApplication.translate("MainWindow", "GPU SyncTest", None, QtGui.QApplication.UnicodeUTF8))
        self.SyncedBox.setText(QtGui.QApplication.translate("MainWindow", "Synced", None, QtGui.QApplication.UnicodeUTF8))

