class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        m = len(grid)
        n = len(grid[0])
        ans = 0
        visit = set()

        for i in range(m):
            for j in range(n):

                if grid[i][j] and (i,j) not in visit:
                    cnt = self.dfs(i,j,m,n,grid,visit)
                    ans = max(ans,cnt)
        return ans

    def dfs(self, i,j,m,n,grid,visit):

        if i<0 or i>=m or j<0 or j>=n or grid[i][j] == 0 or (i,j) in visit:
            return 0
        

        visit.add((i,j))
        cnt = 1

        dir = [(0,1),(1,0),(0,-1),(-1,0)]

        for r,c in dir:
            cnt += self.dfs(i+r,j+c,m,n,grid,visit)
        
        return cnt






        return cnt




