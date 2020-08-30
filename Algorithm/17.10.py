# 主要元素

# 数组中占比超过一半的元素称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。


from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        r = None
        c = 0
        for i in nums:
            if r == None:
                r = i
                c = 1
            else:
                if r == i:
                    c += 1
                else:
                    c -= 1
                    if c < 0:
                        r = i
                        c = 1
        if 2 * nums.count(r) > len(nums):
            return r
        return -1
            



c = Solution()
print(c.majorityElement([1,2,5,9,5,9,5,5,5]))

