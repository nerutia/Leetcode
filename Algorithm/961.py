# 重复 N 次的元素

# 在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。
# 返回重复了 N 次的那个元素。

from typing import List

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        s = set()
        for i in A:
            if i in s:
                return i
            s.add(i)


c = Solution()
print(c.repeatedNTimes([1,2,3,3]))
