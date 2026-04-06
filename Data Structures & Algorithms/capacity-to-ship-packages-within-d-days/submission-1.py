class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        ans = float('inf')

        def canDo(cap):
            
            day = 1
            curr = cap

            for w in weights:

                if curr - w < 0:
                    day += 1

                    if day > days:
                        return False

                    curr = cap #reset

                curr -= w

            return True
        
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