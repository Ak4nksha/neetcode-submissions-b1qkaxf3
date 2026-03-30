class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums: return 0
        arr = set(nums)
        ans = 0

        for num in arr:
            if num-1 not in arr:

                curr = num
                temp = 1

                while curr+1 in arr:
                    temp += 1
                    curr += 1
                ans = max(ans,temp)

        return ans
