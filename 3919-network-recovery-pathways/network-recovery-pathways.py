from collections import deque

class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n = len(online)
        
        
        filtered_edges = []
        for u, v, cost in edges:
            if online[u] and online[v]:
                filtered_edges.append((u, v, cost))
                
        
        adj_full = [[] for _ in range(n)]
        for u, v, cost in filtered_edges:
            adj_full[u].append((v, cost))
            
       
        if not filtered_edges:
           
            return -1
            
        max_cost = max(cost for u, v, cost in filtered_edges)
        
        def check(min_allowed_edge):
            
            in_degree = [0] * n
            adj = [[] for _ in range(n)]
            
            for u, v, cost in filtered_edges:
                if cost >= min_allowed_edge:
                    adj[u].append((v, cost))
                    in_degree[v] += 1
            
            
            dp = [float('inf')] * n
            dp[0] = 0
            
            
            queue = deque([i for i in range(n) if in_degree[i] == 0])
            
            while queue:
                u = queue.popleft()
                
                for v, cost in adj[u]:
                    if dp[u] != float('inf'):
                        if dp[u] + cost < dp[v]:
                            dp[v] = dp[u] + cost
                    
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        queue.append(v)
            
            return dp[n - 1] <= k

        
        low, high = 0, max_cost
        ans = -1
        
        while low <= high:
            mid = (low + high) // shift_value if 'shift_value' in locals() else (low + high) // 2
            if check(mid):
                ans = mid       
                low = mid + 1
            else:
                high = mid - 1  
                
        return ans