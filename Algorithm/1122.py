# 数组的相对排序

# 给你两个数组，arr1 和 arr2，
# arr2 中的元素各不相同
# arr2 中的每个元素都出现在 arr1 中
# 对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。


from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        r = []
        for i in arr2:
            r += [i]*arr1.count(i)
        t = []
        s = set(arr2)
        for i in arr1:
            if i in s:
                continue
            t += [i]
        return r + sorted(t)

        # 大佬做法：
        # arr2 += sorted(set(arr1)-set(arr2))
        # arr1.sort(key=arr2.index)
        # return arr1
        # sort(key=arr2.index) 就是按arr2元素对应的下标顺序进行排序, 类似还比如有sort(key=arr2.len) 按arr2元素的长度进行排序，希望能帮到你。
        # key=arr2.index 可以看成 key=lambda x: arr2.index(x)


c = Solution()
print(c.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))
