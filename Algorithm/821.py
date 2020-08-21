# 字符的最短距离

# 给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。

from typing import List

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        pos = [i for i,x in enumerate(S) if x == C]
        r = list(range(len(S)))
        for i in r:
            r[i] = min([abs(j-i) for j in pos])
        return r
        return [min([abs(j-i) for j in pos]) for i in r]


c = Solution()
print(c.shortestToChar(S = "loveleetcode", C = 'e'))

