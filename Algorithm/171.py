# Excel表列序号

# 给定一个Excel表格中的列名称，返回其相应的列序号。

class Solution:
    def titleToNumber(self, s: str) -> int:
        r = 0
        for i in s:
            r *= 26
            r += ord(i)-ord('A')+1
        return r


c = Solution()
print(c.titleToNumber("ZY"))

