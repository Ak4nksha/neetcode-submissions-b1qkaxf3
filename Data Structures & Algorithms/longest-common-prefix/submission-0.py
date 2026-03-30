class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        n = len(strs)

        if n == 0:
            return ""
        elif n == 1:
            return strs[0]
        
        ans = strs[0]

        for i in range(1,n):

            p = len(ans)
            q = len(strs[i])

            if q == 0:
                return ""
            
            j = 0

            while j<q and j<p:

                if strs[i][j] != ans[j]:
                    break
                else:
                    j+=1
            ans = ans[:j]
        
        return ans
            

             


            
            






