class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low = 1
        high = max(piles)
        ans = high
        n = len(piles)
        if h == n:
            return high

        def canDo(k):
            cnt = 0
            for i in range(n):
                x = piles[i]
                # cnt += math.ceil(x/k) -> this can break if x is tooooo large
                cnt += (x + k - 1) // k
                if cnt > h:
                    return False
            return cnt <= h

        while low<=high:

            mid = (low+high)//2

            if canDo(mid):
                ans = min(ans,mid)
                high = mid-1 #try at a lower speed
            else:
                low = mid+1 # increase the speed

        return ans

















