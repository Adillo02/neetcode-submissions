class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #Understand: we want to determine the cells that flow into the pacific and Atlantic

        #Match: DFS 

        #Plan: have a Pacific Set to store coordinates that flow into the pacific and an Atlantic set to store coordinates that flow in to the Atlantic
        # Utilize the four corners -- > Start at the column of the pacifc side and Atlantic side and move in to determine what flows in by using a DFS call
        #Do the same for columns

        # Lastly do a check thriugh grid to see what coordinates is in both sets

        rows, cols = len(heights), len(heights[0])
        ans = []
        visited = set()
        pacific, atlantic = set(), set()

        def dfs(r, c, ocean, prev):
            if (r,c) in ocean or r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] < prev:
                return

            
            ocean.add((r,c))
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])


        
        for i in range(rows):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, cols - 1, atlantic, heights[i][cols - 1])
        

        for i in range(cols):
            dfs(0, i, pacific, heights[0][i])
            dfs(rows - 1, i, atlantic, heights[rows - 1][i])


        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    ans.append([r,c])

        return ans 
