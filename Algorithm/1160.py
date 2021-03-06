# 拼写单词

# 给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
# 假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
# 注意：每次拼写（指拼写词汇表中的一个单词）时，chars 中的每个字母都只能用一次。
# 返回词汇表 words 中你掌握的所有单词的 长度之和。

from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        r = 0
        for i in words:
            f = True
            m = {}
            for t in chars:
                if t in m:
                    m[t] += 1
                else:
                    m[t] = 1
            for j in i:
                if j in m and m[j] > 0:
                    m[j] -= 1
                else:
                    f = False
                    break
            if f:
                r += len(i)
        return r



c = Solution()
print(c.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))