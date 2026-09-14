class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Understand: we must determine if the Tree is valid, meaning no cycles, and every node can be reached
        #Input: Array with a pair representing a node and the node its connected to
        #Output: Return True or false based on if the Tree is Valid

        #Match: DFS --> Must Verify if there a cycle

        #Plan:
        #Have a hasmap with each node and the nodes it connects to in a araay it is directed so we must connect both ways
        #have a visit set to detect ccycles
        #Hav a DFS function where the Base case is: if we already visited that node, return False
        #Then add to visit and do recursive call with DFS 
        #Then one last check to see if the number of nodes visited == n

        
        if not edges:
            return True 
        nodes = {i:[] for i in range(n)}

        
        for node, connect in edges:
            nodes[node].append(connect)
            nodes[connect].append(node)

        path = set()

        def DFS(node, prev):
            if node in path:
                return False

            path.add(node)

            for connect in nodes[node]:
                if connect == prev:
                    continue
                if not DFS(connect, node):
                    return False
            

            return True 
        


        return DFS(0, -1) and n == len(path)
        