class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        # memo = [0] * (n+1)
        prev2 = 0 #0th index
        prev = 0 #1th index

        for i in range(2, n+1):

            one = prev + cost[i-1]  #30
            two = prev2 + cost[i-2] #15
            curr = min(one,two) #15

            prev2 = prev #10
            prev = curr  #15
            
        return prev
       
        
        



        