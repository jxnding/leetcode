# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            if root.left:
                root.left = self.pruneTree(root.left)
            if root.right:
                root.right = self.pruneTree(root.right)
            
            if root.left or root.right or root.val == 1:
                return root
            else:
                return None