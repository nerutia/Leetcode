# 下一个更大元素 I

# 给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
# nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        r = []
        for i in range(len(nums1)):
            for j in range(nums2.index(nums1[i])+1,len(nums2)):
                if nums1[i] < nums2[j]:
                    r.append(nums2[j])
                    break
            else:
                r.append(-1)
        return r

        # 更好的做法是先用stack和hashmap把nums2转换成可直接用的结构

c = Solution()
print(c.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))

