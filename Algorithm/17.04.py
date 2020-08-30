# 消失的数字

# 数组nums包含从0到n的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗？


from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        return (1+l)*l//2 - sum(nums)


c = Solution()
print(c.missingNumber([3,0,1]))

