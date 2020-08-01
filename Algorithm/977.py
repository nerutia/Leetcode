# 有序数组的平方

# 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(map(lambda x:x**2, A))



c = Solution()
print(c.sortedSquares([-4,-1,0,3,10]))
