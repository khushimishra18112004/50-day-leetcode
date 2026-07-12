class Solution(object):
    def shuffle(self, nums, n):
        k = len(nums)
        shuffled = []  
        
        for i in range(0, n):
            shuffled.append(nums[i])      
            shuffled.append(nums[i + n]) 
            
        return shuffled  