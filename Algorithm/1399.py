# 统计最大组的数目

# 给你一个整数 n 。请你先求出从 1 到 n 的每个整数 10 进制表示下的数位和（每一位上的数字相加），然后把数位和相等的数字放到同一个组中。
# 请你统计每个组中的数字数目，并返回数字数目并列最多的组有多少个。


class Solution:
    def countLargestGroup(self, n: int) -> int:
        tran = []
        for i in range(1,n+1):
            tl = list(str(i))
            t = 0
            for j in tl:
                t += int(j)
            tran.append(t)
        m = {}
        for i in tran:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        r = 0
        mv = 0
        for a,b in m.items():
            if mv < b:
                r = 1
                mv = b
            elif mv == b:
                r += 1
        return r


c = Solution()
print(c.countLargestGroup(n = 13))
