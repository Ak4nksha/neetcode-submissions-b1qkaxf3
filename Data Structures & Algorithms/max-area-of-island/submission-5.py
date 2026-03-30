class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        m = len(grid)
        n = len(grid[0])
        ans = 0
        visit = [[0]*n for _ in range(m)]
        

        for i in range(m):
            for j in range(n):

                q = deque()

                if grid[i][j] and not visit[i][j]:
                    q.append((i,j))
                    visit[i][j] = 1
                    cnt = 1
                    dir = [(0,1),(1,0),(-1,0),(0,-1)]
                    while q:
                        row,col = q.popleft()
                        for r,c in dir:
                            nr,nc = row + r, col + c

                            if nr>=0 and nr<m and nc>=0 and nc<n and (not visit[nr][nc]) and grid[nr][nc]:
                                cnt += 1
                                q.append((nr,nc))
                                visit[nr][nc] = 1
                                #ans = max(ans,cnt)  
                    ans = max(ans,cnt)
        
        return ans

