# 宝石与石头

#  给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。
# S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
# J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。

from typing import List

class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        l = len(guess)
        res = 0
        for i in range(l):
            if guess[i] == answer[i]:
                res = res + 1
        return res


c = Solution()
print(c.game(guess = [1,2,3], answer = [1,2,3]))



