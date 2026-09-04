from collections import deque 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        #understand we want to determine the minimum amount of time for every fresh fruit in the grid to become rotten
        #Input: 2D grid
        #Output: an integer representing how much time it takes for all fresh fruit to become rotten

        #Match: Multi source BFS

        #Edge case if a fruit isolated and still fresh then we would return -1

        #Plan: Get alll the rotten fruits in the queue make sure they already haven't been visited 
        #initilize the minute = 0
        #We want to pop  and check the adjacent cells if they are fresh because they now become rotten in that current minute

        #After we want to check again in the grid if there are fresh fruit remaining. If so then we know that we can just return -1

        queue = deque()
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def gotRotten(r, c):
            if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] == 1 and (r, c) not in visited:
                queue.append((r,c))
                visited.add((r, c))
                grid[r][c] = 2

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2 and (i, j) not in visited:
                    queue.append((i,j))
                    visited.add((i,j))

        
        minute = 0

        while queue:
            
            for i in range(len(queue)):
                r, c = queue.popleft()
                gotRotten(r + 1, c)
                gotRotten(r - 1, c)
                gotRotten(r, c + 1)
                gotRotten(r, c - 1)
            if queue:
                minute += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return - 1


        
        return minute 
        