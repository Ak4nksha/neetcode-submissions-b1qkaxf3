class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        sum1 = nums[0]
        ans = sum1

        for i in range(1, n):

            k = sum1 + nums[i]

            if nums[i] > k:
                sum1 = nums[i]
            else:
                sum1 = k
            
            ans = max(ans,sum1)

        return ans



