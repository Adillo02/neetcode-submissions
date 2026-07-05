class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for index, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackind = stack.pop()
                res[stackind] = index - stackind
            stack.append([t, index])
        return res