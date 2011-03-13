code = """
#define INF 2e10f
#define SPHERES 10

struct sphere {
    int r; /* Red channel.  */
    int g; /* Green channel.  */
    int b; /* Blue channel.  */
    int radius; /* Radius.  */
    int x; /* Centre x.  */
    int y; /* Centre y.  */
    int z; /* Centre z.  */
};
__device__ __constant__ struct sphere spheres[SPHERES];

__device__ float hit(struct sphere *sphere, float ox, float oy, float *n)
{
    float dx = ox - sphere->x;
    float dy = oy - sphere->y;
    float radius = sphere->radius;
    if (dx * dx + dy * dy < radius * radius) {
        float dz = sqrtf(radius * radius - dx * dx - dy * dy);
        *n = dz / sqrtf(radius * radius);
        
        return dz + sphere->z;
    }
    return -INF;
}

__global__ void RayTracer(unsigned char *data, int *rows, int *columns)
{
    int x = threadIdx.x + blockIdx.x * blockDim.x;
    int y = threadIdx.y + blockIdx.y * blockDim.y;
    int offset = x + y * blockDim.x * gridDim.x;

    float ox = (x - *rows / 2);
    float oy = (y - *columns / 2);
    float r = 0, g = 0, b = 0;
    float maxz = -INF;
    for(int i = 0; i < SPHERES; i++) {
        float n;
        float t = hit(&spheres[i], ox, oy, &n);
        if (t > maxz) {
            r = spheres[i].r * n;
            g = spheres[i].g * n;
            b = spheres[i].b * n;
        }
    }

    data[offset * 3 + 0] = r; /* Red channel.  */
    data[offset * 3 + 1] = g; /* Green channel.  */
    data[offset * 3 + 2] = b; /* Blue channel.  */
}
"""
