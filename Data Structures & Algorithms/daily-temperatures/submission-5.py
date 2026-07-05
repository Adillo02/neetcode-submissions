class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            stack = []
            res = [0] * len(temperatures)

            for i , value in enumerate(temperatures):
                while stack and stack[-1][1] < value:
                    removed = stack.pop()
                    res[removed[0]] = i - removed[0]
                
                stack.append((i, value))
            
            return res
