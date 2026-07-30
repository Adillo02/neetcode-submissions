# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #Understand: We are given the root of a Binary Tree and we want to only return the values on the right most side for each level

        #Input: root of a Binary Tree
        # Output: A list of the right most values of each level 

        #plan: BFS because we want o get the right most value of  a level
        # We could use a queue and start by adding the root value to the queue
        #While queue we pop from the queue until we get the right most value
        # Add the right most to the queue and contiune

        if not root:
            return []

        queue = deque([root])
        ans = []

        while queue:
            size = len(queue)

            for i in range(size - 1):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            
            node = queue.popleft()

            if not node:
                return ans 

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            ans.append(node.val)

        return ans 


            



        