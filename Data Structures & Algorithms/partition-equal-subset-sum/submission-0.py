class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        

        n = len(nums)
        total = sum(nums)
        #target = totalSum // 2
        if total%2:
            return False # can't divide into two partition
        target = total//2

        # i -> 0 to n-1 , target -> 0 to target ( max value of target = 200*100 check constraints)
        dp = [[-1] * (target+1) for _ in range(n)]

        # for i in range(n):
        #     dp[i][0] = True #i.e. if target == 0, return True

        # dp[0][nums[0]]

        def isSubsetEqualTarget(i, target):
            
            if target == 0: return True

            if i == 0:
                return nums[i] == target # if target is not zero and this is the last element to check, 
                                        # return true onlyy if this last element = target

            if dp[i][target] != -1: return dp[i][target]

            notTake = isSubsetEqualTarget(i-1, target)
            # I can only pick an element if it's less than or equal to target
            take = isSubsetEqualTarget(i-1, target - nums[i])

            dp[i][target] = take or notTake
            return dp[i][target]


        

        return isSubsetEqualTarget(n-1, target)