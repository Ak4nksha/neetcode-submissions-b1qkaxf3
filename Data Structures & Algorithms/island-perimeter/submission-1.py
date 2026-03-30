class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        visit = set()

        def dfs(i,j):

            if i<0 or i>= m or j<0 or j>=n or grid[i][j] == 0:
                return 1 
            elif (i,j) in visit:
                return 0


            visit.add((i,j))
            dir = [(0,1),(0,-1),(1,0),(-1,0)]
            peri = 0

            for r,c in dir:
                nr, nc = i + r, j + c
                peri += dfs(nr,nc)
            
            return peri

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    return dfs(i,j)

            

                
