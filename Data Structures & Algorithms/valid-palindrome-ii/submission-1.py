class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        n = len(s)

        
        def isPal(l,r):

            while l<r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1

            return True

        
        l = 0
        r = n-1

        while l<r:
            if s[l] != s[r]:
                left = isPal(l+1,r)
                right = isPal(l,r-1)

                return left or right

            l += 1
            r -= 1

        return True