# 两个数组的交集

# 给定两个数组，编写一个函数来计算它们的交集。

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))



c = Solution()
print(c.intersection(nums1 = [1,2,2,1], nums2 = [2,2]))