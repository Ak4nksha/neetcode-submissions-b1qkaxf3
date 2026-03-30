# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        l = 1
        r = n+1
        
        while l<=r:

            i = l + (r-l)//2
            m = guess(i)
            if m == 0:
                return i
            elif m == -1:
                r = i-1
            else:
                l = i+1



        return -1
