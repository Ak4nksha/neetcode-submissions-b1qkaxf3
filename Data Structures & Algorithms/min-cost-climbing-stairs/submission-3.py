class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.append(0)
        n = len(cost)
        dp = [-1] * n
        dp[0] = cost[0]
        if n > 1:
            dp[1] = cost[1]
        
        def dfs(i):
            if i <= 1:
                return cost[i]
            
            if dp[i] != -1: return dp[i]

            dp[i] = cost[i] + min(dfs(i - 1), dfs(i - 2))
            return dp[i]

        return dfs(n-1)
       
        
        



        