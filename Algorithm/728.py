# 自除数

# 自除数 是指可以被它包含的每一位数除尽的数。
# 例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
# 还有，自除数不允许包含 0 。
# 给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。


from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            t = i
            while t != 0:
                a = t % 10
                if a == 0 or i % a != 0:
                    break
                t = t // 10
            if t == 0:
                res.append(i)
        if right == 10000:
            res.append(right)
        return res


c = Solution()
print(c.selfDividingNumbers(left = 1, right = 22))
