# 和为s的两个数字

# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set(nums)
        for i in s:
            if 2*i == target:
                continue
            if target - i in s:
                return [i,target-i]

        # 这题是可以用双指针的

c = Solution()
print(c.twoSum(nums = [2,7,11,15], target = 9))
