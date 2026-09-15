class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Understand: We must verify if the tree is Valid. A valid Tree is a Tree with all nodes connecting and no cycles


        #Input: Array with all edge pairs
        #Output: Return True or False based on if the Tree is Valid

        #Match: DFS --> Check in one direction and check for a cycle

        #Plan:Have an adjacency list where for each node store all its neighbors
        #Have a visited set to determine if there is a cycle and if we meet every node
        #Call DFS at the first node 0
        #need to track previous to avoid false negatives
        #DFS: if the node has already been visited return False.
        #Otherwise make DFS call for all neighbors except the prev
        #Add node to path and return True

        nodes = {i:[] for i in range(n)}

        for node, nei in edges:
            nodes[node].append(nei)
            nodes[nei].append(node)

        visited = set()
        def DFS(node, prev):
            if node in visited:
                return False


            visited.add(node)

            for neighbor in nodes[node]:
                if neighbor == prev:
                    continue
                if not DFS(neighbor, node):
                    return False
            
            return True

        
        return DFS(0, -1) and len(visited) == n

        