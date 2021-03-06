import sys
import numpy
# Qt4 import(s)
from PyQt4 import QtCore, QtGui
# PyCUDA import(s)
import pycuda.driver as cuda
import pycuda.tools
from pycuda.compiler import SourceModule
from cudakernel import code

import MainUI

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = MainUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.statusBar().showMessage("Ready")
        self.ui.playButton.setEnabled(True)
        self.connect(self.ui.playButton, QtCore.SIGNAL("clicked()"), self.play)
        self.ui.stopButton.setEnabled(False)
        self.connect(self.ui.stopButton, QtCore.SIGNAL("clicked()"), self.stop)
        self.timer = QtCore.QTimer()
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.TimerExpired)
        self.ui.GpuSyncBox.setEnabled(True)
        self.connect(self.ui.GpuSyncBox, QtCore.SIGNAL("stateChanged(int)"), self.GpuSyncFn)
        self.ui.SyncedBox.setEnabled(False)
        self.connect(self.ui.SyncedBox, QtCore.SIGNAL("stateChanged(int)"), self.SyncedFn)
    def play(self):
        # qimage2ndarray import(s)
        import qimage2ndarray
        self.ui.GpuSyncBox.setEnabled(False)
        self.ui.SyncedBox.setEnabled(False)
        self.ui.playButton.setEnabled(False)
        self.ui.stopButton.setEnabled(True)
        self.rows = numpy.int32(512)
        self.columns = numpy.int32(256)
        self.threads = 16
        image = QtGui.QImage(self.rows, self.columns, QtGui.QImage.Format_RGB32)
        self.data = qimage2ndarray.rgb_view(image)
        # Needs a contiguos buffer
        self.data = numpy.copy(self.data)
        self.ticks = numpy.zeros(1, dtype=numpy.int32);
        self.timer.start(16.667)
    def stop(self):
        self.timer.stop()
        self.ui.playButton.setEnabled(True)
        self.ui.stopButton.setEnabled(False)
        self.ui.GpuSyncBox.setEnabled(True)
        if self.ui.GpuSyncBox.isChecked():
            self.ui.SyncedBox.setEnabled(True)
        else:
            self.ui.SyncedBox.setEnabled(False)
    def SetImage(self, data):
        # qimage2ndarray import(s)
        import qimage2ndarray
        image = qimage2ndarray.array2qimage(data)
        pixmap = QtGui.QPixmap(image)
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(pixmap)
        self.ui.graphicsView.setScene(scene)
    def TimerExpired(self):
        # Init CUDA
        cuda.init()
        # Create CUDA Context
        ctx = pycuda.tools.make_default_context()
        # Memory on Device
        gpu_alloc = cuda.mem_alloc(self.data.nbytes)
        gpu_ticks = cuda.mem_alloc(self.ticks.nbytes)
        # Copy data from Host to Device
        cuda.memcpy_htod(gpu_ticks, self.ticks)
        # Execute on host
        mod = SourceModule(code)
        if self.ui.GpuSyncBox.isChecked():
            if self.ui.SyncedBox.isChecked():
                self.synced = numpy.ones(1, dtype=numpy.int32);
            else:
                self.synced = numpy.zeros(1, dtype=numpy.int32);
            gpu_synced = cuda.mem_alloc(self.synced.nbytes)
            cuda.memcpy_htod(gpu_synced, self.synced)
            kernel = mod.get_function("GpuSync")
            kernel(gpu_alloc, gpu_ticks, gpu_synced, block=(self.threads, self.threads, 1),
                                                     grid=(int(self.rows) / self.threads,
                                                           int(self.columns) / self.threads))
        else:
            gpu_rows = cuda.mem_alloc(self.rows.nbytes)
            gpu_columns = cuda.mem_alloc(self.columns.nbytes)
            cuda.memcpy_htod(gpu_rows, self.rows)
            cuda.memcpy_htod(gpu_columns, self.columns)
            kernel = mod.get_function("GpuRipple")
            kernel(gpu_alloc, gpu_ticks, gpu_rows, gpu_columns, block=(self.threads, self.threads, 1),
                                                                grid=(int(self.rows) / self.threads,
                                                                      int(self.columns) / self.threads))
        # Copy data from Device to Host
        cuda.memcpy_dtoh(self.data, gpu_alloc)
        ctx.pop()
        self.ticks += 1
        self.SetImage(self.data)
    def GpuSyncFn(self, status):
        if self.ui.GpuSyncBox.isChecked():
            self.ui.SyncedBox.setEnabled(True)
        else:
            self.ui.SyncedBox.setEnabled(False)
    def SyncedFn(self, status):
        if self.ui.SyncedBox.isChecked():
            self.ui.GpuSyncBox.setEnabled(False)
        else:
            self.ui.GpuSyncBox.setEnabled(True)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
