# 汉明距离

# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
# 给出两个整数 x 和 y，计算它们之间的汉明距离。

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        while x or y:
            res += abs(x%2 - y%2)
            x = x>>1
            y = y>>1
        return res

c = Solution()
print(c.hammingDistance(x = 1, y = 4))





