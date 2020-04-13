"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def conn(c):
            if c.left and c.right:
                if c.next:
                    c.right.next = c.next.left
                c.left.next = c.right
            if c.right: conn(c.right)
            if c.left: conn(c.left)
        if root==None: return None
        conn(root)
        return root
#### O(n), O(1); 86, 89 Python3
## 4/13
# Review why below doesn't work
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         def conn(c):
#             if c.right: conn(c.right)
#             if c.left and c.right:
#                 if c.next:
#                     c.right.next = c.next.left
#                 c.left.next = c.right
#             if c.left: conn(c.left)
#         if root==None: return None
#         conn(root)
#         return root

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def conn(root):
            if root.left!=None:
                root.left.next = root.right
                if root.next!=None:
                    root.right.next = root.next.left
                conn(root.right)
                conn(root.left)
        if root==None: return None
        conn(root)
        return root
#### O(n), O(1); 76; 100 Python3
#### TODO: tricky