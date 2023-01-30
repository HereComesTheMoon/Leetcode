class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
            
        M = (
            (1, 1, 1),
            (1, 0, 0),
            (0, 1, 0)
        )
        return self.fast_pow(M, n - 1)[0][0]

    @cache
    def prod(self, a, b):
        return (
            (
            a[0][0]*b[0][0] + a[0][1]*b[1][0] + a[0][2]*b[2][0],
            a[0][0]*b[0][1] + a[0][1]*b[1][1] + a[0][2]*b[2][1],
            a[0][0]*b[0][2] + a[0][1]*b[1][2] + a[0][2]*b[2][2], 
            ),
            (
            a[1][0]*b[0][0] + a[1][1]*b[1][0] + a[1][2]*b[2][0],
            a[1][0]*b[0][1] + a[1][1]*b[1][1] + a[1][2]*b[2][1],
            a[1][0]*b[0][2] + a[1][1]*b[1][2] + a[1][2]*b[2][2], 
            ),
            (
            a[2][0]*b[0][0] + a[2][1]*b[1][0] + a[2][2]*b[2][0],
            a[2][0]*b[0][1] + a[2][1]*b[1][1] + a[2][2]*b[2][1],
            a[2][0]*b[0][2] + a[2][1]*b[1][2] + a[2][2]*b[2][2], 
            ),
        )

    
    @cache
    def fast_pow(self, x, n):
        if n == 1:
            return x
        if n % 2:
            return self.prod(self.prod(self.fast_pow(x, n // 2), self.fast_pow(x, n // 2)), x)
        return self.prod(self.fast_pow(x, n // 2), self.fast_pow(x, n // 2))