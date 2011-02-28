import numpy
import sys
# Qt4 import(s)
from PyQt4 import Qt, QtCore, QtGui
# PyCUDA import(s)
import pycuda.driver as cuda
import pycuda.tools
###
import MainUI      
    
class ThreadJulia(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent=None)
        self.exiting = False
    def __del__(self):
        self.exiting = True
        self.wait()
    def Julia(self, data, gpu):
        self.data = data
        self.gpu = gpu
        self.start()
    def run(self):
        if self.gpu == 0:
            self.JuliaCPU()
        elif self.gpu == 1:
            cuda.init()
            gpudev = cuda.Device(0)
            # Memory on Host
            single_data = numpy.copy(self.data)
            # Create CUDA Context
            ctx = pycuda.tools.make_default_context()
            # Memory on Device
            gpu_alloc = cuda.mem_alloc(single_data.nbytes)
            # Copy data from Host to Device
            cuda.memcpy_htod(gpu_alloc, single_data)
            # Execute on host
            from cudakernel import mod
            kernel = mod.get_function("JuliaGPU")
            kernel(gpu_alloc, block=(1, 1, 1))
            # Copy data from Device to Host
            cuda.memcpy_dtoh(single_data, gpu_alloc)
            ctx.pop()
            self.data = single_data
            self.emit(QtCore.SIGNAL("ThreadJuliaCompleted(PyQt_PyObject)"), self.data)
    def JuliaCPU(self):
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
        self.connect(self.ui.StartButton, QtCore.SIGNAL("clicked()"), self.StartJulia)
        self.ui.StartButton.setEnabled(False)
        self.ThreadJulia = ThreadJulia()
    def fileOpen(self):
#        self.filename = QtGui.QFileDialog.getOpenFileName(parent=None, caption="FileDialog")
        self.filename = "/Users/giuseppecalderaro/Downloads/irina.jpg"
        if (self.filename != ""):
            scene = QtGui.QGraphicsScene()
            self.image = QtGui.QImage(self.filename)
            pixmap = QtGui.QPixmap(self.image)
            scene.addPixmap(pixmap.scaled(self.ui.graphicsView.size()))
            self.ui.graphicsView.setScene(scene)
            self.ui.StartButton.setEnabled(True)
    def StartJulia(self):
        import qimage2ndarray
        data = qimage2ndarray.rgb_view(self.image)
        self.ui.progressBar.setVisible(True)
        self.connect(self.ThreadJulia, QtCore.SIGNAL("ThreadJuliaCompleted(PyQt_PyObject)"), self.CompletedJulia)
        self.connect(self.ThreadJulia, QtCore.SIGNAL("ThreadJuliaUpdateStatus(int)"), self.UpdateStatusJulia)
        self.ui.StartButton.setEnabled(False)
        # Spawn the thread
        if self.ui.radioCPU.isChecked():
            self.ThreadJulia.Julia(data, 0)
        else:
            self.ThreadJulia.Julia(data, 1)
    def CompletedJulia(self, data):
        import qimage2ndarray
        self.ui.progressBar.setHidden(True)
        newimage = qimage2ndarray.array2qimage(data)
        newpixmap = QtGui.QPixmap(newimage)
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(newpixmap.scaled(self.ui.graphicsView.size()))
        self.ui.graphicsView.setScene(scene)
        self.ui.StartButton.setEnabled(True)
    def UpdateStatusJulia(self, status):
        self.ui.progressBar.setValue(status)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())