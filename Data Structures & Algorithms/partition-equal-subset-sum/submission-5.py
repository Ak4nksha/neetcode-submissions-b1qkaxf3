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
        # print(target)
        # # i -> 0 to n-1 , target -> 0 to target ( max value of target = 200*100 check constraints)
        # dp = [[False] * (target+1) for _ in range(n)]

        # Previous row stores:
        # Using elements from index 0 to i-1, which target sums from 0 to target are possible?
        prev = [False] * (target+1)

        # for i in range(n):
        #     dp[i][0] = True #i.e. if target == 0, return True 
        #     # Because sum 0 can always be made by taking nothing.

        prev[0] = True 
        
        
        # if nums[0] <= target:
        #     dp[0][nums[0]] = True #i.e. if nums[0] == target. Using only nums[0], what sums can I make?
        #     # Because row 0 means using only the first element nums[0].

        if nums[0] <= target:
            prev[nums[0]] = True

        # print(dp)
        
        for i in range(1, n):

            curr = [False] * (target+1)
            
            for k in range(1, (target+1)):

                notTake = prev[k]
                take = False
                if nums[i] <= k:
                    take = prev[k - nums[i]]
                curr[k] = take or notTake

            prev = curr

        # for i in range(n):
        #     print(f"{dp[i]} ")
        return prev[target]

