code = """
__global__ void GpuRipple(unsigned char *data, int *ticks, int *rows, int *columns)
{
        int x = threadIdx.x + blockIdx.x * blockDim.x;
        int y = threadIdx.y + blockIdx.y * blockDim.y;
        int offset = x + y * blockDim.x * gridDim.x;
        
        float fx = x - *rows/2;
        float fy = y - *columns/2;
        float d = sqrtf(fx * fx + fy * fy);
        
        unsigned char grey = (unsigned char)(128.0f + 127.0f * cosf(d/10.0f - *ticks/7.0f) / (d/10.0f + 1.0f));
        
        data[offset * 3 + 0] = grey; /* Red channel.  */
        data[offset * 3 + 1] = grey; /* Green channel.  */
        data[offset * 3 + 2] = grey; /* Blue channel.  */
}
"""
