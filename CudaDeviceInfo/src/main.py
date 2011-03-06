# PyCUDA import(s)
import pycuda
import pycuda.driver as cuda
from pycuda.driver import device_attribute


if __name__ == '__main__':
    cuda.init()
    gpudev = cuda.Device(0)
    print("CUDA Device Info:")
    print("Cuda Version %s" % pycuda.VERSION_TEXT)
    print("Max Threads per block: %d" % gpudev.get_attribute(device_attribute.MAX_THREADS_PER_BLOCK))
    print("Max Block dim x: %d" % gpudev.get_attribute(device_attribute.MAX_BLOCK_DIM_X))
    print("Max Block dim y: %d" % gpudev.get_attribute(device_attribute.MAX_BLOCK_DIM_Y))
    print("Max Block dim z: %d" % gpudev.get_attribute(device_attribute.MAX_BLOCK_DIM_Z))
    print("Max Grid dim x: %d" % gpudev.get_attribute(device_attribute.MAX_GRID_DIM_X))
    print("Max Grid dim y: %d" % gpudev.get_attribute(device_attribute.MAX_GRID_DIM_Y))
    print("Max Grid dim z: %d" % gpudev.get_attribute(device_attribute.MAX_GRID_DIM_Z))
    print("Total constant memory: %d" % gpudev.get_attribute(device_attribute.TOTAL_CONSTANT_MEMORY))
    print("Warp size: %d" % gpudev.get_attribute(device_attribute.WARP_SIZE))
    print("Max Pitch: %d" % gpudev.get_attribute(device_attribute.MAX_PITCH))
    print("Clock rate: %d" % gpudev.get_attribute(device_attribute.CLOCK_RATE))
    print("Texture alignment: %d" % gpudev.get_attribute(device_attribute.TEXTURE_ALIGNMENT))
    print("GPU Overlap: %d" % gpudev.get_attribute(device_attribute.GPU_OVERLAP))
    print("Multiprocessor count: %d" % gpudev.get_attribute(device_attribute.MULTIPROCESSOR_COUNT))
    print("Max shared memory per block: %d" % gpudev.get_attribute(device_attribute.MAX_SHARED_MEMORY_PER_BLOCK))
    print("Kernel exec timeout: %d" % gpudev.get_attribute(device_attribute.KERNEL_EXEC_TIMEOUT))
    print("Integrated: %d" % gpudev.get_attribute(device_attribute.INTEGRATED))
    print("Can map host memory: %d" % gpudev.get_attribute(device_attribute.CAN_MAP_HOST_MEMORY))
    print("PCI bus id: %d" % gpudev.get_attribute(device_attribute.PCI_BUS_ID))
    print("PCI device id: %d" % gpudev.get_attribute(device_attribute.PCI_DEVICE_ID))