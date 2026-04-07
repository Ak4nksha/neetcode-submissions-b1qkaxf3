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
        
        def f(idx, s): # how many subsets can form sum s till index idx

            #base cases
            if idx == 0:

                if s == 0 and nums[idx] == 0:
                    return 2
                if s == 0 or s == nums[idx]:
                    return 1
                return 0

            if dp[idx][s] != -1:
                return dp[idx][s]
            
            notTake = f(idx-1, s)
            take = 0
            if nums[idx] <= s:
                take = f(idx-1, s-nums[idx])

            dp[idx][s] = take + notTake
            return dp[idx][s]

        total = sum(nums)
        # k = (target + total )
        # if k % 2: return 0

        if abs(target) > total: # Because the biggest positive sum you can ever make is: [-total, total]
            return 0

        k = target + total
        if k < 0 or k % 2 != 0:
            return 0
        
        s1 =  k // 2 
        dp = [[-1] * (s1+1) for _ in range(n)]

        if s1 == 0 and nums[0] == 0: 
            dp[0][0] = 2
        else:
            dp[0][0] = 1

        if nums[0] != 0 and nums[0] <= s1:
            dp[0][nums[0]] = 1

        return f(n-1, s1)







