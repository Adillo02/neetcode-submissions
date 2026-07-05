class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        key = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if stack:
                    top_val = stack[-1]
                    if key[top_val] != char:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        if stack:
            return False
        return True 
