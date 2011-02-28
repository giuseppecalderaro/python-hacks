from pycuda.compiler import SourceModule

mod = SourceModule("""
    __global__ void JuliaGPU(float *vector)
    {
        int idx = threadIdx.x + threadIdx.y * 4;
    }
 """)
