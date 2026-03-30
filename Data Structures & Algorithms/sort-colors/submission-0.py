class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)

        i = 0
        j = n-1
        k = 0

        while i<j and k<=j:

            if nums[k] == 0:
                nums[k], nums[i] = nums[i],nums[k]
                k += 1
                i += 1
            elif nums[k] == 2:
                nums[j],nums[k] = nums[k], nums[j]
                j -= 1

            else:
                k += 1

        return nums