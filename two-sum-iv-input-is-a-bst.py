# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def traverse(node):
            nonlocal complements
            nonlocal found
            if node:
                if node.val in complements: found=True
                complements.add(k-node.val)
                traverse(node.left)
                traverse(node.right)
        complements = set()
        found = False
        traverse(root)
        return True if found else False
#### O(n), O(n); 76, 23