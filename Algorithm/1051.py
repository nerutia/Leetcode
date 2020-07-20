# 高度检查器

# 学校在拍年度纪念照时，一般要求学生按照 非递减 的高度顺序排列。
# 请你返回能让所有学生以 非递减 高度排列的最小必要移动人数。
# 注意，当一组学生被选中时，他们之间可以以任何可能的方式重新排序，而未被选中的学生应该保持不动。


from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s = sorted(heights)
        return sum(h1 != h2 for h1, h2 in zip(heights, s))


c = Solution()
print(c.heightChecker(heights = [1,1,4,2,1,3]))
