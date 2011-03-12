code = """
__global__ void RayTracer(unsigned char *data)
{
        int x = threadIdx.x + blockIdx.x * blockDim.x;
        int y = threadIdx.y + blockIdx.y * blockDim.y;
        int offset = x + y * blockDim.x * gridDim.x;
        
        data[offset * 3 + 0] = 0; /* Red channel.  */
        data[offset * 3 + 1] = 0; /* Green channel.  */
        data[offset * 3 + 2] = 0; /* Blue channel.  */
}
"""
