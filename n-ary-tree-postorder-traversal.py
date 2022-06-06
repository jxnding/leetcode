"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # 	86 ms	16.6 MB on 22/06/06
    def postorder(self, root: 'Node') -> List[int]:
        def postorderinner(root: 'Node', ans = List['Node']):
            if root.children:
                for c in root.children:
                    postorderinner(c, ans)
            ans.append(root.val) #don't forget your own value
        
        if root == None: return []
        
        ans = []
        postorderinner(root, ans)
        return ans

    #   60 ms	16 MB on 22/06/06
    ## NOTE: Iterative solution below, pretty messy I think
    def postorderIterative(self, root: 'Node') -> List[int]:
        if root is None: return []
        
        ans = []
        stack = deque() #dfs is FIFO
        stack.append(root)
        
        while stack:
            curr = stack.pop()
            if curr.children:
                stack.append(curr)
                stack.append(curr.children[0])
                del curr.children[0]
            else:
                #stay popped
                ans.append(curr.val)
        
        return ans
            