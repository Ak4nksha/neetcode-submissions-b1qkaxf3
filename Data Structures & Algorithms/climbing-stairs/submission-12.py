class Solution:
    def climbStairs(self, n: int) -> int:
        
        # dp = [-1] * (n+1)
        # dp[1] = 1
        # if n > 1: dp[2] = 2

        if n <= 2: return n

        prev2 = 1
        prev = 2

        for i in range(3,n+1):
            
            curr = prev2 + prev
            prev2 = prev
            prev = curr

        return prev