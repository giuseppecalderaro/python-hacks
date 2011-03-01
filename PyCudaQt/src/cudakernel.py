code = """
__global__ void JuliaGPU(float *vector)
{
        int idx = threadIdx.x + threadIdx.y * 4;
        idx = idx;
}
"""