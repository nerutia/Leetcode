# 重塑矩阵

# 在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。
# 给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。
# 重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。
# 如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

from typing import List

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        a,b = len(nums),len(nums[0])
        if a * b != r * c:
            return nums
        s = []
        for i in nums:
            s += i
        res = []
        for i in range(r):
            res.append(s[c*i:c*i+c])
        return res



c = Solution()
print(c.matrixReshape(nums = [[1,2],[3,4]], r = 1, c = 4))
