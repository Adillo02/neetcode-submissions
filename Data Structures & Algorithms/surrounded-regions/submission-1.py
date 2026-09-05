from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:

        #Understand: We want to replace groups of Os that do have a single cell connected to a border
        #Input: 2D Array
        #Output: 

        #Match: BFS starting from Os touching the border

        #Plan:
        #Traverse through until we run into an O that is on the border of the grid
        #call the BFS algorithm where we pop and check for adjacent Os and mark them as visited
        #After go through the grid again to see if there Os that have not been visited and change them to Xs


        queue = deque()
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def BFS(r, c):
            queue.append((r,c))
            visited.add((r,c))

            while queue:
                r,c = queue.popleft()

                for cr, cc in [(1,0), (0,1), (-1, 0), (0, -1)]:
                    nr, nc = r + cr, c + cc

                    if (nr, nc) not in visited and nr >= 0 and nr < rows and nc >= 0 and nc < cols and board[nr][nc] == "O":
                        visited.add((nr, nc))
                        queue.append((nr, nc))



        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in visited and (r == 0 or r == rows - 1 or c ==0 or c == cols -1):
                    BFS(r,c)


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i,j) not in visited:
                    board[i][j] = "X"
                
        