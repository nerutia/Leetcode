# 6 和 9 组成的最大数字

# 给你一个仅由数字 6 和 9 组成的正整数 num。
# 你最多只能翻转一位数字，将 6 变成 9，或者把 9 变成 6 。
# 请返回你可以得到的最大数字。

class Solution:
    def maximum69Number(self, num: int) -> int:
        s = list(str(num))
        for i in range(len(s)):
            if s[i] == '6':
                s[i] = '9'
                return int("".join(s))
        return num



c = Solution()
print(c.maximum69Number(num = 9669))

