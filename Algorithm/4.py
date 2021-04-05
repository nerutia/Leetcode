# 寻找两个正序数组的中位数

# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
# 请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 你可以假设 nums1 和 nums2 不会同时为空。

# TODO

from typing import List
class Solution:
    def findK(self, a1, a2, k):
        if a1 == []:
            return a2[k]
        if a2 == []:
            return a1[k]
        if k == 0:
            return min(a1[0], a2[0])
        p = k // 2
        l1 = len(a1)
        l2 = len(a2)
        if p > l1 or a1[p] < a2[p]:
            return self.findK(a1[p:], a2, k-p)
        else:
            return self.findK(a1, a2[p:], k-p)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        p1 = (l1 + l2) // 2
        p2 = (l1 + l2 - 1) // 2
        return (self.findK(nums1, nums2, p1) + self.findK(nums1, nums2, p2)) / 2
        

c = Solution()
print(c.findMedianSortedArrays(nums1=[1,3],nums2=[9]))






