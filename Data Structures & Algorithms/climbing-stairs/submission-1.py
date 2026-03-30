class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1: return 1
        arr = [-1] * (n+1)
        for i in range(3):
            arr[i] = i
        #print(arr)
        def steps(n):
            #print(arr)
            if n<=2:
                return arr[n]

            if arr[n] == -1:
                arr[n] = steps(n-1) + steps(n-2)
            print(arr)
            return arr[n]

        return steps(n)

        

