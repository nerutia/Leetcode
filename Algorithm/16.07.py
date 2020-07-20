# 最大数值

# 编写一个方法，找出两个数字a和b中最大的那一个。不得使用if-else或其他比较运算符。


class Solution:
    def maximum(self, a: int, b: int) -> int:
        # a>b -> k=0
        # a<b -> k=1
        k=((a-b)>>34)&1
        # k=0 -> a
        # k=1 -> b
        return k*b+a*(k^1)


c = Solution()
print(c.maximum(a = 1, b = 2))


