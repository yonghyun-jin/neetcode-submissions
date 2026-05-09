class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # ()()()
        # open
        # close
        # open > close
        # (()())
        # ()()()
        # ((()))
        # ()()()
        # (())()
        # map
        # first is ( 
        # ( 
        stack = []
        res = []

        def backtrack(openN, closedN):
            # this is when the loop ends
            # Only add open parenthesis if open < n
            # Only add a closing parenthesis if open > close 
            # valid when open == close == n 

            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n: 
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0,0)
        return res
            
            
             
            


        