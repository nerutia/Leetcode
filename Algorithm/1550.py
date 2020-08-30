# 存在连续三个奇数的数组

# 给你一个整数数组 arr，请你判断数组中是否存在连续三个元素都是奇数的情况：如果存在，请返回 true ；否则，返回 false 。

from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        l = len(arr)
        for i in range(l-2):
            if arr[i] & arr[i+1] & arr[i+2] % 2 & 1:
                return True
        return False



c = Solution()
print(c.threeConsecutiveOdds(arr = [2,6,4,1]))

