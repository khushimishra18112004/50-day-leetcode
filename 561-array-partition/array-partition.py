class Solution(object):
    def arrayPairSum(self, nums):
        n=len(nums)
        nums.sort()
        max_sum=0
        for i in range(0,n,2):
            max_sum+=nums[i]
        return max_sum    