# 特殊数组的特征值

# 给你一个非负整数数组 nums 。如果存在一个数 x ，使得 nums 中恰好有 x 个元素 大于或者等于 x ，那么就称 nums 是一个 特殊数组 ，而 x 是该数组的 特征值 。
# 注意： x 不必 是 nums 的中的元素。
# 如果数组 nums 是一个 特殊数组 ，请返回它的特征值 x 。否则，返回 -1 。可以证明的是，如果 nums 是特殊数组，那么其特征值 x 是 唯一的 。


from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        arr = sorted(nums)
        for i in range(len(arr)):
            x = len(arr) - i
            if arr[i] >= x and (i == 0 or arr[i-1] < x):
                return x
        return -1


c = Solution()
print(c.specialArray(nums = [0,4,3,0,4]))


