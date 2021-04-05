# 矩阵对角线元素的和

# 给你一个正方形矩阵 mat，请你返回矩阵对角线元素的和。
# 请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。

from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l = len(mat)
        r = 0
        for i in range(l):
            r += mat[i][i] + mat[i][l-i-1]
        if l % 2:
            r -= mat[l//2][l//2]
        return r


c = Solution()
print(c.diagonalSum(
    mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]
))

