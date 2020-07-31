# 和为零的N个唯一整数

# 给你一个整数 n，请你返回 任意 一个由 n 个 各不相同 的整数组成的数组，并且这 n 个数相加和为 0 。

from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [2*i-n+1 for i in range(n)]



c = Solution()
print(c.sumZero(n = 6))

