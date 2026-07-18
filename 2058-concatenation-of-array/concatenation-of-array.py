class Solution(object):
    def getConcatenation(self, nums):
        n=len(nums)
        ans=[]
        for i in range(0,n):
            ans.append(nums[i])
        
        for num in nums:
            ans.append(num)
            
        return ans    


