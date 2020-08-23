# 判定是否互为字符重排

# 给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。



class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return sorted(s1) == sorted(s2)



c = Solution()
print(c.CheckPermutation(s1 = "abc", s2 = "bca"))
