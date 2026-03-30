class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n < 3:
            return max(nums)
        prev2 = nums[0]
        prev = max(nums[0],nums[1])


        for i in range(2, n):
            pick = nums[i] + prev2
            notpick = prev

            curr = max(pick,notpick)

            prev2 = prev
            prev = curr

        return prev

            

            

