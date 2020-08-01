# 矩阵中的幸运数

# 给你一个 m * n 的矩阵，矩阵中的数字 各不相同 。请你按 任意 顺序返回矩阵中的所有幸运数。
# 幸运数是指矩阵中满足同时下列两个条件的元素：
# 在同一行的所有元素中最小
# 在同一列的所有元素中最大

from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        r = []
        mlist = []
        for i in range(len(matrix[0])):
            b = [t[i] for t in matrix]
            mlist.append(max(b))
        print(mlist)
        for i in matrix:
            m = min(i)
            t = 0
            for j in i:
                if j == m and j == mlist[t]:
                    r.append(j)
                t += 1
        return r



c = Solution()
print(c.luckyNumbers(matrix = [[3,7,8],[9,11,13],[15,16,17]]))