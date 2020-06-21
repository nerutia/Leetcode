# 在既定时间做作业的学生人数

# 给你两个整数数组 startTime（开始时间）和 endTime（结束时间），并指定一个整数 queryTime 作为查询时间。
# 已知，第 i 名学生在 startTime[i] 时开始写作业并于 endTime[i] 时完成作业。
# 请返回在查询时间 queryTime 时正在做作业的学生人数。形式上，返回能够使 queryTime 处于区间 [startTime[i], endTime[i]]（含）的学生人数。

from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        res = 0
        l = len(startTime)
        for i in range(l):
            if startTime[i]<=queryTime and queryTime<=endTime[i]:
                res += 1
        return res


c = Solution()
print(c.busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 4))





