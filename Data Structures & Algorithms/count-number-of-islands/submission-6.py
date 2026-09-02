from collections import deque 
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Understand: We want to count the number of groups of ones on the grid

        #Match: Graph BFS

        #Plan: Edge Cases: If the grid is empty return 0
        #Edges count as water
        #Transverse each position in the Grid
        #If the position is a 1 and it has not been visited then we should run the BFS to mark all connecting 1s to that land position
        #Use a set to track visited cells
        #When done you want to mark the cell as visited when done with that position
        
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0 

        def BFS(i, j):
            queue = deque()
            queue.append((i,j))

            while queue: 
                r,c = queue.popleft()

                for cr, cc in [(1,0), (0, 1), (-1,0), (0, -1)]:
                    nr,  nc = cr + r, cc + c 
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and (nr,nc) not in visited and grid[nr][nc] == "1":
                        visited.add((nr,nc))
                        queue.append((nr,nc))

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    BFS(i,j)
                    visited.add((i, j))
                    count += 1

        
        return count 

        
        