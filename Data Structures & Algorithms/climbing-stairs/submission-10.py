class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [-1] * (n+1)
        dp[1] = 1
        if n > 1: dp[2] = 2

        def f(i):

            if i <= 2: 
                return i

            if dp[i] != -1:
                return dp[i]

            one = f(i-1) 
            two = f(i-2) 
            dp[i] = one + two

            return dp[i]


        return f(n)