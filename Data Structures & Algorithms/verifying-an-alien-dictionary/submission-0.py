class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        n = len(words)
        d = {}
        for idx, val in enumerate(order):
            d[val] = idx


        for i in range(n-1):
            m = len(words[i])
            for j in range(m):

                if j >= len(words[i+1]): #apple and app
                    return False

                if words[i][j] != words[i+1][j]:
                    if d[words[i][j]] > d[words[i+1][j]]:
                        return False
                    break

        
        return True

                