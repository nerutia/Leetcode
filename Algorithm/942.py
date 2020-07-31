# 增减字符串匹配

# 给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。
# 返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有：
# 如果 S[i] == "I"，那么 A[i] < A[i+1]
# 如果 S[i] == "D"，那么 A[i] > A[i+1]

from typing import List

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        r = [0]
        m, M = 0, 0
        for i in S:
            if i == 'I':
                M += 1
                r += [M]
            else:
                m -= 1
                r += [m]
        return [i-m for i in r]



c = Solution()
print(c.diStringMatch("IDID"))