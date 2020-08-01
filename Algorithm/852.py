# 山脉数组的峰顶索引

# 我们把符合下列属性的数组 A 称作山脉：

# A.length >= 3
# 存在 0 < i < A.length - 1 使得A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
# 给定一个确定为山脉的数组，返回任何满足 A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1] 的 i 的值。

from typing import List

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        p = 0
        while A[p]<A[p+1]:
            p += 1
        return p




c = Solution()
print(c.peakIndexInMountainArray([0,1,0]))

