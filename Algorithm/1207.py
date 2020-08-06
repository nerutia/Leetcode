# 独一无二的出现次数

# 给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
# 如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        m = {}
        for i in arr:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        a = [i for t,i in m.items()]
        return len(a) == len(set(a))


c = Solution()
print(c.uniqueOccurrences(arr = [1,2,2,1,1,3]))
