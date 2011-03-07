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

__global__ void GpuSync(unsigned char *data, int *ticks, int *synced)
{
#define PI 3.1415926535897932f

        int x = threadIdx.x + blockIdx.x * blockDim.x;
        int y = threadIdx.y + blockIdx.y * blockDim.y;
        int offset = x + y * blockDim.x * gridDim.x;
        
        const float period = 128.0f;
        __shared__ float shared [16][16];
        
        shared[threadIdx.x][threadIdx.y] = 
                                            255 * (sinf(x * 2.0f * PI / period) + 1.0f) *
                                            (sinf(y * 2.0f * PI / period) + 1.0f) / 4.0f;
        
        if (*synced)
            __syncthreads();
        
        data[offset * 3 + 0] = 0; /* Red channel.  */
        data[offset * 3 + 1] = shared[15 - threadIdx.x][15 - threadIdx.y]; /* Green channel.  */
        data[offset * 3 + 2] = 0; /* Blue channel.  */
}
"""
