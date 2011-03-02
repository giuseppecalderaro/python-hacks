code = """
struct cuComplex {
    float r;
    float i;
    cuComplex(float a, float b) : r(a), i(b) {}
    __device__ float magnitude2(void) {
        return r * r + i * i;
    }
    __device__ cuComplex operator*(const cuComplex &a) {
        return cuComplex(r * a.r - i * a.i, i * a.r + r * a.i);
    }
    __device__ cuComplex operator+(const cuComplex &a) {
        return cuComplex(r + a.r, i + a.i);
    }
};

__device__ int PixelJulia(int x, int y, int rows, int columns)
{
    const float scale = 1.5;
    float jx = scale * (float)((rows / 2) - x)/(rows / 2);
    float jy = scale * (float)((columns / 2) - y)/(columns / 2);
    int i;
    
    cuComplex c(-0.8, 0.156);
    cuComplex a(jx, jy);
    for (i = 0; i < 200; i++) {
        a = a * a + c;
        if (a.magnitude2() > 1000)
            return 0;
    }
    return 1;
}

__global__ void JuliaGPU(unsigned char *data)
{
        int x = blockIdx.x;
        int rows = gridDim.x;
        int y = blockIdx.y;
        int columns = gridDim.y;
        int offset = y + x * columns;
        
        int value = PixelJulia(x, y, rows, columns);
        data[offset * 3 + 0] *= value; /* Red channel.  */
        data[offset * 3 + 1] *= value; /* Green channel.  */
        data[offset * 3 + 2] *= value; /* Blue channel.  */
}
"""