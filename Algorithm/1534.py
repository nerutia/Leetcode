# 统计好三元组

# 给你一个整数数组 arr ，以及 a、b 、c 三个整数。请你统计其中好三元组的数量。
# 如果三元组 (arr[i], arr[j], arr[k]) 满足下列全部条件，则认为它是一个 好三元组 。
# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# 其中 |x| 表示 x 的绝对值。

# 返回 好三元组的数量 。

from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        l = len(arr)
        r = 0
        for i in range(l-2):
            for j in range(i+1,l-1):
                if abs(arr[i]-arr[j]) > a:
                    continue
                for k in range(j+1,l):
                    if abs(arr[j]-arr[k]) > b:
                        continue
                    if abs(arr[i]-arr[k]) > c:
                        continue
                    r += 1
        return r


c = Solution()
print(c.countGoodTriplets(arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3))


