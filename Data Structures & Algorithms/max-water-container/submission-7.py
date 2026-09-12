class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Understand: We want to find the biggest area between two Bars
        #Width is the difference between the bars
        #Height: the minimum bteween the two bars

        #Match: Two pointer

        #Plan:Start out from the beginning and R on the last:
        #Calculate Area and move the pointer depending on which bar is smaller
        #Return the max_area 


        max_area = 0

        L, R = 0, len(heights) - 1

        while L < R:
            width = R - L
            height = min(heights[L], heights[R])

            area = width * height
            max_area = max(area, max_area)

            if heights[L] >= heights[R]:
                R -= 1
            else:
                L += 1
        
        return max_area

        


             


        