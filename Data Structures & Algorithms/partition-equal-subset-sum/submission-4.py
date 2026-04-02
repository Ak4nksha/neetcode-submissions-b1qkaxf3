class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ''' Just python things

        print(0 or False)     # False
        print(0 or 5)         # 5
        print(-1 or 100)      # -1
        print("" or "hello")  # hello
        print(-1 or False)    # -1

        '''

        n = len(nums)
        total = sum(nums)
        #target = totalSum // 2
        if total%2:
            return False # can't divide into two partition
        target = total//2
        print(target)
        # i -> 0 to n-1 , target -> 0 to target ( max value of target = 200*100 check constraints)
        dp = [[False] * (target+1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True #i.e. if target == 0, return True 
            # Because sum 0 can always be made by taking nothing.
        
        
        if nums[0] <= target:
            dp[0][nums[0]] = True #i.e. if nums[0] == target. Using only nums[0], what sums can I make?
            # Because row 0 means using only the first element nums[0].

        # print(dp)
        
        for i in range(1, n):
            for k in range(1, (target+1)):

                notTake = dp[i-1][k]
                take = False
                if nums[i] <= k:
                    take = dp[i-1][k - nums[i]]
                dp[i][k] = take or notTake

        # for i in range(n):
        #     print(f"{dp[i]} ")
        return dp[n-1][target]

