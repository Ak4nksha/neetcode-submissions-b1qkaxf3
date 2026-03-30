class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        memo = {}
        memo[0] = nums[0]
       

        def dp(i):

            if i == 0:
                return memo[0]
            if i<0: return 0

            if i in memo:
                return memo[i]

            pick = nums[i] + dp(i-2)
            notpick = dp(i-1)

            memo[i] = max(pick,notpick)
            return memo[i]

        s = dp(n-1)
        return s

            

            

