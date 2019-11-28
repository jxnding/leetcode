# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        self.LR = []
        self.RL = []

        self.doLR(root)
        self.doRL(root)

        return self.LR==self.RL

    def doLR(self,root):
        if root is None:
            self.LR.append(None)
        else:
            self.LR.append(root.val)
            self.doLR(root.left)
            self.doLR(root.right)

    def doRL(self,root):
        if root is None:
            self.RL.append(None)
        else:
            self.RL.append(root.val)
            self.doRL(root.right)
            self.doRL(root.left)
