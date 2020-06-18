# 统计作战单位数

#  n 名士兵站成一排。每个士兵都有一个 独一无二 的评分 rating 。

# 每 3 个士兵可以组成一个作战单位，分组规则如下：

# 从队伍中选出下标分别为 i、j、k 的 3 名士兵，他们的评分分别为 rating[i]、rating[j]、rating[k]
# 作战单位需满足： rating[i] < rating[j] < rating[k] 或者 rating[i] > rating[j] > rating[k] ，其中  0 <= i < j < k < n
# 请你返回按上述条件可以组建的作战单位数量。每个士兵都可以是多个作战单位的一部分。


from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        l = len(rating)
        if l < 3:
            return 0
        minv = rating[0]
        maxv = rating[0]
        minn, maxn = 0, 0
        for i in rating:
            if minv >= i:
                minv = i
                minn += 1
            if maxv <= i:
                maxv = i
                maxn += 1
        print(minn, maxn)
        return minn*(minn-1)*(minn-2)/6 + maxn*(maxn-1)*(maxn-2)/6


c = Solution()
print(c.numTeams(rating = [2,5,3,4,1]))





