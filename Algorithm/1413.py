# 逐步求和得到正数的最小值

# 给你一个整数数组 nums 。你可以选定任意的 正数 startValue 作为初始值。
# 你需要从左到右遍历 nums 数组，并将 startValue 依次累加上 nums 数组中的值。
# 请你在确保累加和始终大于等于 1 的前提下，选出一个最小的 正数 作为 startValue 。


from typing import List
from more_itertools.recipes import accumulate

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # for i in range(1, len(nums)):
        #     nums[i] += nums[i-1]
        # return max(-min(nums), 0) + 1

        ### 可一行：
        return max(-min(accumulate(nums)), 0) + 1


c = Solution()
print(c.minStartValue(nums = [-3,2,-3,4,2]))

