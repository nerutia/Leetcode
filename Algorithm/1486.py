# 数组异或操作

# 给你两个整数，n 和 start 。
# 数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。
# 请返回 nums 中所有元素按位异或（XOR）后得到的结果。


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + 2 * i for i in range(n)]
        r = 0
        for i in nums:
            r ^= i
        return r



c = Solution()
print(c.xorOperation(n = 5, start = 0))