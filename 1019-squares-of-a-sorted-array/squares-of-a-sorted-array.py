class Solution(object):
    def sortedSquares(self, nums):
        n=len(nums)
        result=[]
        for i in range(0,n):
            k=nums[i]*nums[i]
            result.append(k)
        result.sort() 
        return result   
            