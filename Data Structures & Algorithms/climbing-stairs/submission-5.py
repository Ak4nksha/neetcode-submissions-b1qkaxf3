class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = [-1] * (n+1)
        
        def steps(i):
            if i < 1: return 0
            if i <= 3: return i

            if cache[i] == -1:
                cache[i] = steps(i-1) + steps(i-2)

            return cache[i]
        
        return steps(n)
