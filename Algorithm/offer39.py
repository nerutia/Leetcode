# 数组中出现次数超过一半的数字

# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        for i in nums:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        a,b = 0, 0
        for i,j in m.items():
            if b < j:
                b = j
                a = i
        return a


        # 很强的一个方法，可行的原因是一个数比其余的数的总和还多。
        # //摩尔投票
        # int count = 0;
        # Integer card = null;
        # for(int num:nums){
        #     if(count == 0) card = num;
        ### 注意这里的加一减一：
        #     count += (card == num)?1:-1;
        # }
        # return card;

c = Solution()
print(c.majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))

