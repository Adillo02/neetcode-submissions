class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #Understand: We want to count the number of connected sections in the graph
        #input: Array with pairs representing the undirected connections
        #outputL Return the number of connected sections 

        #Match: DFS 


        #Plan: We use a hasmap to create an adjacency list
        #We loop through 0 to n - 1 nodes and for the first node we call DFS
        #If node not in visited then increment count
        #Else mark all connected nodes as visited
        #If the node is visited skip it


        nodes = {i: [] for i in range(n)}
        count = 0

        for node, connect in edges:
            nodes[node].append(connect)
            nodes[connect].append(node)

        visited = set()
        def DFS(node):
            if node in visited:
                return

            visited.add(node)

            for connect in nodes[node]:
                DFS(connect)

            
            return

        for i in range(n):
            if i not in visited:
                DFS(i)
                count += 1
            else:
                continue

        return count

        