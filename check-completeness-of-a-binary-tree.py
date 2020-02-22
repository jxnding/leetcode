# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        def dfs(root,d,i,setting):
            nonlocal depth
            depth = max(depth,d)
            if setting:
                # print(root.val,d,i,setting)
                nonlocal tree
                # print(2**depth+i-1)
                tree[2**depth+i-1] = root.val
            if root.left: dfs(root.left,d+1,i*2,setting)
            if root.right: dfs(root.right,d+1,i*2+1,setting)
        depth = 0
        dfs(root, depth, 0, False)
        print(depth)
        # BFS
        tree = [-1]*(2**(depth+1)-1)
        print(len(tree))
        dfs(root, 0, 0, True)
        for i in range(2**depth,len(tree)):
            if tree[i-1]==-1: 
                print('waka')
                if (i-1)%2==0: return False # empty right child
                else:
                    if tree[i]<tree[(i-1)//2]: return False
        return True

# class Solution:
#     def isCompleteTree(self, root: TreeNode) -> bool:
#         # Get queue
#         from queue import Queue
#         stack = []
#         stack.append((root, None, 0))
#         # BFS
#         i, counter = 0, 0
#         prevDepth = 0
#         while i<len(stack):
#             curr, parent, depth = stack[i]
#             i += 1
#             if depth != prevDepth: # Check filled
#                 if 2**depth-1 > counter: return False
#                 prevDepth = depth
#             if type(curr)==int: continue
#             counter += 1
#             if curr.left: stack.append((curr.left, curr, depth+1))
#             else: stack.append((-2, curr, depth+1))
#             if curr.right: stack.append((curr.right, curr, depth+1))
#             else: stack.append((-1, curr, depth+1))
#         print('here')
#         # Check left-most
#         for i in range(2**prevDepth-1, len(stack)):
#             curr, parent, depth = stack[i]
#             prev = stack[i-1]
#             if type(prev[0])==int: # previous is empty
#                 if prev[0] == -2: # left empty
#                     if curr.val < prev[1].val: return False
#                 else:
#                     return False
#                     # if curr.val < prev[1].val: return False
#         return True