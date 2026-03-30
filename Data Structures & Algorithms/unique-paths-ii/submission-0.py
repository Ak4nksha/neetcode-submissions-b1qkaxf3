class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1] * n for  _ in range(m)]
        dp[0][0] = 1

        def f(i, j ):

            if i < 0 or j < 0: return 0

            if i >= 0 and j >= 0 and obstacleGrid[i][j] == 1:
                return 0

            if i == 0 and j == 0: return 1

            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = f(i-1,j) + f(i,j-1)

            return dp[i][j]

        
        return f(m-1,n-1)