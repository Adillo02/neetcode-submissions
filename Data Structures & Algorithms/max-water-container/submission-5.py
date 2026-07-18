class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1

        max_area = 0

        while L <= R:
            if heights[L] > heights[R]:
                max_area = max(max_area, heights[R] * (R - L))
                R -=1 
            else:
                max_area = max(max_area, heights[L] * (R - L))
                L +=1

        return max_area

        


             


        