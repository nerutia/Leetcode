# 两个数组间的距离值

# 给你两个整数数组 arr1 ， arr2 和一个整数 d ，请你返回两个数组之间的 距离值 。
# 「距离值」 定义为符合此距离要求的元素数目：对于元素 arr1[i] ，
# 不存在任何元素 arr2[j] 满足 |arr1[i]-arr2[j]| <= d 。

from typing import List

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        r = 0
        p = set(arr2)
        for i in arr1:
            f = 0
            for j in p:
                if abs(i-j) <= d:
                    f = 1
                    break
            if f == 0:
                r += 1
        return r

c = Solution()
print(c.findTheDistanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2))