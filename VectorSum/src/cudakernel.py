code = """
__global__ void VectorSum(int *elements, double *vector1, double *vector2, double *results)
{
    int index = threadIdx.x + blockIdx.x * blockDim.x;
    
    while (index < *elements) {
        results[index] = vector1[index] + vector2[index];
        index += blockDim.x * gridDim.x;
    }
}

__global__ void AnimationGPU(double *operand1, double *operand2)
{
        int x = blockIdx.x;
        
        x = x;
}
"""
