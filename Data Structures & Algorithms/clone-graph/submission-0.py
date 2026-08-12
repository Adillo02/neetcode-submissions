"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Understand: is that we want to create a deep copy of the graph, which means creating new nodes that have the same neighbors

        #Match: DFS

        #Edgecase: if the matrix is empty return [] or only oen element inside is [[]]

        #Plan: Use a hashmap to store the current nodes paired with the cloned nodes
        #Then go to the neighbors node 

        if not node:
            return None
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            
            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        
        return dfs(node)


