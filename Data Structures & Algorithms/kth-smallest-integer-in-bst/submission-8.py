# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
             #Understand: We want to return the kth smallest node. So go to the lowest and work your way back up
             #Input: root of a BST
             #Output: kth smallest Node (so if 1th smallest node, return the left most)

             #Match: Inorder Traversal --> DFS

             #Plan:
             #Edgecases: if tree is None return None
             #base Case if k 


             self.k = k

             def shortest(root):
                if not root:
                    return 0
                
                

                

                left = shortest(root.left)

                self.k -= 1

                if self.k == 0:
                    return root.val
                right = shortest(root.right)

                


                return left or right


             return shortest(root)