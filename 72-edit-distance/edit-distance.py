class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        
        # dp[i][j] will hold the minimum edit distance 
        # to convert word1[0...i-1] to word2[0...j-1]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base Cases:
        # Converting word1[0...i-1] to empty string word2 requires i deletions
        for i in range(m + 1):
            dp[i][0] = i
            
        # Converting empty string word1 to word2[0...j-1] requires j insertions
        for j in range(n + 1):
            dp[0][j] = j
            
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # Characters match: no new operations needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Minimum of:
                    # 1. Insert:  dp[i][j - 1] + 1
                    # 2. Delete:  dp[i - 1][j] + 1
                    # 3. Replace: dp[i - 1][j - 1] + 1
                    dp[i][j] = 1 + min(
                        dp[i][j - 1],      # Insert
                        dp[i - 1][j],      # Delete
                        dp[i - 1][j - 1]   # Replace
                    )
                    
        return dp[m][n]