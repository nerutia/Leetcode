# 奇数值单元格的数目

# 给你一个 n 行 m 列的矩阵，最开始的时候，每个单元格中的值都是 0。
# 另有一个索引数组 indices，indices[i] = [ri, ci] 中的 ri 和 ci 分别表示指定的行和列（从 0 开始编号）。
# 你需要将每对 [ri, ci] 指定的行和列上的所有单元格的值加 1。
# 请你在执行完所有 indices 指定的增量操作后，返回矩阵中 「奇数值单元格」 的数目。

from typing import List

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        ma, mb = {}, {}
        ra, rb = 0, 0
        for i in indices:
            a,b = i
            if a in ma:
                ma[a] ^= 1
            else:
                ma[a] = 1
                
            if b in mb:
                mb[b] ^= 1
            else:
                mb[b] = 1
        ra = list(ma.values()).count(1)
        rb = list(mb.values()).count(1)
        return ra*m+rb*n-2*ra*rb


c = Solution()
print(c.oddCells(n = 2, m = 3, indices = [[0,1],[1,1]]))
