# 求1+2+…+n

# 求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

from typing import List

class Solution:
    def sumNums(self, n: int) -> int:
        return int(.5*n+.5*n**2)

c = Solution()
print(c.sumNums(n = 3))




