class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        n_s = len(s)
        n_t = len(t)

        if n_s != n_t: return False

        d1 = {}

        for ch in s:

            if ch not in d1:
                d1[ch] = 0
            else:
                d1[ch] += 1

        d2 = {}
        for ch in t:
            if ch not in d2:
                d2[ch] = 0
            else:
                d2[ch] += 1

        for k,v in d1.items():

            if k not in d2 or d2[k] != v:
                return False

        return True



            
