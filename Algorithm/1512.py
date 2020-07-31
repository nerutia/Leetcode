# 好数对的数目

# 给你一个整数数组 nums 。
# 如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。
# 返回好数对的数目。

from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        m = {}
        r = 0
        for i in nums:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        for i,j in m.items():
            r += (j-1)*j//2
        return r



c = Solution()
print(c.numIdenticalPairs(nums = [1,2,3,1,1,3]))

