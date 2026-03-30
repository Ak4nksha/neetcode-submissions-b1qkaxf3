class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        

        n = len(nums)
        total = sum(nums)
        
        if total%k != 0: return False

        partSum = total // k
        nums.sort(reverse=True)
        if nums[0] > partSum: return False

        parts = [0] * k

        def back(i):
            if i == n:
                return True

            for j in range(k):

                # If two buckets currently have the same sum,
                # putting nums[i] into bucket 0 or bucket 1 leads to the same state shape
                if j > 0 and parts[j] == parts[j - 1]:
                    continue

                if parts[j] + nums[i] <= partSum:

                    parts[j] += nums[i]
                    if back(i+1):
                        return True

                    parts[j] -= nums[i]

                    #If nums[i] does not work in one empty bucket,
                    #  it will not work in another empty bucket either.
                    if parts[j] == 0: break 
            return False
        
        return back(0)




