#  将每个元素替换为右侧最大元素

#  给你一个数组 arr ，请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用 -1 替换。
# 完成所有替换操作后，请你返回这个数组。

from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        res = [0] * l
        m = None
        for i in range(l):
            if m == None:
                res[l-1-i] = -1
                m = arr[l-1-i]
            else:
                res[l-1-i] = m
                if m < arr[l-1-i]:
                    m = arr[l-1-i]
        return res

c = Solution()
print(c.replaceElements(arr = [17,18,5,4,6,1]))


