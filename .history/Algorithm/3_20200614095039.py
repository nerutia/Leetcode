# 无重复字符的最长子串
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=len(s)
        # if l<2:
        #     return l
        res=0
        for i in range(l+1):
            for j in range(i):
                print(s[j:i])
                if len(set(s[j:i])) == len(s[j:i]):
                    res=max(res,len(s[j:i]))
        return res

c = Solution()
print(c.lengthOfLongestSubstring(""))
