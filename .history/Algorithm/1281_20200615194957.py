

from typing import List

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        st = str(n)
        rg = range(len(st))
        li = [int(st[i]) for i in rg]
        pr = 1
        su = 0
        for i in rg:
            pr *= li[i]
            su += li[i]
        return pr - su




c = Solution()
print(c.subtractProductAndSum(n = 234))

