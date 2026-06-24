class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9 + 7
        m = r - l + 1
        
        if n == 1:
            return m
        
        def multiply(A, B):
            size = len(A)
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                for k in range(size):
                    if A[i][k] == 0:
                        continue
                    for j in range(size):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C

        def power(A, p):
            size = len(A)
            res = [[0] * size for _ in range(size)]
            for i in range(size):
                res[i][i] = 1
            base = A
            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                p //= 2
            return res
        
        size = 2 * m
        T = [[0] * size for _ in range(size)]
        
        for x in range(m):
            for y in range(x + 1, m):
                T[m + y][x] = 1
            for y in range(x):
                T[y][m + x] = 1

        T_pow = power(T, n - 1)
        
        initial = [1] * size
        
        ans = 0
        for i in range(size):
            sum_row = 0
            for j in range(size):
                sum_row = (sum_row + T_pow[i][j] * initial[j]) % MOD
            ans = (ans + sum_row) % MOD
            
        return ans