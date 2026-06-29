class Solution(object):
    def sortArray(self, nums):
        
        if len(nums) <= 1:
            return nums
        
        
        mid = len(nums) // 2
        
        
        left_arr = nums[:mid]
        right_arr = nums[mid:]
        
       
        left = self.sortArray(left_arr)
        right = self.sortArray(right_arr)
        
        
        return self.merge_arr(left, right)
    
    def merge_arr(self, left, right):
        result = []
        i, j = 0, 0
        n, m = len(left), len(right)
        
        while i < n and j < m:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        
        while i < n:
            result.append(left[i])
            i += 1
        while j < m:
            result.append(right[j])
            j += 1
            
        return result