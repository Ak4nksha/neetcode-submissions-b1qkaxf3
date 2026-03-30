class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        stack = []
        m = len(board)
        n = len(board[0])
        x = len(word)
        vis = [[False for _ in range(n)] for _ in range(m)]
        #print(vis)

        def dfs(i,j,idx):

            if idx == x:
                return True

            if i < 0 or i == m or j < 0 or j == n or (idx < x and board[i][j] != word[idx]) or vis[i][j]:
                return False

            vis[i][j] = True
            dir = [(0,1),(0,-1),(1,0),(-1,0)]

            for r,c in dir:
                res = dfs(i+r, j+c, idx+1)

                if res:
                    vis[i][j] = False
                    return True
            vis[i][j] = False
            return False


        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True

        return False


            
                