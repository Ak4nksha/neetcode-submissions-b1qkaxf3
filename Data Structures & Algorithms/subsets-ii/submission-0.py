class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        n = len(nums)

        def back(idx, curr):

            res.append(curr.copy())

            for j in range(idx, n):

                if j>idx and nums[j] == nums[j-1]:
                    continue

                curr.append(nums[j])
                back(j+1, curr)
                curr.pop()

        back(0,[])
        return res


            