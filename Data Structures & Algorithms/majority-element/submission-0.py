class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]

        ele = nums[0] #candidate
        cnt = 1 #count of candidate
        k = n/2

        #first pass - find candidate

        for i in range(n):

            if nums[i] == ele:
                cnt += 1
            else:

                cnt -= 1
                if cnt == 0:
                    ele = nums[i]
                    cnt = 1

        
        #second pass - count the number of candidate ele
        c = 0
        for i in range(n):
            if nums[i] == ele:
                c += 1

        if c > k:
            return ele

        
