"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Understand: We want to create a deep copy of the adjaecent list meaning new node and not pointing to the old nodes\
        #Input: Node
        #Output: copy of the graph (I believe we can return any node and that should return everything)
        #match: DFS  --> handling only the neighbors of the index we are at
        #Plan: Traverse through each node  by going through the neighbors list  and for each node store in haspmap with the old being the Key and the new being the value   Call the BFS when setting the neighbors
        #In the queue add the new copy of the copy of the neighbor if it deosn't already exist

        
        if not node:
            return None
        
        

        otn = {}
        
        def dfs(node):
            if node in otn:
                return otn[node]

            copy = Node(node.val)
            otn[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy

        return dfs(node)


        