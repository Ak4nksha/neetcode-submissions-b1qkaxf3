class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        #nums.sort()
        n = len(nums)
        res = []

        def dfs(curr, unique):
            # print(curr)
            # print(unique)
            if len(curr) == n:
                res.append(curr.copy())
                #print((res))
                return
            
            for k,v in unique.items():

                if v > 0:

                    curr.append(k)
                    unique[k] -= 1
                    dfs(curr,unique)
                    curr.pop()
                    unique[k] += 1

        u = {}
        for num in nums:
            if num not in u:
                u[num] = 1
            else:
                u[num] += 1

        dfs([],u )
        return res

        


            