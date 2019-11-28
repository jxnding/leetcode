# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        tl = []
        def treeList(root):
            nonlocal tl
            tl.append(root.val)
            if root.left:
                treeList(root.left)
            if root.right:
                treeList(root.right)
        if root is None:
            return None
        treeList(root)
        tl.sort()

        root = TreeNode(tl[0])
        for i in range(1,len(tl)):
            root.right = TreeNode(tl[i])
            root = root.right
