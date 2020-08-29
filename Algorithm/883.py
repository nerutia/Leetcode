# 三维形体投影面积

# 在 N * N 的网格中，我们放置了一些与 x，y，z 三轴对齐的 1 * 1 * 1 立方体。
# 每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。
# 现在，我们查看这些立方体在 xy、yz 和 zx 平面上的投影。
# 投影就像影子，将三维形体映射到一个二维平面上。
# 在这里，从顶部、前面和侧面看立方体时，我们会看到“影子”。
# 返回所有三个投影的总面积。

from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        down,left,front = 0,[],[]
        for i in grid:
            down += len(i) - i.count(0)
            left += [max(i)]
            if front == []:
                front = i
            else:
                if len(i) > len(front):
                    for j in range(len(front)):
                        i[j] = max(i[j],front[j])
                    front = i
                else:
                    for j in range(len(i)):
                        front[j] = max(i[j],front[j])
        return down + sum(left) + sum(front)


c = Solution()
print(c.projectionArea([[2]]))

