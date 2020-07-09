# 判断能否形成等差数列

# 给你一个数字数组 arr 。
# 如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为 等差数列 。
# 如果可以重新排列数组形成等差数列，请返回 true ；否则，返回 false 。

from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return True
        arrTemp = sorted(arr)
        print(arrTemp)
        diff = arrTemp[1] - arrTemp[0]
        for i in range(len(arrTemp)-1):
            if arrTemp[i+1] - arrTemp[i] != diff:
                return False
        return True

c = Solution()
print(c.canMakeArithmeticProgression(arr = [3,5,1]))

