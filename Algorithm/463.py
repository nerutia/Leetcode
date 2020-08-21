# 岛屿的周长

# 给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
# 网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
# 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r = 0
        a,b = len(grid), len(grid[0])
        for i in range(a):
            for j in range(b):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0:
                        r += 1
                    if j == 0 or grid[i][j-1] == 0:
                        r += 1
                    if i == a-1 or grid[i+1][j] == 0:
                        r += 1
                    if j == b-1 or grid[i][j+1] == 0:
                        r += 1
        return r


c = Solution()
print(c.islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))

