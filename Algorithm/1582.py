# 二进制矩阵中的特殊位置

# 给你一个大小为 rows x cols 的矩阵 mat，其中 mat[i][j] 是 0 或 1，请返回 矩阵 mat 中特殊位置的数目 。
# 特殊位置 定义：如果 mat[i][j] == 1 并且第 i 行和第 j 列中的所有其他元素均为 0（行和列的下标均 从 0 开始 ），则位置 (i, j) 被称为特殊位置。

from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        mat_transpose = list(map(list, zip(*mat)))
        print(mat_transpose)
        m = len(mat)
        n = len(mat_transpose)
        ml = []
        nl = []
        for i in range(m):
            s = sum(mat[i])
            if s == 1:
                ml.append(i)
        for i in range(n):
            s = sum(mat_transpose[i])
            if s == 1:
                nl.append(i)
        res = 0
        for i in ml:
            for j in nl:
                if mat[i][j] == 1:
                    res += 1
        return res


c = Solution()
print(c.numSpecial(mat = [[1,0,0],
            [0,0,1],
            [1,0,0]]))




