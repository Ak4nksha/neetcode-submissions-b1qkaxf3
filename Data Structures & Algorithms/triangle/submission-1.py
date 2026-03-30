class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        m = len(triangle)
        n = len(triangle[-1])
        prev = [float('inf')]  * n
        

        for j in range(n):
            prev[j] = triangle[m-1][j]

        for i in range(m-2, -1, -1):
            curr = [float('inf')]  * n
            for j in range(i, -1, -1):

                down = triangle[i][j] + prev[j]
                diag = triangle[i][j] + prev[j+1]
                curr[j] = min(down, diag)

            prev = curr

        return prev[0]

            