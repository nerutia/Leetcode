# 去掉最低工资和最高工资后的工资平均值

# 给你一个整数数组 salary ，数组里每个数都是 唯一 的，其中 salary[i] 是第 i 个员工的工资。
# 请你返回去掉最低工资和最高工资以后，剩下员工工资的平均值。

from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        # 也可以：
        # salary.remove(max(salary))
        salary.pop(salary.index(min(salary)))
        salary.pop(salary.index(max(salary)))
        return sum(salary)/len(salary)
        # 一步：
        # return (sum(salary)-max(salary)-min(salary)) / (len(salary)-2)


c = Solution()
print(c.average(salary = [4000,3000,1000,2000]))

