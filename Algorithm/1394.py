# 找出数组中的幸运数

# 在整数数组中，如果一个整数的出现频次和它的数值大小相等，我们就称这个整数为「幸运数」。
# 给你一个整数数组 arr，请你从中找出并返回一个幸运数。
# 如果数组中存在多个幸运数，只需返回 最大 的那个。
# 如果数组中不含幸运数，则返回 -1 。

from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        s = set(arr)
        r = [-1]
        for i in s:
            if i == arr.count(i):
                r.append(i)
        return max(r)



c = Solution()
print(c.findLucky(arr = [2,2,3,4]))
