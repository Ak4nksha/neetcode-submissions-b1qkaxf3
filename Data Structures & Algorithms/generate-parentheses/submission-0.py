class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ''' add "(" if openN > 0
            add ")" if closeN < openN
            return IFF len = 2n
        ''' 

        res = []
        stack = []

        def dfs(openN, closeN):

            if (openN == 0 and closeN == 0 ):
                res.append("".join(stack))
                return

            
            if openN > 0:
                stack.append("(")
                dfs(openN - 1, closeN)
                stack.pop()

            if closeN > openN:
                stack.append(")")
                dfs(openN, closeN - 1)
                stack.pop()

        dfs(n,n)
        return res
       









