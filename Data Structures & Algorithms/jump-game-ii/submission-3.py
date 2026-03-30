class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jump = 0
        l=r= 0
        n = len(nums)

        while r < n-1:
            far = 0

            for i in range(l, r+1):
                far = max(far, i + nums[i])

            l = r+1
            r = far
            jump += 1
        
        return jump