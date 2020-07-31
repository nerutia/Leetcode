#  数组拆分 I

#  给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn)，
# 使得从1 到 n 的 min(ai, bi) 总和最大。

from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        t = sorted(nums)
        r = 0
        for i in range(0,len(nums),2):
            r += t[i]
        return r


c = Solution()
print(c.arrayPairSum([1,4,3,2]))