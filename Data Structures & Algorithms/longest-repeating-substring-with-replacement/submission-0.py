class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        d = dict()
        l,r = 0,0 
        ans = 0

        while r < n:

            if s[r] not in d:
                d[s[r]] = 1
            else:
                d[s[r]] += 1

            print(d)
            max_v = max(d.values())
            window = r-l+1

            print(max_v, window)

            if window - max_v <= k:
                ans = max(ans,window)
                r += 1
                continue
            
            while l < r:

                d[s[l]] -= 1
                l += 1
                max_v = max(d.values())
                window = r-l+1

                if window - max_v <= k:
                    ans = max(ans,window)
                    r += 1
                    break

        return ans           






            






