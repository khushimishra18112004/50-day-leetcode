class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        if n == 0:
            return ""
        longest = ""
        for i in range(0, n):
            for j in range(n - 1, i - 1, -1):
                if s[i] == s[j]:
                    substring = s[i : j + 1]
                    
                    if substring == substring[::-1]:
                        longest = max(longest, substring, key=len)
                        break  
        return longest
        
        