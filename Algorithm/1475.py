# 商品折扣后的最终价格

# 给你一个数组 prices ，其中 prices[i] 是商店里第 i 件商品的价格。
# 商店里正在进行促销活动，如果你要买第 i 件商品，那么你可以得到与 prices[j] 相等的折扣，其中 j 是满足 j > i 且 prices[j] <= prices[i] 的 最小下标 ，如果没有满足条件的 j ，你将没有任何折扣。
# 请你返回一个数组，数组中第 i 个元素是折扣后你购买商品 i 最终需要支付的价格。


from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        l = len(prices)
        for i in range(l):
            for j in range(i+1,l):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices


c = Solution()
print(c.finalPrices(prices = [8,4,6,2,3]))
