# 斐波那契数

# 给定 N，计算 F(N)。

class Solution:
    def fib(self, N: int) -> int:
        r = [0,1]
        l = 1
        while l < N:
            r.append(r[-1]+r[-2])
            l += 1
        return r[N]



c = Solution()
print(c.fib(3))
