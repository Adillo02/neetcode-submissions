class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #Understand: We want to return the island with the most Area on the grid

        #Match: DFS or BFS

        #Edge case: if the grid is empty we would return 0

        #Plan: Having a set to determine if we have visted a cell while looping throiugh each cell
        #If we run into a cell hasn't been visited and is a 1 then we run the DFS
        #Base DFS: if we are out of range or run into a 0 or a value we have visted already we would return 0 
        #Other wise we would return 1 + all directions because we know that the cell we are at is a land


        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        visited = set()

        ans = 0

        def dfs(r, c):
            if r < 0 or r > rows - 1 or c < 0 or c > cols - 1 or (r,c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))

            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r, c - 1)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    size = 0
                    size = dfs(i, j)
                    if size > ans:
                        ans = size

        return ans 


        