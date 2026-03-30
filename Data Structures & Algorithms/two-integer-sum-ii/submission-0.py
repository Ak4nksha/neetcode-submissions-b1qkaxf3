class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)
        a = 0
        b = n-1

        while a<b:

            k = nums[a] + nums[b]

            if k == target:
                return [a+1,b+1]
            elif k < target:
                a += 1
            else:
                b -= 1

        return [-1,-1]