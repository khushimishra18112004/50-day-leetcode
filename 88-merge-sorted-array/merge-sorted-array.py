class Solution(object):
    def merge(self, nums1, m, nums2, n):
        result = []
        i, j = 0, 0
    
        
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
                
        
        while i < m:
            result.append(nums1[i])
            i += 1
            
        
        while j < n:
            result.append(nums2[j])
            j += 1
            
        
        nums1[:] = result