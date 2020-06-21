# 访问所有点的最小时间

# 平面上有 n 个点，点的位置用整数坐标表示 points[i] = [xi, yi]。请你计算访问所有这些点需要的最小时间（以秒为单位）。

# 你可以按照下面的规则在平面上移动：

# 每一秒沿水平或者竖直方向移动一个单位长度，或者跨过对角线（可以看作在一秒内向水平和竖直方向各移动一个单位长度）。
# 必须按照数组中出现的顺序来访问这些点。


from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        l = len(points)-1
        for i in range(l):
            res += self.dist(points[i], points[i+1])
        return res

    def dist(self, a, b):
        return max(abs(a[0]-b[0]),abs(a[1]-b[1]))

c = Solution()
print(c.minTimeToVisitAllPoints(points = [[1,1],[3,4],[-1,0]]))



