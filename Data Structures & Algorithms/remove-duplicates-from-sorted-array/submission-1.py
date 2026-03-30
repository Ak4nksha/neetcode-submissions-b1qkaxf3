class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        n = len(nums)
        i = 0

        while i+1 < n:

            if nums[i+1] != nums[i]:
                i += 1
            else:
                break

        j = i+1

        while j<n:

            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
            
            j += 1

        return i+1