from pycuda.compiler import SourceModule

mod = SourceModule("""
    __global__ void doublify(float *a)
    {
        int idx = threadIdx.x + threadIdx.y * 4;
        a[idx] *= 2;
    }
 """)
