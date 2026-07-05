class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1 
        curr_size = 0
        max_size = 0
        area = 0
         
      

        while L < R:
            if heights[L] < heights[R]:
                curr_size = heights[L]                
                area = R - L
                L += 1
            elif heights[L] > heights[R]:
                curr_size = heights[R]
                area = R - L
                R -= 1
            else:
                curr_size = heights[L]
                area = R - L
                L += 1

            curr_size  = area * curr_size 

            max_size = max(max_size, curr_size)

        return max_size

             


        