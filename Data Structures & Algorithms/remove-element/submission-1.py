class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        n = len(nums)
        if n == 0 or ( n== 1 and nums[0] == val):
            return 0

        k = 0
        i = 0
        while i < n:
            if nums[i] == val:
                break
            else:
                i += 1
                continue
        
        if i == n: return n

        

        while i < n:
            j = i + 1

            while j < n:
                if nums[j] == val:
                    j += 1
                    continue
                else:
                    nums[i],nums[j] = nums[j],nums[i]
                    break
            
            if j == n:
                return i
            i += 1

        
        return k

