# 和为s的连续正数序列

# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

from typing import List

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        r = []
        for l in range(2,target):
            t = target - (l-1)*l/2
            if t <= 0:
                break
            a = t // l
            if a * l == t:
                r.append([int(a+i) for i in range(l)])
        return r[::-1]


c = Solution()
print(c.findContinuousSequence(target = 15))