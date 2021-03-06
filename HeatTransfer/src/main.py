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
        self.ui.startButton.setEnabled(True)
        self.connect(self.ui.startButton, QtCore.SIGNAL("clicked()"), self.start)
        self.ui.stopButton.setEnabled(False)
        self.connect(self.ui.stopButton, QtCore.SIGNAL("clicked()"), self.stop)
        self.timer = QtCore.QTimer()
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.TimerExpired)
    def start(self):
        # qimage2ndarray import(s)
        import qimage2ndarray
        self.ui.startButton.setEnabled(False)
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
        self.ui.startButton.setEnabled(True)
        self.ui.stopButton.setEnabled(False)
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
        kernel = mod.get_function("HeatTransfer")
        kernel(gpu_alloc, gpu_ticks, block=(self.threads, self.threads, 1),
                                     grid=(int(self.rows) / self.threads,
                                     int(self.columns) / self.threads))
        # Copy data from Device to Host
        cuda.memcpy_dtoh(self.data, gpu_alloc)
        ctx.pop()
        self.ticks += 1
        self.SetImage(self.data)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())