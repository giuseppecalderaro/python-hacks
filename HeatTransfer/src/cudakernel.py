code = """
__global__ void HeatTransfer(unsigned char *data, int *ticks, int *rows, int *columns)
{
        int x = threadIdx.x + blockIdx.x * blockDim.x;
        int y = threadIdx.y + blockIdx.y * blockDim.y;
        int offset = x + y * blockDim.x * gridDim.x;
        
        data[offset * 3 + 0] = 0xFF; /* Red channel.  */
        data[offset * 3 + 1] = 0x00; /* Green channel.  */
        data[offset * 3 + 2] = 0x00; /* Blue channel.  */
}
"""
