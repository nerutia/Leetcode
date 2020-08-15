# 数字的补数

# 给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。


class Solution:
    def findComplement(self, num: int) -> int:
        t = num
        r = 0
        while t:
            t >>= 1
            r = (r<<1) + 1
        return num ^ r


c = Solution()
print(c.findComplement(5))