# 子矩形查询

# 请你实现一个类 SubrectangleQueries ，它的构造函数的参数是一个 rows x cols 的矩形（这里用整数矩阵表示），
# 并支持以下两种操作：
# 1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)
# 用 newValue 更新以 (row1,col1) 为左上角且以 (row2,col2) 为右下角的子矩形。
# 2. getValue(int row, int col)
# 返回矩形中坐标 (row,col) 的当前值。
from typing import List

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rect = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                self.rect[i][j] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rect[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
obj = SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]])
obj.updateSubrectangle(0, 0, 3, 2, 5)
param_2 = obj.getValue(0, 2)

print(param_2)
