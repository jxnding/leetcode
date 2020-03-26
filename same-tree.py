# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def same_tree(p, q):
            nonlocal ans
            if (not p) and (not q):
                pass
            elif (not p) or (not q):
                ans = False
            elif p.val!=q.val: 
                ans = False
            else:
                if p.left or q.left: same_tree(p.left, q.left)
                if p.right or q.right: same_tree(p.right, q.right)
        ans = True
        same_tree(p, q)
        return ans
#### O(n), O(1); 68, 100 Python3