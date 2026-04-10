class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        ans = []

        q = deque()
        l = 0
        r = 0
        while l<=r and r < n:

            while r-l+1 <= k:

                while q and q[-1] < nums[r]:
                    q.pop()
                
                q.append(nums[r])
                r += 1

            ans.append(q[0])
            if nums[l] == q[0]:
                q.popleft()

            l += 1

        return ans
               






