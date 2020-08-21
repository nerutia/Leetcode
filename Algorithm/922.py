# 按奇偶排序数组 II

# 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
# 对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
# 你可以返回任何满足上述条件的数组作为答案。

from typing import List

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        a = [i for i in A if not i % 2]
        b = [i for i in A if i % 2]
        r = []
        for i in range(len(a)):
            r.append(a[i])
            r.append(b[i])
        return r
        # 最后合并可只用一步：
        # return [i for j in zip(a,b) for i in j]

        

c = Solution()
print(c.sortArrayByParityII([4,2,5,7,6,3,8,9]))

