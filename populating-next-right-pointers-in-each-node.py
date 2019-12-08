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