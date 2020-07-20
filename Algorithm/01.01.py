# 判定字符是否唯一

# 实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(astr) == len(set(astr))


c = Solution()
print(c.isUnique("ac"))