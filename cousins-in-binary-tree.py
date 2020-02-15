# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def find(root, d, parent, target):
            if root==None: return
            nonlocal found
            if root.val == target:
                found = (d, parent)
            if not found:
                find(root.left, d+1, root, target)
                find(root.right, d+1, root, target)
        x_val, y_val = None, None
        found = False
        if root.val == x:
            x_val = (0, None)
        else:
            find(root, 0, None, x)
            x_val = found
            found = False
        if root.val == y:
            y_val = (0, None)
        else:
            find(root, 0, None, y)
            y_val = found
            found = False
        # Compare
        if x_val[0] == y_val[0] and x_val[1] != y_val[1]: return True
        return False

#### O(n), O(1); 94, 100 Python3