class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        l = 0
        r = n-1

        while l<=r:

            m = l+(r-l)//2

            if nums[m] == target:
                return m

            if nums[m] > target:

                if m-1 != -1:
                    if nums[m-1] < target:
                        return m
                    else:
                        r = m-1
                else:
                    return 0

            elif nums[m] < target:

                if m+1 != n:
                    if nums[m+1] > target:
                        return m+1
                    else:
                        l = m+1
                else:
                    return n

        return -1

