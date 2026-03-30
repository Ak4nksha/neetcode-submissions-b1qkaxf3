class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        d = {0:1}
        sm = 0
        cnt = 0

        for x in nums:

            sm += x
            diff = sm - k

            cnt += d.get(diff,0)
            d[sm] = 1 + d.get(sm,0)

        return cnt