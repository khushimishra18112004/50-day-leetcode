from collections import Counter

class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = Counter(nums)
        max_len = 0
        
       
        if 1 in counts:
            max_len = counts[1] if counts[1] % 2 != 0 else counts[1] - 1
            
        
        for x in counts:
            if x == 1:
                continue
                
            current_len = 0
            curr = x
            
            while curr in counts:
                
                if counts[curr] >= 2:
                    if curr * curr in counts:
                        current_len += 2
                        curr = curr * curr
                    else:
                        
                        current_len += 1
                        break
                
                elif counts[curr] == 1:
                    current_len += 1
                    break
            
            max_len = max(max_len, current_len)
            
        return max_len