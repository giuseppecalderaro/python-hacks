import numpy
import sys
# Qt4 import(s)
from PyQt4 import Qt, QtCore, QtGui
# PyCuda import(s)
import pycuda.driver as cuda
import pycuda.autoinit
from cudakernel import mod
###
import MainUI      
    
class ThreadJulia(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent=None)
        self.exiting = False
    def __del__(self):
        self.exiting = True
        self.wait()
    def CpuJulia(self, data):
        self.data = data
        self.start()
    def run(self):
        rows = numpy.shape(self.data)[0]
        columns = numpy.shape(self.data)[1]
        for x in range(rows):
            for y in range(columns):
                self.data[x][y][0] = 0xFF * self.PixelJulia(x, y, rows, columns)
                self.data[x][y][1] = 0
                self.data[x][y][2] = 0
            self.emit(QtCore.SIGNAL("ThreadJuliaUpdateStatus(int)"), (x * 100) / rows)
        self.emit(QtCore.SIGNAL("ThreadJuliaCompleted(PyQt_PyObject)"), self.data)
    def PixelJulia(self, x, y, rows, columns):
        c = numpy.complex(-0.8, 0.156)
        x = 1.5 * (rows/2 - x)/(rows/2)
        y = 1.5 * (columns/2 - y)/(columns/2)
        a = numpy.complex(x, y)
        for i in range(200):
            a = a**2 + c
            if (numpy.abs(a) > 1000):  
                return 0
        return 1
          
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = MainUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.statusBar().showMessage("Ready")
        self.ui.actionOpen.setShortcut("Ctrl+O")
        self.connect(self.ui.actionOpen, QtCore.SIGNAL("triggered()"), self.fileOpen)
        self.connect(self.ui.CpuButton, QtCore.SIGNAL("clicked()"), self.CpuJulia)
        self.connect(self.ui.GpuButton, QtCore.SIGNAL("clicked()"), self.GpuJulia)
        self.ui.CpuButton.setEnabled(False)
        self.ui.GpuButton.setEnabled(False)
        self.ThreadJulia = ThreadJulia()
    def fileOpen(self):
        self.filename = QtGui.QFileDialog.getOpenFileName(parent=None, caption="FileDialog")
        if (self.filename != ""):
            scene = QtGui.QGraphicsScene()
            self.image = QtGui.QImage(self.filename)
            pixmap = QtGui.QPixmap(self.image)
            scene.addPixmap(pixmap.scaled(self.ui.graphicsView.size()))
            self.ui.graphicsView.setScene(scene)
            self.ui.CpuButton.setEnabled(True)
            self.ui.GpuButton.setEnabled(True)
    def CpuJulia(self):
        import qimage2ndarray
        vector = qimage2ndarray.rgb_view(self.image)
        self.ui.progressBar.setVisible(True)
        self.connect(self.ThreadJulia, QtCore.SIGNAL("ThreadJuliaCompleted(PyQt_PyObject)"), self.CompletedJulia)
        self.connect(self.ThreadJulia, QtCore.SIGNAL("ThreadJuliaUpdateStatus(int)"), self.UpdateStatusJulia)
        self.ui.CpuButton.setEnabled(False)
        self.ui.GpuButton.setEnabled(False)
        # Spawn the thread
        self.ThreadJulia.CpuJulia(vector)
    def GpuJulia(self):
        import qimage2ndarray
        # Memory on Host
        # vector = qimage2ndarray.byte_view(self.image)
        vector = qimage2ndarray.rgb_view(self.image)
        single_vector = numpy.copy(vector)
        # Memory on Device
        gpu_alloc = cuda.mem_alloc(single_vector.nbytes)
        # Copy data from Host to Device
        cuda.memcpy_htod(gpu_alloc, single_vector)
        # Execute on host
        kernel = mod.get_function("getJuliaSet")
        kernel(gpu_alloc, block=(1, 1, 1))
        # Copy data from Device to Host
        cuda.memcpy_dtoh(single_vector, gpu_alloc)
        
        # Show final result
        newimage = qimage2ndarray.array2qimage(single_vector)
        newpixmap = QtGui.QPixmap(newimage)
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(newpixmap.scaled(self.ui.graphicsView.size()))
        self.ui.graphicsView.setScene(scene)
    def CompletedJulia(self, data):
        import qimage2ndarray
        self.ui.progressBar.setHidden(True)
        newimage = qimage2ndarray.array2qimage(data)
        newpixmap = QtGui.QPixmap(newimage)
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(newpixmap.scaled(self.ui.graphicsView.size()))
        self.ui.graphicsView.setScene(scene)
        self.ui.CpuButton.setEnabled(True)
        self.ui.GpuButton.setEnabled(True)
    def UpdateStatusJulia(self, status):
        self.ui.progressBar.setValue(status)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())