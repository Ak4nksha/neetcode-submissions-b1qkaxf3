class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        n = len(nums)
        minq = deque() # monotonically increasing
        maxq = deque() # monotonically decreasing
        res = 0

        l = 0

        for r in range(n):

            while minq and minq[-1] > nums[r]:
                minq.pop()

            while maxq and maxq[-1] < nums[r]:
                maxq.pop()

            minq.append(nums[r])
            maxq.append(nums[r])

            while maxq[0] - minq[0] > limit and l <= r:

                if minq[0] == nums[l]:
                    minq.popleft()

                if maxq[0] == nums[l]:
                    maxq.popleft()
                l += 1
            res = max(res, r-l+1)

        return res





            



        

