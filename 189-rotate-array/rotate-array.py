class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        if k == 0:
            return
         
        left = 0
        right = n - k
        
        while k > 0 and left < right:
            
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right += 1
            
            if right == n:
                k = k % (n - left)
                right = n - k
            
            elif left == right:
                right = n - k