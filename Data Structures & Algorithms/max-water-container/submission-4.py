class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        max_area = 0

        while L < R:
            height = min(heights[L], heights[R])

            max_area = max(max_area, height * (R - L))
           
            if heights[R] > heights[L]:
                L += 1
            else:
                R -= 1 
        return max_area

            
        


             


        