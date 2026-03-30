from collections import Counter

''' 
window | +char | -char | matched change
lec | +c | - | matched = 1
eca | +a | -l | matched = 2
caa | +a | -e | matched = 1
aab | +b | -c | matched = 1
abc | +c | -a | matched = 3  ✓ Matched == Need -> return True
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        n = len(s1)
        if len(s2) < n: return False

        need = Counter(s1)
        have = {}
        reqd = len(need.keys())
        matched = 0
        #window_size = n

        def add(ch):
            nonlocal matched
            if ch not in need: return

            before = have.get(ch,0)
            if before == need[ch]:
                matched -= 1

            after = 1 + before
            if after == need[ch]:
                matched += 1
            have[ch] = after
            
        def remove(ch):
            nonlocal matched
            if ch not in need: return 
            before = have.get(ch,0)
            if before == need[ch]:
                matched -= 1

            after = before - 1
            if after == need[ch]:
                matched += 1

            if after == 0:
                del have[ch]
            else:
                have[ch] = after

        for i in range(n):  #initial window
            add(s2[i])

        if matched == reqd: return True

        for r in range(n,len(s2)):
            add(s2[r])
            remove(s2[r-n])
            if matched == reqd:
                return True

        return False




        


        




        
