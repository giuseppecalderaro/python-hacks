import sys
import numpy
import random
import array
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
        random.seed()
        self.numspheres = numpy.int32(10)
        self.rows = numpy.int32(512)
        self.columns = numpy.int32(256)
        self.threads = 16;
    def go(self):
        import qimage2ndarray
        image = QtGui.QImage(self.rows, self.columns, QtGui.QImage.Format_RGB32)
        self.data = qimage2ndarray.rgb_view(image)
        # Needs a contiguos buffer
        self.data = numpy.copy(self.data)
        self.spheres = numpy.array(self.CreateSpheres())
        # Init CUDA
        cuda.init()
        # Create CUDA Context
        ctx = pycuda.tools.make_default_context()
        # Declare event(s)
        startEvent = cuda.Event()
        stopEvent = cuda.Event()
        # Memory on Device
        gpu_alloc = cuda.mem_alloc(self.data.nbytes)
        gpu_rows = cuda.mem_alloc(self.rows.nbytes)
        gpu_columns = cuda.mem_alloc(self.columns.nbytes)
        # Copy data from Host to Device
        cuda.memcpy_htod(gpu_rows, self.rows)
        cuda.memcpy_htod(gpu_columns, self.columns)
        # Execute on host
        mod = SourceModule(code)
        gpu_spheres = mod.get_global("spheres")    
        cuda.memcpy_htod(gpu_spheres[0], self.spheres)
        kernel = mod.get_function("RayTracer")
        startEvent.record()
        kernel(gpu_alloc, gpu_rows, gpu_columns,
               block=(self.threads, self.threads, 1), 
               grid=(int(self.rows / self.threads), int(self.columns / self.threads)))
        stopEvent.record()
        stopEvent.synchronize()
        print("Time elapsed: %fms" % startEvent.time_till(stopEvent))
        # Copy data from Device to Host
        cuda.memcpy_dtoh(self.data, gpu_alloc)
        ctx.pop()
        self.SetImage(self.data)
    def CreateSpheres(self):
        self.spheres_list = array.array('l')
        for index in range(self.numspheres):
            self.spheres_list.append(random.randint(0, 255)) # Red Channel
            self.spheres_list.append(random.randint(0, 255)) # Green Channel
            self.spheres_list.append(random.randint(0, 255)) # Blue Channel
            self.spheres_list.append(random.randint(0, 100)) # Radius
            self.spheres_list.append(random.randint(-(self.rows / 2), self.rows / 2)) # x
            self.spheres_list.append(random.randint(-(self.columns / 2), self.columns / 2)) # y
            self.spheres_list.append(random.randint(0, 256)) # z
        return self.spheres_list
    def SetImage(self, data):
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
    