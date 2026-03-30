class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.append(0)
        n = len(cost)
        arr = [-1]* n
        arr[0] = cost[0]

        def f(i):

            if i < 0:
                return 0

            if arr[i] != -1:
                return arr[i]

            arr[i] = cost[i] + min(f(i-1),f(i-2))
            print(arr[i])
            return arr[i]


        arr[n-1] = f(n-1)
        return arr[-1]
