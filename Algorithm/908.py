# 最小差值 I

# 给你一个整数数组 A，请你给数组中的每个元素 A[i] 都加上一个任意数字 x （-K <= x <= K），从而得到一个新数组 B 。
# 返回数组 B 的最大值和最小值之间可能存在的最小差值。

from typing import List

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(0, max(A)-min(A)-2*K)

c = Solution()
print(c.smallestRangeI(A = [1], K = 0))