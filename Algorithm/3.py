# 无重复字符的最长子串
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=len(s)
        if l<2:
            return l
        res=0
        for i in range(l):
            k=set(s[i])
            for j in range(i-1,-1,-1):
                if s[j] in k:
                    break
                k.add(s[j])
            res=max(res,len(k))
        return res

c = Solution()
print(c.lengthOfLongestSubstring("cdd"))
