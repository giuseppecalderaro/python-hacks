import sys
from PyQt4 import QtGui, QtCore
import pycuda.driver as cuda
import pycuda.autoinit
import numpy
from cudakernel import mod
import array

import MainUI      
        
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = MainUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.statusBar().showMessage("Ready")
        self.ui.actionOpen.setShortcut("Ctrl+O")
        self.connect(self.ui.actionOpen, QtCore.SIGNAL("triggered()"), self.fileOpen)
        self.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.getJulia)
    def fileOpen(self):
        self.filename = QtGui.QFileDialog.getOpenFileName(parent=None, caption="FileDialog")
        if (self.filename != ""):
            scene = QtGui.QGraphicsScene()
            self.image = QtGui.QImage(self.filename)
            pixmap = QtGui.QPixmap(self.image)
            scene.addPixmap(pixmap.scaled(self.ui.graphicsView.size()))
            self.ui.graphicsView.setScene(scene)
    def getJulia(self):
#        a = numpy.random.randn(4, 4)
#        a = a.astype(numpy.float32)
#        a_gpu = cuda.mem_alloc(a.nbytes)
#        cuda.memcpy_htod(a_gpu, a)
#        func = mod.get_function("doublify")
#        func(a_gpu, block=(4,4,1))
#        a_doubled = numpy.empty_like(a)
#        cuda.memcpy_dtoh(a_doubled, a_gpu)
#        print a_doubled
#        print a
        address = int(self.image.bits())
        width = self.image.width()
        height = self.image.height()
        data = [0] * width * height
        gpu_alloc = cuda.mem_alloc(width * height)
        cuda.memcpy_htod(gpu_alloc, address)
        cuda.memcpy_dtoh(data, gpu_alloc)
        newimage = QtGui.QImage(data)
        newpixmap = QtGui.QPixmap(newimage)
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(newpixmap)
        self.ui.graphicsView.setScene(scene)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())