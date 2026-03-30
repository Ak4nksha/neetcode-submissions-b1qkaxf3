class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)
        if n == 1 or k == 0: return False

        d = {}

        for i in range(n):
            if nums[i] in d:
                return True
            else:
                if len(d) == k:
                    idx = i - k
                    del d[nums[idx]]
                d[nums[i]] = i

        return False
