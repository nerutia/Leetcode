# 重新排列字符串

# 给你一个字符串 s 和一个 长度相同 的整数数组 indices 。
# 请你重新排列字符串 s ，其中第 i 个字符需要移动到 indices[i] 指示的位置。
# 返回重新排列后的字符串。


from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        r = list(s)
        for i in range(len(s)):
            r[indices[i]] = s[i]
        return "".join(r)



c = Solution()
print(c.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))