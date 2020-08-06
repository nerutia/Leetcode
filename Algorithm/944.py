# 删列造序

# 给定由 N 个小写字母字符串组成的数组 A，其中每个字符串长度相等。
# 你需要选出一组要删掉的列 D，对 A 执行删除操作，使 A 中剩余的每一列都是 非降序 排列的，然后请你返回 D.length 的最小可能值。
# 删除 操作的定义是：选出一组要删掉的列，删去 A 中对应列中的所有字符，形式上，第 n 列为 [A[0][n], A[1][n], ..., A[A.length-1][n]]）。（可以参见 删除操作范例）

from typing import List

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        r = 0
        l = len(A[0])
        for i in range(l):
            for j in range(len(A)-1):
                if A[j][i] > A[j+1][i]:
                    break
            else:
                r += 1
        return l - r

        # 学了一手：
        # for i in zip(*A):
        #   print(i)
        # 结果为：
        # ('c', 'd', 'g')
        # ('b', 'a', 'h')
        # ('a', 'f', 'i')
        # 单独使用*A是不行的


c = Solution()
print(c.minDeletionSize(["cba", "daf", "ghi"]))

