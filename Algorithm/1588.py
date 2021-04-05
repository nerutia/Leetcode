# 所有奇数长度子数组的和

# 给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。
# 子数组 定义为原数组中的一个连续子序列。
# 请你返回 arr 中 所有奇数长度子数组的和 。

# 已评论https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays/comments/
from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        l = len(arr)
        if l == 0:
            return 0
        if l == 1:
            return arr[0]
        if l == 2:
            return arr[0] + arr[1]
        if l % 2 == 0:
            s = sum(arr) * (l // 2)
        else:
            s = sum(arr) * (l // 2 + 1) - sum(arr[1::2])
        return self.sumOddLengthSubarrays(arr[1:-1]) + s

c = Solution()
print(c.sumOddLengthSubarrays(
    arr = [1,4,2,5,3]
))
