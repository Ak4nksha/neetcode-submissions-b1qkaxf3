class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
         #s1 -> all positive
        #s2 -> all positive 
        #s1 - s2 = target
        #s2 = total - s1
        #s1 - (total - s1) = target
        #2 * s1 = target + total
        #s1 = (target + total) //2  -> (target + total) >= 0 and even number because s1 can't be fraction

        n = len(nums)
        total = sum(nums)
        if abs(target) > total: # Because the biggest positive sum you can ever make is: [-total, total]
            return 0
        k = target + total
        if k < 0 or k % 2 != 0:
            return 0
        
        s1 =  k // 2 
        dp = [[0]*(s1+1) for _ in range(n)]

        if nums[0] == 0: 
            dp[0][0] = 2
        else:
            dp[0][0] = 1

        if nums[0] != 0 and nums[0] <= s1:
            dp[0][nums[0]] = 1

        # print(dp)
        for idx in range(1,n):
            for s in range(0,(s1+1)):
            
                notTake = dp[idx-1][s]
                take = 0
                if nums[idx] <= s:
                    take = dp[idx-1][s-nums[idx]]

                dp[idx][s] = take + notTake
                # print(dp)
    
        return dp[n-1][s1]







