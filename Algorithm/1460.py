# 通过翻转子数组使两个数组相等

# 给你两个长度相同的整数数组 target 和 arr 。
# 每一步中，你可以选择 arr 的任意 非空子数组 并将它翻转。你可以执行此过程任意次。
# 如果你能让 arr 变得与 target 相同，返回 True；否则，返回 False 。

from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        m = {}
        for i in target:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        for i in arr:
            if i in m:
                m[i] -= 1
                if m[i] < 0:
                    return False
            else:
                return False
        return True


c = Solution()
print(c.canBeEqual(target = [1,2,3,4], arr = [2,4,1,3]))
