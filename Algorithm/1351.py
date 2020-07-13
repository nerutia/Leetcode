# 统计有序矩阵中的负数

# 给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 

# 请你统计并返回 grid 中 负数 的数目。

from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        l = len(grid)
        res = 0
        for i in range(l):
            for j in range(len(grid[i])):
                if grid[i][j] >= 0:
                    res += 1
                else:
                    break
        return l*len(grid[0]) - res


c = Solution()
print(c.countNegatives(grid = [[3,2],[1,0]]))


