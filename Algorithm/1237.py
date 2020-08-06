# 找出给定方程的正整数解

# 给出一个函数  f(x, y) 和一个目标结果 z，请你计算方程 f(x,y) == z 所有可能的正整数 数对 x 和 y。
# 给定函数是严格单调的，也就是说：
# f(x, y) < f(x + 1, y)
# f(x, y) < f(x, y + 1)


"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

from typing import List

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        # 问题可变描述为：
        # 在行列严格递增矩阵中查某值的所有出现位置
        # 技巧：从左下或右上角可以不遗漏地找出
        r = []
        i, j = 1, 1001
        while i <= 1001 and j >= 1:
            t = customfunction.f(i,j)
            if t < z:
                i += 1
            elif t > z:
                j -= 1
            else:
                r.append([i,j])
                i,j = i+1,j-1
        return r



c = Solution()
print(c.findSolution(nums1=[1,3],nums2=[2]))
