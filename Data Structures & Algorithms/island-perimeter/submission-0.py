class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        n = len(grid[0])
        m = len(grid)
        

        visit = set()

        def dfs(i,j):

            if i < 0 or i >= m or j<0 or j>=n or grid[i][j] == 0:
                return 1

            if (i,j) in visit:
                return 0

            visit.add((i,j))
            dir = [(0,1),(0,-1),(1,0),(-1,0)]
            peri = 0

            for r,c in dir:

                peri += dfs(i+r,j+c)

            return peri


        for i in range(m):
            for j in range(n):

                if grid[i][j]:
                    return dfs(i,j)



            

