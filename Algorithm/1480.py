class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a= len(nums)
        b=[0]*a
        for i in range(a):
            if i>0:
                b[i]=b[i-1]+nums[i]
            else:
                b[i]=nums[i]
        return b