# 反转字符串中的单词 III

# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([word[::-1] for word in s.split(" ")])




c = Solution()
print(c.reverseWords("Let's take LeetCode contest"))