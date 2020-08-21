# 子域名访问计数

# 一个网站域名，如"discuss.leetcode.com"，包含了多个子域名。
# 作为顶级域名，常用的有"com"，下一级则有"leetcode.com"，最低的一级为"discuss.leetcode.com"。
# 当我们访问域名"discuss.leetcode.com"时，也同时访问了其父域名"leetcode.com"以及顶级域名 "com"。

# 给定一个带访问次数和域名的组合，要求分别计算每个域名被访问的次数。
# 其格式为访问次数+空格+地址，例如："9001 discuss.leetcode.com"。

# 接下来会给出一组访问次数和域名组合的列表cpdomains 。
# 要求解析出所有域名的访问次数，输出格式和输入格式相同，不限定先后顺序。

from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        r = {}
        for i in cpdomains:
            t, s = i.split(" ")
            c = int(t)
            while "." in s:
                if s in r:
                    r[s] += c
                else:
                    r[s] = c
                s = s.split(".", 1)[1]
            if s in r:
                r[s] += c
            else:
                r[s] = c
        res = []
        for a,b in r.items():
            res.append(" ".join([str(b),a]))
        return res


c = Solution()
print(c.subdomainVisits(["9001 discuss.leetcode.com"]))

