# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Understand: for two given descendants we want to find the most recent/lowest ancestor
        #Input: root of the binary tree, and both nodes
        # Output: value of the most recent ancestor

        #Plan:use the fact that it is a binary tree
        # if p and q are both bigger than root then we go to the right
        # if p is greater and q is less than the most common ancestor would be that root vice versa
        # if p and q are both smaller than the root then we go to the left



        if (p.val >= root.val and q.val <= root.val) or (q.val >= root.val and p.val <= root.val):
            return root

        if (p.val >= root.val and q.val >= root.val):
            return self.lowestCommonAncestor(root.right, p, q)

        if (p.val <= root.val and q.val <= root.val):
            return self.lowestCommonAncestor(root.left, p, q)

        
        


        