# 统计一致字符串的数目

# 给你一个由不同字符组成的字符串 allowed 和一个字符串数组 words 。如果一个字符串的每一个字符都在 allowed 中，就称这个字符串是 一致字符串 。
# 请你返回 words 数组中 一致字符串 的数目。

from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(allowed)
        r = 0
        for i in words:
            t = set(i)
            if t <= s:  # set 使用 <= 可表示集合的包含。
                r += 1
        return r


c = Solution()
print(c.countConsistentStrings(
    allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
))


