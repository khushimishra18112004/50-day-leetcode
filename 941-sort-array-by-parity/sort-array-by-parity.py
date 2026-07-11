class Solution(object):
    def sortArrayByParity(self, nums):
        n=len(nums)
        temp=[]
        num=[]
        for i in range(0,n):
            if nums[i]%2==0:
                temp.append(nums[i])
            else:
                 num.append(nums[i])   
        z=len(temp)        
        for i in range(0,z):
            nums[i]=temp[i]
        for i in range(z,n):
            nums[i]=num[i-z]
        return nums        
        


        