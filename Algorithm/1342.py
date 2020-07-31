# 将数字变成 0 的操作次数

# 给你一个非负整数 num ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。


class Solution:
    def numberOfSteps(self, num: int) -> int:
        r = 0
        while num != 0:
            r += num % 2
            if num == 1:
                break
            num >>= 1
            r += 1
        return r


c = Solution()
print(c.numberOfSteps(num = 14))