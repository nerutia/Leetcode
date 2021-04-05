# 唯一元素的和

# 给你一个整数数组 nums 。数组中唯一元素是那些只出现 恰好一次 的元素。
# 请你返回 nums 中唯一元素的 和 。
from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum([(i if nums.count(i)==1 else 0) for i in nums])



c = Solution()
print(c.sumOfUnique(
    nums = [1,1,1,1,1]
))