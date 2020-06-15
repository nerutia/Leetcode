# 重新排列数组

# 给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。
# 请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l = len(candies)
        p = max(candies) - extraCandies
        res = [False for i in range(l)]
        for i in range(l):
            if candies[i] >= p:
                res[i] = True
        return res


c = Solution()
print(c.kidsWithCandies(candies = [4,2,1,1,2], extraCandies = 1))

