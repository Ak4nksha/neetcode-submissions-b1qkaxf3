class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        max_idx = 0  # maximum idx I can reach so far

        for i in range(n):

            if i > max_idx:
                return False
            if max_idx >= n-1:
                return True
            max_idx = max(max_idx, i+nums[i])

        return True