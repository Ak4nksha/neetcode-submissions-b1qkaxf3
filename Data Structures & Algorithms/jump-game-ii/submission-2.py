class Solution:
    def jump(self, nums: List[int]) -> int:
        
        memo = {}
        # jump = float('inf')
        n = len(nums)

        def dp(i):
            
            if i >= n-1:
                return 0

            if i in memo:
                return memo[i]


            if nums[i] == 0:
                return float('inf')


            end = min(n-1, i + nums[i])
            jump = float('inf')
            for j in range(i+1, end+1):
                jump = min(jump, 1+dp(j))
            memo[i] = jump
            return jump

        return dp(0)
