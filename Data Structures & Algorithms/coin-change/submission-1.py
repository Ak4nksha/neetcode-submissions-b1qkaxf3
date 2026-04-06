class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        ans = float('inf')
        dp = [[0] * (amount+1) for _ in range(n)]

        for t in range(amount+1):

            if t%coins[0] == 0:
                dp[0][t] = t//coins[0]
            else:
                dp[0][t] = float('inf')

        for i in range(1, n):
            for target in range(amount+1):

                notTake = 0 + dp[i-1][target]
                take = float('inf')
                if coins[i] <= target:
                    take = 1 + dp[i][target - coins[i]]
                #print(take, notTake)
                dp[i][target] =  min(take, notTake)

        ans = dp[n-1][amount]
        if ans >= float('inf'):
            return -1
        else:
            return ans