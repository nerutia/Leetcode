# 转置矩阵

# 给定一个矩阵 A， 返回 A 的转置矩阵。
# 矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。

from typing import List

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        r = []
        for i in range(len(A[0])):
            r.append([A[j][i] for j in range(len(A))])
            # list的append和加法在这里有效果的不同，
            # 使用加法得到的是[1, 4, 7, 2, 5, 8, 3, 6, 9]，
            # 而使用append才能得到[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        return r
        # 大神一行代码：
        # return zip(*A)
        # 以及：
        # return np.array(A).T.tolist()


c = Solution()
print(c.transpose([[1,2,3],[4,5,6],[7,8,9]]))
