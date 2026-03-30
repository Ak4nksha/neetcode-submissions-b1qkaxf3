class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        n = len(nums)
        minSm = nums[0]
        maxSm = nums[0]
        total = sum(nums)
        minAns = minSm
        maxAns = maxSm

        for i in range(1,n):

            k = minSm + nums[i]

            if nums[i] < k:
                minSm = nums[i]
            else:
                minSm = k

            minAns = min(minAns, minSm)

            l = maxSm + nums[i]

            if nums[i] > l:
                maxSm = nums[i]
            else:
                maxSm = l

            maxAns = max(maxSm, maxAns)

        #print(minAns, total)
        
        if maxAns > 0:
            return max( maxAns, total-minAns)
        else:
            return maxAns


       

