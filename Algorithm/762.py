# 二进制表示中质数个计算置位

# 给定两个整数 L 和 R ，找到闭区间 [L, R] 范围内，计算置位位数为质数的整数个数。
# （注意，计算置位代表二进制表示中1的个数。例如 21 的二进制表示 10101 有 3 个计算置位。还有，1 不是质数。）


class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        r = 0
        def f(i):
            if i == 1:
                return False
            if i == 2:
                return True
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    return False
            return True

        for i in range(L,R+1):
            t = bin(i).count('1')
            if f(t):
                print(t)
                r += 1
        return r



c = Solution()
print(c.countPrimeSetBits(L = 842, R = 888))

