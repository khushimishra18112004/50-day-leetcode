class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        freq={}
        for i in range(0,n+1):
            freq[i]=0
        for num in nums:
            freq[num]=1
        for key,value in freq.items():
            if value==0:
               return key        

        