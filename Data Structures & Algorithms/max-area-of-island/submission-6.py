from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #Understand: Is that we want to find the biggest group of 1s
        #Input: grid with 1s and 0s
        #Output: area of the biggest group

        #Match: BFS utilizing a queue 

        #Edegecases: if the grid is empty or if we are at an edege

        #plan: We want to transverse the Grid and if we reach 1 that has not been viisted then we want to call the BFS function
        #Inside the BFS function we want to sore the coordinates of the cell in a queue 
        #While queue --> Pop from the left, for every direction check if it is a 1 that has not been visited if so
        #then we want to increment our count and add that position to the set
        #when done with the BFS algorithm we sget the max_size



        rows = len(grid)
        cols = len(grid[0])
        max_size = 0
        visited = set()

        def BFS(i, j):
            queue = deque()
            queue.append((i,j))
            visited.add((i,j))
            size = 1

            while queue: 
                r,c = queue.popleft()

                for cr, cc in [(1,0), (0, 1), (-1,0), (0, -1)]:
                    nr, nc = cr + r, cc + c

                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        size += 1
                        queue.append((nr,nc))
                        visited.add((nr,nc))
            return size 




        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    count = BFS(i,j)
                    
                    max_size = max(max_size, count)

        
        return max_size

        

        