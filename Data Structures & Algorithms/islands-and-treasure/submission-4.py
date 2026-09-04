from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #Understand: for each tarversable land cell we want to get the distance to the nearest treasure chest
        #Input: 2D grid
        #Output; The same grid but the cells now have the distance to the nearest Treasure chest

        #Match: BFS starting from the Treasure chests

        #Plan: We want to traverse the 2D grid and if we run into a 0
        #Then we want to call BFS and start getting the distances for the adjacent cells
        #In the BFS we are going to use a queue to store the adjacent lands
        #Increment a count everytime we get further from the chest and see if the distance is less than what's already inside
        
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        visited = set()

        def add(r, c):
            if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] > 0 and (r,c) not in visited:
                queue.append((r,c))
                visited.add((r,c))




        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j] == 0:
                    queue.append((i,j))

        distance = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                grid[r][c] = distance

                add(r-1, c)
                add(r + 1, c)
                add(r, c + 1)
                add(r, c - 1)
            
            distance += 1
       

        
        
        