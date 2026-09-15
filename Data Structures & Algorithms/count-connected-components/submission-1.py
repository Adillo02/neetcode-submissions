class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #Understand: We want to get the count of connected sections in the Graph
        #Input: Array of pairs for the edges
        #Output: count of how many sections there are

        #DFS --> We want to mark all nodes

        #Plan: Use an adjacency list for each node and all its neighbors and Create DFS
        #Have a count to track sections
        #Call dfs for each node if it has not been visited then we know that is a section and increment count
        #If node in visited return nothing
        #Otherwise go to every neighbor and mark them as visited

        nodes = {i:[] for i in range(n)}

        for node, nei in edges:
            nodes[node].append(nei)
            nodes[nei].append(node)

        visited = set()

        count = 0
        
        def DFS(node):
            if node in visited:
                return

            visited.add(node)

            for neighbor in nodes[node]:
                DFS(neighbor)

            return

        
        for i in range(n):
            if i not in visited:
                DFS(i)
                count += 1
        return count

            
