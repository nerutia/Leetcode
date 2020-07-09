# 数组中两元素的最大乘积

# 给你一个整数数组 nums，请你选择数组的两个不同下标 i 和 j，使 (nums[i]-1)*(nums[j]-1) 取得最大值。
# 请你计算并返回该式的最大值。

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        at = sorted(map(lambda x:x-1, nums))
        return max(at[0] * at[1], at[-2] * at[-1])


c = Solution()
print(c.maxProduct(nums = [3,4,5,2]))



