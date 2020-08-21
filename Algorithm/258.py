# 各位相加

# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。



class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum([int(i) for i in list(str(num))])
        return num

### 不使用循环或者递归，且在 O(1) 时间复杂度内:
# 假如一个三位数'abc'，其值大小为s1 = 100 * a + 10 * b + 1 * c，
# 经过一次各位相加后，变为s2 = a + b + c，减小的差值为(s1 -s2) = 99 * a + 9 * b，
# 差值可以被9整除，每一个循环都这样，缩小了9的倍数。当num小于9，即只有一位时，直接返回num，
# 大于9时，如果能被9整除，则返回9（因为不可能返回0也不可能返回两位数及以上的值）
        # if num > 9:
        #     num = num % 9
        #     if num == 0:
        #         return 9
        # return num


c = Solution()
print(c.addDigits(38))

