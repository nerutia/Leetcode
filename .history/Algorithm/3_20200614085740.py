# 无重复字符的最长子串
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l == 0:
            return 0
        ms = 1
        for a in range(l-1):
            p = s[a+1:].find(s[a])
            ms = max(ms, p-a)
        return ms



Solution.lengthOfLongestSubstring("abcabcbb")
