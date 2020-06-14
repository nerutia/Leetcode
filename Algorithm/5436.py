# 一维数组的动态和
# 给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。
# 请返回 nums 的动态和。

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l = len(nums)
        for i in range(l):
            if i > 0:
                nums[i] = nums[i-1] + nums[i]
        return nums

c = Solution()
print(c.runningSum(nums=[5,5,4]))
