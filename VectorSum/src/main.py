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

class ThreadVectorSum(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent=None)
        self.exiting = False
    def __del__(self):
        self.exiting = True
        self.wait()
    def VectorSum(self, elements, blocks, operands1, operands2):
        self.elements = elements
        self.blocks = blocks
        self.operands1 = operands1
        self.operands2= operands2
        self.results = numpy.zeros_like(self.operands1)
        self.start()
    def run(self):
        # Init CUDA
        cuda.init()
        # Create CUDA Context
        ctx = pycuda.tools.make_default_context()
        # Memory on Device
        gpu_elements = cuda.mem_alloc(self.elements.nbytes)
        gpu_operands1 = cuda.mem_alloc(self.operands1.nbytes)
        gpu_operands2 = cuda.mem_alloc(self.operands2.nbytes)
        gpu_results = cuda.mem_alloc(self.results.nbytes)
        # Copy data from Host to Device
        cuda.memcpy_htod(gpu_elements, self.elements)
        cuda.memcpy_htod(gpu_operands1, self.operands1)
        cuda.memcpy_htod(gpu_operands2, self.operands2)
        # Execute on host
        mod = SourceModule(code)
        kernel = mod.get_function("VectorSum")
        kernel(gpu_elements, gpu_operands1, gpu_operands2, gpu_results, block=(int(self.elements / self.blocks), 1, 1), grid=(self.blocks, 1))
        # Copy data from Device to Host
        cuda.memcpy_dtoh(self.results, gpu_results)
        ctx.pop()
        self.emit(QtCore.SIGNAL("ThreadVectorSumCompleted(PyQt_PyObject)"), self.results)

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = MainUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.statusBar().showMessage("Ready")
        self.connect(self.ui.playButton, QtCore.SIGNAL("clicked()"), self.start)
        self.connect(self.ui.stopButton, QtCore.SIGNAL("clicked()"), self.stop)
        self.ThreadVectorSum = ThreadVectorSum()
        self.connect(self.ThreadVectorSum, QtCore.SIGNAL("ThreadVectorSumCompleted(PyQt_PyObject)"), self.CompletedSum)
    def start(self):
        # Memory on Host
        self.size = numpy.int32(512)
        self.blocks = 16
        self.operands1 = numpy.random.randn(self.size)
        self.operands2 = numpy.random.randn(self.size)
        self.ThreadVectorSum.VectorSum(self.size, self.blocks, self.operands1, self.operands2)
    def stop(self):
        print "Stop"
    def CompletedSum(self, results):
        for index in range(self.size):
            print("%d: %f + %f = %f" % (index, self.operands1[index], self.operands2[index], results[index]))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
