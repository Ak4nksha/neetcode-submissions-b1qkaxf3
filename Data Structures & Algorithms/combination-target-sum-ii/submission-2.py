class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        n = len(candidates)
        res = []

        def back(i, curr, tar):
            
            if tar == 0:
                res.append(curr.copy())
                return
            elif i >= n or tar < 0 :
                return

            ''' Pick path: dfs(i+1, ...) is already unique by index usage. Even if there are duplicates, picking candidates[i] 
            and picking candidates[i+1] are different indices, and both may be needed to form valid combos that use multiple copies. 
            You should not skip duplicates before exploring pick, or you’ll accidentally remove possibilities like using the 2nd copy after using the 1st copy.
                
            Not-pick path: This is where duplicates create identical states. If you don’t pick the first 2,
            and then you also “don’t pick” the second 2, and then also “don’t pick” the third 2… 
            those are all the same decision: “I’m not using value 2 at all”. So you skip the whole block and do just one recursion for not-pick. '''

            

            ele = candidates[i]
            curr.append(ele)
            tar -= ele
            back(i+1,curr,tar)
            curr.pop()
            tar += ele
            while i+1 < n and candidates[i+1] == candidates[i]:
                i += 1
                continue
            back(i+1,curr,tar)

        back(0, [], target)
        return res

        






        