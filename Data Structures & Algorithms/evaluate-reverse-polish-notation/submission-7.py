class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for item in tokens:
            if item =="*":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second * first))
            elif item == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second / first))
            elif item == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second + first))

            elif item =="-":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second - first))
            else:
                stack.append(int(item))
        
        return stack[0]




