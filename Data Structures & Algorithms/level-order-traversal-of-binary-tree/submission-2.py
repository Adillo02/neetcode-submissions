# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Understand: We want to traverse the binary tree level by level so that each level has its own sublist in the answer
        #Input: root of Binary Tree
        #Output: list of sublist and each suvlist represents a level in the Tree


        #Plan: Start off by using the first level in the Tree in the list 
        # We want to use a helper function that does BFS
        # Base Case: if root is None return []
        if not root:
            return []

        queue = deque()
        queue.append(root)
        ans = []

        while queue:
            level_size = len(queue)
            temp = []

            for i in range(level_size):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(temp)

        
        return ans 
        