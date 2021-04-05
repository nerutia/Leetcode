# 交替合并字符串

# 给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。

# 返回 合并后的字符串 。



class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        r = []
        for i, j in zip(word1, word2):
            r += i + j
        l = len(word1) - len(word2)
        r = ''.join(r)
        if l > 0:
            return r + word1[-l:]
        elif l < 0:
            return r + word2[l:]
        else:
            return r

c = Solution()
print(c.mergeAlternately(
    word1 = "ab", word2 = "pqrs"
))