# 按奇偶排序数组

# 给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。
# 你可以返回满足此条件的任何数组作为答案。

from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A)-1
        while i < j:
            if A[i] % 2 == 0:
                i += 1
            elif A[j] % 2 == 1:
                j -= 1
            else:
                A[i], A[j] = A[j], A[i]
        return A


c = Solution()
print(c.sortArrayByParity([3,1,2,4]))