class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        temp=[]
        for i in range(0,n):
            if nums[i]!=0:
                temp.append(nums[i])
        z=len(temp)
        for i in range(0,z):
            nums[i]=temp[i]
        for i in range(z,n):
                nums[i]=0
        return nums                    