# 最小绝对差

# 给你个整数数组 arr，其中每个元素都 不相同。
# 请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。

from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ar = sorted(arr)    
        dist = ar[1] - ar[0]
        r = [[ar[0],ar[1]]]
        for i in range(1, len(ar)-1):
            if ar[i+1] - ar[i] == dist:
                r.append([ar[i],ar[i+1]])
            elif ar[i+1] - ar[i] < dist:
                dist = ar[i+1] - ar[i]
                r = [[ar[i],ar[i+1]]]
        return r



c = Solution()
print(c.minimumAbsDifference(arr = [4,2,1,3]))
