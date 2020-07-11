# 分割平衡字符串

# 在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。
# 给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。
# 返回可以通过分割得到的平衡字符串的最大数量。


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        diff = 0
        res = 0
        for i in s:
            if i == 'L':
                diff += 1
            else:
                diff -= 1
            if diff == 0:
                res += 1
        return res

c = Solution()
print(c.balancedStringSplit(s = "RLRRLLRLRL"))
