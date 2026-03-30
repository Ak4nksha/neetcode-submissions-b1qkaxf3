class Solution:
    def rob(self, nums: List[int]) -> int:
        m = len(nums)
        if m< 3:
            # print("yes")
            return max(nums)

        def findMax(p,q):

            arr = nums[p:q+1]
            
            n = len(arr)
            if n < 3:
                # print("yes")
                return max(arr)
            prev2 = arr[0]
            prev = max(arr[0], arr[1])
            # print(arr,  prev2, prev )   
            
            for i in range(2, n):

                
                curr = max(arr[i] + prev2, prev)

                prev2 = prev
                prev = curr
                # print(arr[i])
                # print(prev2, prev)

            return prev

    
        return max(findMax(0, m-2), findMax(1,m-1))
