class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res = []
        nums.sort()
        visit = [0] * n
        

        def back(curr):

            if len(curr) == n:
                res.append(curr.copy())

            
            for i in range(n):

                if visit[i]:
                    continue

                if i and nums[i] == nums[i-1] and not visit[i-1]:
                    continue

                curr.append(nums[i])
                visit[i] = 1
                back(curr)
                visit[i] = 0
                curr.pop()


        back([])
        return res


            