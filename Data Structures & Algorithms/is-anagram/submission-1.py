class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        n_s = len(s)
        n_t = len(t)

        if n_s != n_t: return False

        d1 = {}
        d2 = {}

        for i in range(n_s):

            d1[s[i]] = 1 + d1.get(s[i],0)
            d2[t[i]] = 1 + d2.get(t[i], 0)

        return d1 == d2


            
