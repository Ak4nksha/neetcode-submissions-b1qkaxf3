class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        m = len(triangle)
        n = len(triangle[-1])
        dp = [[float('inf')] * n for _ in range(m)]

        for j in range(n):
            dp[m-1][j] = triangle[m-1][j]

        for i in range(m-2, -1, -1):
            for j in range(i, -1, -1):

                down = triangle[i][j] + dp[i+1][j]
                diag = triangle[i][j] + dp[i+1][j+1]
                dp[i][j] = min(down, diag)


        return dp[0][0]

            