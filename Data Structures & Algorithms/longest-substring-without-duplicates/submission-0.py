class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        d = {}
        n = len(s)
        start = 0
        end = 0
        i = 0
        ans = 0

        while i < n and end < n:

            ch = s[i]

            if ch not in d:
                d[ch] = i
                i += 1
                end += 1

            else:

                ans = max(ans, end - start)
                while start <= end and ch in d:
                    del d[s[start]]
                    start += 1
                d[ch] = i
                #ans = max(ans, end-start)
                i += 1
                end += 1

        return max(ans, end-start)


       

