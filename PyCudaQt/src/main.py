import numpy
import sys
# Qt4 import(s)
from PyQt4 import Qt, QtCore, QtGui
# PyCUDA import(s)
from pycuda.compiler import SourceModule
import pycuda.driver as cuda
import pycuda.tools
from cudakernel import code
###
import MainUI      
    
class ThreadJulia(QtCore.QThread):
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent=None)
        self.exiting = False
    def __del__(self):
        self.exiting = True
        self.wait()
    def Julia(self, data, gpu=False):
        self.data = data
        self.gpu = gpu
        self.rows = numpy.shape(self.data)[0]
        self.columns = numpy.shape(self.data)[1]
        self.start()
    def run(self):
        if self.gpu is False:
            self.JuliaCPU()
        else:
            self.JuliaGPU()
    def JuliaCPU(self):
        for x in range(self.rows):
            for y in range(self.columns):
                julia = self.JuliaPixel(x, y, self.rows, self.columns)
                self.data[x][y][0] *= julia # Red channel
                self.data[x][y][1] *= julia # Green channel 
                self.data[x][y][2] *= julia # Blue channel
            self.emit(QtCore.SIGNAL("ThreadJuliaUpdateStatus(int)"), (x * 100) / self.rows)
        self.emit(QtCore.SIGNAL("ThreadJuliaCompleted(PyQt_PyObject)"), self.data)
    def JuliaPixel(self, x, y, rows, columns):
        c = numpy.complex(-0.8, 0.156)
        x = 1.5 * (rows/2 - x)/(rows/2)
        y = 1.5 * (columns/2 - y)/(columns/2)
        a = numpy.complex(x, y)
        for i in range(200):
            a = a**2 + c
            if (numpy.abs(a) > 1000):  
                return 0
        return 1
    def JuliaGPU(self):
        # Init CUDA
        cuda.init()
        # Create CUDA Context
        ctx = pycuda.tools.make_default_context()
        # Memory on Host
        single_data = numpy.copy(self.data)
        # Memory on Device
        gpu_alloc = cuda.mem_alloc(single_data.nbytes)
        # Copy data from Host to Device
        cuda.memcpy_htod(gpu_alloc, single_data)
        # Execute on host
        mod = SourceModule(code)
        self.kernel = mod.get_function("JuliaGPU")
        self.kernel(gpu_alloc, block=(1, 1, 1), grid=(self.rows, self.columns))
        # Copy data from Device to Host
        cuda.memcpy_dtoh(single_data, gpu_alloc)
        ctx.pop()
        self.data = single_data
        self.emit(QtCore.SIGNAL("ThreadJuliaCompleted(PyQt_PyObject)"), self.data)
          
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = MainUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.statusBar().showMessage("Ready")
        self.ui.actionOpen.setShortcut("Ctrl+O")
        self.ui.actionSave.setShortcut("Ctrl+S")
        self.connect(self.ui.actionOpen, QtCore.SIGNAL("triggered()"), self.fileOpen)
        self.connect(self.ui.actionSave, QtCore.SIGNAL("triggered()"), self.fileSave)
        self.connect(self.ui.StartButton, QtCore.SIGNAL("clicked()"), self.StartJulia)
        self.ui.progressBar.setVisible(False)
        self.ui.StartButton.setEnabled(False)
        self.ThreadJulia = ThreadJulia()
    def fileOpen(self):
        filename = QtGui.QFileDialog.getOpenFileName(parent=None, caption="FileDialog")
        if (filename != ""):
            scene = QtGui.QGraphicsScene()
            self.image = QtGui.QImage(filename)
            rows = self.image.height()
            columns = self.image.width()
            self.ui.labelRows.setText("Rows: " + str(rows))
            self.ui.labelColumns.setText("Columns: " + str(columns))
            pixmap = QtGui.QPixmap(self.image)
            scene.addPixmap(pixmap)
            self.ui.graphicsView.setScene(scene)
            if (rows < 512):
                self.ui.graphicsView.resize(columns + 10, rows + 10)
            self.ui.StartButton.setEnabled(True)
    def fileSave(self):
        filename = QtGui.QFileDialog.getSaveFileName(parent=None, caption="Save")
        self.image.save(filename)
    def StartJulia(self):
        import qimage2ndarray
        data = qimage2ndarray.rgb_view(self.image)
        self.connect(self.ThreadJulia, QtCore.SIGNAL("ThreadJuliaCompleted(PyQt_PyObject)"), self.CompletedJulia)
        self.connect(self.ThreadJulia, QtCore.SIGNAL("ThreadJuliaUpdateStatus(int)"), self.UpdateStatusJulia)
        self.ui.progressBar.setVisible(True)
        self.ui.StartButton.setEnabled(False)
        # Spawn the thread
        self.time = QtCore.QTime()
        self.time.start()
        self.ThreadJulia.Julia(data, self.ui.radioGPU.isChecked())
    def CompletedJulia(self, data):
        import qimage2ndarray
        elapsed = self.time.elapsed()
        if elapsed > 1000000:
            self.ui.labelTime.setText("Time: %ds" % (self.time.elapsed() / 1000))
        else:
            self.ui.labelTime.setText("Time: %dms" % self.time.elapsed())
        self.ui.progressBar.setHidden(True)
        self.image = qimage2ndarray.array2qimage(data)
        pixmap = QtGui.QPixmap(self.image)
        scene = QtGui.QGraphicsScene()
        scene.addPixmap(pixmap)
        self.ui.graphicsView.setScene(scene)
        self.ui.StartButton.setEnabled(True)
    def UpdateStatusJulia(self, status):
        self.ui.progressBar.setValue(status)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())