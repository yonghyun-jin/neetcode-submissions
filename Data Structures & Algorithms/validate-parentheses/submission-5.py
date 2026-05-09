class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        # append when you find { [  (
        dic = { "{" : "}", "(":")", "[":"]"}
       
        
        for item in s :
            if item in dic:
                stack.append(dic[item])
                # )]}
            else :
                if len(stack) >0:
                    if item == stack.pop():
                        continue
                    else:
                        return False
                else:
                    return False
        if len(stack) > 0:
            return False
                
        return True
                



        # pop when you find } ] )