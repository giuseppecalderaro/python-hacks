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
        self.ui.pushButton.setEnabled(True)
        self.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.go)
    def go(self):
        import qimage2ndarray
        self.spheres = 20
        self.rows = 512
        self.columns = 256
        image = QtGui.QImage(self.rows, self.columns, QtGui.QImage.Format_RGB32)
        self.data = qimage2ndarray.rgb_view(image)
        # Needs a contiguos buffer
        self.data = numpy.copy(self.data)
        # Init CUDA
        cuda.init()
        # Create CUDA Context
        ctx = pycuda.tools.make_default_context()
        # Memory on Device
        gpu_alloc = cuda.mem_alloc(self.data.nbytes)
        # Execute on host
        mod = SourceModule(code)
        kernel = mod.get_function("RayTracer")
        kernel(gpu_alloc, block=(1, 1, 1), grid=(self.rows, self.columns))
        # Copy data from Device to Host
        cuda.memcpy_dtoh(self.data, gpu_alloc)
        ctx.pop()
        self.SetImage(self.data)
        print "Go!!!"
    def SetImage(self, data):
        # qimage2ndarray import(s)
        import qimage2ndarray
        image = qimage2ndarray.array2qimage(data)
        pixmap = QtGui.QPixmap(image)
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(pixmap)
        self.ui.graphicsView.setScene(scene)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
    