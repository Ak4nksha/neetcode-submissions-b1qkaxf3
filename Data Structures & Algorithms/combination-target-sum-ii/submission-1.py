class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        res = set()
        
        def back(i, arr, tar):
            if tar == 0:

                ''' #because Python is pass by object reference.
                    What that means:
                    Variables don’t store values. They store references to objects.
                    When you pass arr into the function or append it to res, 
                    you are passing the reference to the same list object. '''

                res.add(tuple(sorted(arr))) 
                return
            elif i == n:
                return
            
            ele = candidates[i]

            arr.append(ele)
            tar -= ele
            back(i+1,arr, tar)
           # print("Res =", res)

            arr.pop()
            tar += ele
            back(i+1, arr, tar)
           # print("Res =", res)

        back(0,[],target)
        return [list(x) for x in res]