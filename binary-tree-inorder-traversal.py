# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodes = []
    
    def inorderTraversalHelper(self, root: Optional[TreeNode]) -> List[int]:
        if root.left:
            self.inorderTraversalHelper(root.left)
        self.nodes.append(root.val)
        if root.right:
            self.inorderTraversalHelper(root.right)
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        self.inorderTraversalHelper(root)
        return self.nodes
    
## Can I do return only?
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode], prev = []) -> List[int]:
#         if not root: return []
        
#         if root.left:
#             self.inorderTraversal(root.left, prev)
#         prev.append(root.val)
#         if root.right:
#             self.inorderTraversal(root.right, prev)
#         return prev

## Not sure why the single function version doesn't work
