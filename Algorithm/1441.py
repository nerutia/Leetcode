# 用栈操作构建数组

# 给你一个目标数组 target 和一个整数 n。每次迭代，需要从  list = {1,2,3..., n} 中依序读取一个数字。

# 请使用下述操作来构建目标数组 target ：

# Push：从 list 中读取一个新元素， 并将其推入数组中。
# Pop：删除数组中的最后一个元素。
# 如果目标数组构建完成，就停止读取更多元素。
# 题目数据保证目标数组严格递增，并且只包含 1 到 n 之间的数字。

# 请返回构建目标数组所用的操作序列。

# 题目数据保证答案是唯一的。

from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        p = 0
        r = []
        l = []
        for i in range(1, n+1):
            if p >= len(target):
                return r
            l += [i]
            r += ["Push"]
            if l[-1] != target[p]:
                l.pop()
                r += ["Pop"]
            else:
                p += 1
        return r
            




c = Solution()
print(c.buildArray(target = [1,3], n = 3))
