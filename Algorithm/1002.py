# 查找常用字符

# 给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
# 例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
# 你可以按任意顺序返回答案。

from typing import List

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        r = []
        c = A[0]
        ex = set()
        for ch in c:
            if ch in ex:
                continue
            ex.add(ch)
            t = c.count(ch)
            for st in A:
                if t <= 0:
                    break
                t = min(t, st.count(ch))
            r += [ch] * t
        return r


c = Solution()
print(c.commonChars(["bella","label","roller"]))
