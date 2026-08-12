class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Understand:We must determine the number of islands in the 2d array
        #An island is formed if it connects with land horizontally or vertically and is surroded by water which is 0s or on the edge
        #Match: DFS because we must check for every node to determine if we have seen it

        #Plan:
        #Iterate through the whole 2d array and do a recursive call for each spot and have a set to determine if we have alreadty visted a spot. If it has been visited continue we would updgrade the count by 1 if we run into a 0 


        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        

        visited = set()

        def dfs(r, c):
            if r > rows -1 or r < 0 or c < 0 or  c > cols -1  or (grid[r][c] == "1" and (r, c) in visited) or grid[r][c] == "0" :
                return

            visited.add((r,c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)


        visited = set()

        islands = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    islands += 1 

        return islands




        
        