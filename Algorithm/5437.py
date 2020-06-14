# 不同整数的最少数目
# 给你一个整数数组 arr 和一个整数 k 。现需要从数组中恰好移除 k 个元素，请找出移除后数组中不同整数的最少数目。


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        m = {}
        for i in arr:
            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        r = list(m.values())
        r.sort()
        l = len(r)
        for i in range(l):
            if k < r[i]:
                return l-i
            if k == r[i]:
                return l-i-1
            k = k - r[i]

c = Solution()
print(c.findLeastNumOfUniqueInts(arr=[5,5,4], k=1))
