
from collections import deque 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #Understand: We are given a 2D grid and we want to determine for each land 

        #match: DFS

        #Edgacase: no chest in the grid
        #Edgcase: no traversable land


        #Plan: #Utilizing for loops
        # we want to get to a traversable as long its not 0 or -1
        # we are going to call the DFS which help us determine nearest 0

        #Base case: if we run into a - 1 then we would stop the recursion in total
        #Case: if we run into a treasure chest we would return the distance to it.


        rows, cols = len(grid), len(grid[0])

        def add(r, c):
            if r < 0 or r > rows - 1 or c < 0 or c > cols - 1 or (r, c) in visited or grid[r][c] == - 1:
                return
            queue.append([r, c])
            visited.add((r, c))

        visited = set()

        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append([i, j])
                    visited.add((i, j))

        distance = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = distance
                add(r - 1, c)
                add(r + 1, c)
                add(r, c - 1)
                add(r, c + 1)
            
            distance += 1

        
                
        





        

        