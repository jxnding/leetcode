# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.linear = []
        self.inorderTraverse(root)
        self.index = 0
        

    def inorderTraverse(self, root: Optional[TreeNode]):
        if root.left:
            self.inorderTraverse(root.left)
        self.linear.append(root.val)
        if root.right:
            self.inorderTraverse(root.right)
        
    def next(self) -> int:
        self.index += 1
        return self.linear[self.index-1]

    def hasNext(self) -> bool:
        if self.index + 1 <= len(self.linear):
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()