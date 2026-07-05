class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        

        for char in tokens:
            if char not in ["-", "+", "/", "*"]:
                stack.append(int(char))
            else:
                first = stack.pop()
                second = stack.pop()
                if char == "+":
                    stack.append(second + first)
                   
                elif char == "-" :
                    stack.append(second - first)
                   
                elif char == "*":
                    stack.append(second * first)
                    
                elif char == "/":
                    stack.append(int(second / first))
        
        return stack[0]
            
        