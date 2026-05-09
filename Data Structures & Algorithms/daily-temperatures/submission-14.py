class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
  
        res = [0] * len(temperatures) 
        stack = [] # calculate days took using index [temp, index]
        

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                # until stack is not empty
                # stack[-1]  top of the stack 
                stackT, stackInd = stack.pop()
                res[stackInd] = index - stackInd
            stack.append((temp,index))
            print(stack)

        return res
