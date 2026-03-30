class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []

        def back(i,comb):
            
            if i > n:
                if len(comb) == k:
                    res.append(comb.copy())

                return


            comb.append(i)
            back(i+1,comb)
            comb.pop()
            back(i+1,comb)

        back(1, [])
        return res


        