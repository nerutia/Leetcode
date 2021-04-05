# 多数元素

# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        p = 0
        r = -1
        for idx, val in enumerate(nums):
            if idx == 0:
                r = val
                p += 1
            else:
                if val == r:
                    p += 1
                else:
                    p -= 1
                    if p == -1:
                        r = val
                        p = 1
        return r

c = Solution()
print(c.majorityElement(
    nums=[3,2,3]
))

