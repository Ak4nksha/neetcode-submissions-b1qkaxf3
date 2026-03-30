class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        n = len(s)
        if n == 1:
            return True

        s1 = ""
        for i in range(n):
            if s[i].isalnum():
                s1 = s1 + s[i].lower()
        if s1 == "":
            return True


        l = 0
        r = len(s1)-1
        while l<r:
            if s1[l] == s1[r]:
                l += 1
                r -= 1
                continue
            else:
                return False

        return True

        