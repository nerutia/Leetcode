# 分式化简

# 有一个同学在学习分式。他需要将一个连分数化成最简分数，你能帮助他吗？
# a0 + 1/(a1 + 1/(a2 + 1/(...)))
# 连分数是形如上图的分式。在本题中，所有系数都是大于等于0的整数。
# 输入的cont代表连分数的系数（cont[0]代表上图的a0，以此类推）。返回一个长度为2的数组[n, m]，使得连分数的值等于n / m，且n, m最大公约数为1。


from typing import List

class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        if len(cont) == 1:
            return [cont[0], 1]
        down, up = 1, cont.pop()
        while len(cont) > 0:
            t = cont.pop()
            down, up = up, down + t * up
        return [up, down]


c = Solution()
print(c.fraction(cont = [3, 2, 0, 2]))

