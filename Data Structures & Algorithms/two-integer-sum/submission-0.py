class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        d = {}

        for i in range(n):

            complement = target - nums[i]

            if complement in d:
                return sorted([i,d[complement]])
            else:
                d[nums[i]] = i


        return []


