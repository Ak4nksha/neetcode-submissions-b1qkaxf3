class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        
        m = len(grid)
        n = len(grid[0])
        visit = [[0]*n for _ in range(m)]
        change = []
        dir = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(i,j):
            
            if i<0 or i>=m or j<0 or j>=n or visit[i][j] or grid[i][j] != "O":
                return

            visit[i][j] = 1
            for r,c in dir:
                dfs(i+r,j+c)
            


        for i in range(m):
            for j in range(n):

                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    if grid[i][j] == "O":
                        dfs(i,j)

        for i in range(m):
            for j in range(n):
                if not visit[i][j] and grid[i][j] == "O":
                    grid[i][j] = "X"






    



