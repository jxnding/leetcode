# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def BST(root, L, R):
            if root == None: return
            nonlocal total
            if L <= root.val <= R:
                total += root.val
            if root.val >= L:
                BST(root.left, L, R)
            if root.val <= R:
                BST(root.right, L, R)
        total = 0
        BST(root, L, R)
        return total
#### O(n), O(1); 86, 35 Python3
# 4/13 2:41 -> 2:46
