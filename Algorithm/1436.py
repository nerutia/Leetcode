# 旅行终点站

# 给你一份旅游线路图，该线路图中的旅行线路用数组 paths 表示，其中 paths[i] = [cityAi, cityBi] 表示该线路将会从 cityAi 直接前往 cityBi 。请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市。
# 题目数据保证线路图会形成一条不存在循环的线路，因此只会有一个旅行终点站。

from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        l = len(paths)
        inp = set()
        outp = set()
        for i in range(l):
            inp.add(paths[i][0])
            outp.add(paths[i][1])
        res = outp - inp
        return list(res)[0]


c = Solution()
print(c.destCity(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
