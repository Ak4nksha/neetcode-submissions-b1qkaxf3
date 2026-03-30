class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        ans  = 0
        n = len(prices)

        for i in range(1,n):

            if prices[i] <= buy:
                buy = prices[i]
            else:
                ans = max(ans, prices[i]-buy)

        return ans