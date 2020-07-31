# 解码字母到整数映射

# 给你一个字符串 s，它由数字（'0' - '9'）和 '#' 组成。我们希望按下述规则将 s 映射为一些小写英文字符：

# 字符（'a' - 'i'）分别用（'1' - '9'）表示。
# 字符（'j' - 'z'）分别用（'10#' - '26#'）表示。 
# 返回映射之后形成的新字符串。

# 题目数据保证映射始终唯一。


class Solution:
    def freqAlphabets(self, s: str) -> str:
        r = ""
        i = len(s)-1
        while i != -1:
            if s[i] == '#':
                r += chr(int(s[i-2:i])+96)
                i -= 3
            else:
                r += chr(int(s[i])+96)
                i -= 1
        return r[::-1]

        # 两种精彩写法
        # 1. 使用正则
        # return re.sub(r'\d\d#|\d', lambda x: chr(int(x.group()[:2]) + 96), s)
        # 2. 使用replace
        # for i in ['10#', '11#', '12#', '13#', '14#', '15#', '16#', '17#', '18#', '19#', '20#', '21#','22#', '23#', '24#', '25#', '26#']:
        #     s=s.replace(i, alpha_dict[i])
        # for i in range(1, 10):
        #     s=s.replace(str(i), alpha_dict[str(i)])


c = Solution()
print(c.freqAlphabets(s = "10#11#12"))
