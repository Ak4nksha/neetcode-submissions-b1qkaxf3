class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n < 3:
            return max(nums)
        memo = {}
        memo[0] = nums[0]


        for i in range(1, n):
            pick = nums[i]
            if i > 1: pick += memo[i-2]
            notpick = memo[i-1]

            memo[i] = max(pick,notpick)

        return memo[n-1]

            

            

