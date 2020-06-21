# 有多少小于当前数字的数字

# 给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。
# 换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。
# 以数组形式返回答案。

from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = len(nums)
        m = {}
        for i in nums:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        key = sorted(m.keys())
        s = [0] * len(key)
        for i in range(len(key)-1):
            s[i+1] = s[i] + m[key[i]]
        for i in range(l):
            nums[i] = s[key.index(nums[i])]
        return nums



c = Solution()
print(c.smallerNumbersThanCurrent(nums = [8,1,2,2,3]))



