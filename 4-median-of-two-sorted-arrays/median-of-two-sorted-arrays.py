class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        i, j = 0, 0
        merged = []
        
       
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        
        
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1
            
        
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1
            
        total_len = len(merged)
        mid = total_len // 2
        
        
        if total_len % 2 != 0:
            return float(merged[mid])
        else:
            return (merged[mid - 1] + merged[mid]) / 2.0