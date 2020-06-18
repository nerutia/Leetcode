# 统计位数为偶数的数字

# 给你一个整数数组 nums，请你返回其中位数为 偶数 的数字的个数。

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                res += 1
        return res

c = Solution()
print(c.findNumbers(nums = [12,345,2,6,7896]))





