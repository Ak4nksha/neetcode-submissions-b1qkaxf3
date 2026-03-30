class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        n = len(s)
        if n == 1:
            return True

        l = 0
        r = n-1
        while l<r:

            while l<r and (not s[l].isalnum()):
                l += 1
            while r>l and (not s[r].isalnum()):
                r -= 1

            if l<r:
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                    continue
                else:
                    return False

        return True

        