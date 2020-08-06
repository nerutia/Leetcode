# 配对交换

# 配对交换。编写程序，交换某个整数的奇数位和偶数位，尽量使用较少的指令（也就是说，位0与位1交换，位2与位3交换，以此类推）。


class Solution:
    def exchangeBits(self, num: int) -> int:
        return ((num & 0x55555555) << 1) | ((num & 0xaaaaaaaa) >> 1)



c = Solution()
print(c.exchangeBits(num = 2))