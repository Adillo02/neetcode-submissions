# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # If root is empty return 0 
        #if no roots are greater than return 0

        #Plan: Modified DFS using recursion where we are determining if its bigger than the rooot
        #store the root val in a global variable that way we can compare
        # Base case would be:
        # If the root is None return 0
        # if the left side is bigger than the root:
        # we would do a recursive call to the left + 1 because that is a good node
        # do the same for the right
        # we want to to fo  both of those recursive calls which gives the total number of good nodes

        if not root:
            return 0
        
       

        def dfs(root, curr_max):
            if not root:
                return 0
            
            if root.val >= curr_max:
                curr_max = root.val
                return 1 + dfs(root.left, curr_max) + dfs(root.right, curr_max)

            return dfs(root.left, curr_max) + dfs(root.right, curr_max)

        
        return dfs(root, root.val)

            
            
        