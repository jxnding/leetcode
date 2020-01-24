# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
class Solution:
    def isValidBST(self, root: TreeNode, lower=-sys.maxsize, upper=sys.maxsize) -> bool:
        # print(root)
        # print(lower)
        # print(upper)
        if root==None:
            return True
        # print("Val: %d"%(root.val))
        if lower<root.val<upper:
            return self.isValidBST(root.left, lower, root.val) and self.isValidBST(root.right, root.val, upper)
        else: return False
#### O(n), O(n); 98, 100 Python3; 81, 50 Python2

class Solution:
    def isValidBST(self, root: TreeNode, lower=None, upper=None) -> bool:
        print(root)
        print(lower)
        print(upper)
        if root==None:
            return True
        print("Val: %d"%(root.val))
        valid = True
        if lower and upper:
            if lower<root.val<upper:
                return self.isValidBST(root.left, lower, root.val) and self.isValidBST(root.right, root.val, upper)
            else: return False
        elif lower:
            if lower<root.val:
                return self.isValidBST(root.left, lower, root.val) and self.isValidBST(root.right, root.val, upper)
            else: return False
        elif upper:
            if upper>root.val:
                return self.isValidBST(root.left, lower, root.val) and self.isValidBST(root.right, root.val, upper)
            else: return False
        else:
            return self.isValidBST(root.left, lower, root.val) and self.isValidBST(root.right, root.val, upper)