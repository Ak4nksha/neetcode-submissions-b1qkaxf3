class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        

        n = len(nums)
        total = sum(nums)
        
        if total%k != 0: return False

        partSum = total // k
        if max(nums) > partSum: return False

        parts = [0] * k

        def back(i):
            if i == n:
                return True

            for j in range(k):

                if parts[j] + nums[i] <= partSum:

                    parts[j] += nums[i]
                    if back(i+1):
                        return True

                    parts[j] -= nums[i]
                    if parts[j] == 0: break
            return False
        
        return back(0)




