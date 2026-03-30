class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)
        seen = [0] * n

        def back(curr):

            if len(curr) == n:
                res.append(curr.copy())
                return

            for i in range(n):

                if not seen[i]:
                    curr.append(nums[i])
                    seen[i] = 1
                    back(curr)
                    seen[i] = 0
                    curr.pop()

        back([])
        return res

            

            

        