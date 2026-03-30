class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        n = len(digits)

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }


        def dfs(idx, curr):

            if len(curr) == n:
                res.append("".join(curr))
                return
          
            for ch in digitToChar[digits[idx]]:

                curr.append(ch)
                dfs(idx+1, curr)
                curr.pop()


        if digits:
            dfs(0, [])

        return res


                


                