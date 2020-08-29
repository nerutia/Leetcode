# 托普利茨矩阵

# 如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 托普利茨矩阵 。
# 给定一个 M x N 的矩阵，当且仅当它是托普利茨矩阵时返回 True。


from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        a = len(matrix)
        b = len(matrix[0])
        for i in range(a):
            for j in range(i):
                matrix[i].insert(b,matrix[j][b-1])
        for i in range(a):
            for j in range(i+1,a):
                matrix[i].insert(0,matrix[j][0])
        for i in range(a-1):
            if not matrix[i]==matrix[i+1]:
                return False
        return True

        # 大佬做法：判断上一行去掉最后一个元素 和 下一行去掉第一个元素是否相等即可

c = Solution()
print(c.isToeplitzMatrix(matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]))
