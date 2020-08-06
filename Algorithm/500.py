# 键盘行

# 给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。

from typing import List

class Solution:
    s1 = set(['q','w','e','r','t','y','u','i','o','p'])
    s2 = set(['a','s','d','f','g','h','j','k','l'])
    s3 = set(['z','x','c','v','b','n','m'])
    def findWords(self, words: List[str]) -> List[str]:
        r = []
        for i in words:
            t = set(i.lower())
            if t.issubset(self.s1):
                r.append(i)
            if t.issubset(self.s2):
                r.append(i)
            if t.issubset(self.s3):
                r.append(i)
        return r


c = Solution()
print(c.findWords(["Hello", "Alaska", "Dad", "Peace"]))