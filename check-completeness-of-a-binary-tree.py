class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        stack, i = [(root, 0, 0)], 0
        implied = 0
        while stack:
            curr, d, j = stack.pop()
            i += 1
            implied = max(implied,2**d+j)
            if curr.left: stack.append((curr.left, d+1, j*2))
            if curr.right: stack.append((curr.right, d+1, j*2+1))
        return i == implied
#### TODO: understand their solution
#### 78, 100 Python3
# class Solution:
#     def isCompleteTree(self, root: TreeNode) -> bool:
#         stack, i = [(root, 0, 0)], 0
#         implied = 0
#         while i<len(stack):
#             curr, d, j = stack[i]
#             i += 1
#             implied = 2**d+j
#             if curr.left: stack.append((curr.left, d+1, j*2))
#             if curr.right: stack.append((curr.right, d+1, j*2+1))
#         return len(stack) == implied
#### O(n), O(n); 93, 100 Python3

# class Solution:
#     def isCompleteTree(self, root: TreeNode) -> bool:
#         def dfs(root,d,i,setting):
#             nonlocal depth
#             depth = max(depth,d)
#             if setting:
#                 # print(root.val,d,i,setting)
#                 nonlocal tree
#                 # print(2**d+i-1)
#                 tree[2**d+i-1] = root.val
#             if root.left: dfs(root.left,d+1,i*2,setting)
#             if root.right: dfs(root.right,d+1,i*2+1,setting)
#         depth = 0
#         dfs(root, depth, 0, False)
#         print(depth)
#         # BFS
#         tree = [-1]*(2**(depth+1)-1)
#         print(len(tree))
#         dfs(root, 0, 0, True)
#         print(tree)
#         blank = False
#         for i in range(2**depth-1,len(tree)):
#             if tree[i]==-1: blank = True
#             elif blank: return False
#         return True
#### NOTDONE

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