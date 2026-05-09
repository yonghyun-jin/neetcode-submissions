class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack 
        # start > end
        # 
        res = [0] * len(temperatures)
        stack = [] # pair : [temp, index]
        # [[38, 1], [36, 3], [35, 4]]

        for i, t in enumerate(temperatures):
            # there is stack / until warmer temperature found
            while stack and t > stack[-1][0]:
                print(stack)
                print(stack[-1][0])
                stackT, stackInd = stack.pop()
                # insert the # of days at stackInd Position. 
                # 
                res[stackInd] = (i - stackInd)
            stack.append([t,i])
        return res
