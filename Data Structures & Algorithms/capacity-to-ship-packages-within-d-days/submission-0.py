class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        n = len(weights)
        ans = float('inf')

        def canDo(cap):
            
            cnt = 0 # number of days

            i = 0
            while i < n:

                weight = 0
                while i< n and weight + weights[i] <= cap:
                    weight += weights[i]
                    i += 1

                cnt += 1
                # print(f" cnt = {cnt}, weight = {weight}")

                if cnt > days:
                    return False

            return cnt <= days
        
        # canDo(8)
        low = max(weights)
        high = sum(weights)

        while low <= high:

            mid = (low+high)//2

            if canDo(mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1

        return ans




            
