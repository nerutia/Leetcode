# 距离顺序排列矩阵单元格

# 给出 R 行 C 列的矩阵，其中的单元格的整数坐标为 (r, c)，满足 0 <= r < R 且 0 <= c < C。
# 另外，我们在该矩阵中给出了一个坐标为 (r0, c0) 的单元格。
# 返回矩阵中的所有单元格的坐标，并按到 (r0, c0) 的距离从最小到最大的顺序排，其中，两单元格(r1, c1) 和 (r2, c2) 之间的距离是曼哈顿距离，|r1 - r2| + |c1 - c2|。（你可以按任何满足此条件的顺序返回答案。）

from typing import List

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        r = []
        m = {}
        for i in range(R):
            for j in range(C):
                d = abs(r0-i) + abs(c0-j)
                if d in m:
                    m[d] += [[i, j]]
                else:
                    m[d] = [[i, j]]
        for k in sorted(m):
            r += m[k]
        return r




c = Solution()
print(c.allCellsDistOrder(R = 1, C = 2, r0 = 0, c0 = 0))

