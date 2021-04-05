#  判断字符串的两半是否相似

#  给你一个偶数长度的字符串 s 。将其拆分成长度相同的两半，前一半为 a ，后一半为 b 。
# 两个字符串 相似 的前提是它们都含有相同数目的元音（'a'，'e'，'i'，'o'，'u'，'A'，'E'，'I'，'O'，'U'）。注意，s 可能同时含有大写和小写字母。
# 如果 a 和 b 相似，返回 true ；否则，返回 false 。


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l = len(s)
        a = s[:l//2]
        b = s[l//2:]
        sp = {'a','e','i','o','u','A','E','I','O','U'}
        ca = 0
        for i in a:
            if i in sp:
                ca += 1
        cb = 0
        for i in b:
            if i in sp:
                cb += 1
        return ca == cb
        



c = Solution()
print(c.halvesAreAlike(
    s = "book"
))