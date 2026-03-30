class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        ans = 0
        #visit = [[0]*n for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 2:
                    q.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh += 1

        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:

            row,col,t = q.popleft()

            for r,c in dir:
                nr,nc = row+r,col+c

                if nr<0 or nr>=m or nc<0 or nc>=n or grid[nr][nc] != 1:
                    continue

                grid[nr][nc] = 2
                q.append((nr,nc,t+1))
                fresh -= 1
            
            ans = max(ans,t)

        
        return -1 if fresh else ans

                



