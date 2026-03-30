class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        n = len(s)
        res = []
        part = []

        def isPali(s1):

            i = 0 
            j = len(s1)-1

            while i<j:

                if s1[i] != s1[j]:
                    return False

                i += 1
                j -= 1

            return True

        
        def dfs(i):
            
            if i >= n:
                res.append(part.copy())
                return

            for j in range(i, n):

                s1 = s[i:j+1]
                if isPali(s1):
                    part.append(s1)
                    dfs(j+1)
                    part.pop()

                
        dfs(0)
        return res
        


