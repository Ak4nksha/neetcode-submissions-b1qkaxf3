class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        m = len(grid)
        n = len(grid[0])
        cnt = 0
        visit = set()

        for i in range(m):
            for j in range(n):

                if (i,j) not in visit and grid[i][j] == "1":
                    cnt += 1
                    self.dfs(i,j,m,n,grid,cnt,visit)

        return cnt

    def dfs(self,i,j,m,n,grid,cnt,visit):

        if i<0 or i>=m or j<0 or j>=n or grid[i][j] == "0" or (i,j) in visit:
            return

        visit.add((i,j))
        dir = [(0,1),(0,-1),(1,0),(-1,0)]

        for r,c in dir:
            self.dfs(i+r,j+c, m,n,grid,cnt,visit)

        return