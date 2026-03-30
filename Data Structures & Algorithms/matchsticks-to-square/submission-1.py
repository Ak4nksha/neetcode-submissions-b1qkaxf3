class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        

        n = len(matchsticks)
        total = sum(matchsticks)
        if total % 4 != 0: 
            return False
        else:
            sideLen = total // 4

        if max(matchsticks) > sideLen: return False

        sides = [0] * 4

        def dfs(i):

            if i == n:
                return True
            print("yes")
            for j in range(4):

                if sides[j] + matchsticks[i] <= sideLen:
                    sides[j] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[j] -= matchsticks[i]
            return False


        
        return dfs(0)

            
