# 子矩形查询

# 请你实现一个类 SubrectangleQueries ，它的构造函数的参数是一个 rows x cols 的矩形（这里用整数矩阵表示），
# 并支持以下两种操作：
# 1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)
# 用 newValue 更新以 (row1,col1) 为左上角且以 (row2,col2) 为右下角的子矩形。
# 2. getValue(int row, int col)
# 返回矩形中坐标 (row,col) 的当前值。

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):


    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:


    def getValue(self, row: int, col: int) -> int:



# Your SubrectangleQueries object will be instantiated and called as such:
obj = SubrectangleQueries(rectangle)
obj.updateSubrectangle(row1,col1,row2,col2,newValue)
param_2 = obj.getValue(row,col)

print(param_2)
