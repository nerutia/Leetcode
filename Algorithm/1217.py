# 玩筹码

# 数轴上放置了一些筹码，每个筹码的位置存在数组 chips 当中。
# 你可以对 任何筹码 执行下面两种操作之一（不限操作次数，0 次也可以）：
# 将第 i 个筹码向左或者右移动 2 个单位，代价为 0。
# 将第 i 个筹码向左或者右移动 1 个单位，代价为 1。
# 最开始的时候，同一位置上也可能放着两个或者更多的筹码。
# 返回将所有筹码移动到同一位置（任意位置）上所需要的最小代价。

from typing import List

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        p = [i%2 for i in position]
        return min(p.count(0),p.count(1))


c = Solution()
print(c.minCostToMoveChips([1,2,3]))