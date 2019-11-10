import pdb
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.width = {}
        
    def widthOfBinaryTree(self, root: TreeNode, depth=0, w=1) -> int:
        if depth==0:
            print("New Case")
            print(root)
        if root==None:
        #     try:
        #         self.width[depth].append(root)
        #     except:
        #         self.width[depth]=[root]
            return 0
        try:
            self.width[depth][w] = root.val
        except:
            self.width[depth] = {w: root.val}
        self.widthOfBinaryTree(root.left,depth+1,w*2-1)
        self.widthOfBinaryTree(root.right,depth+1,w*2)
        
        maxWidth = 0
        maxd = None
        for d, bar in self.width.items():
            left, right = 1000000, -1000000
            has = False
            for i in bar:
                if bar[i]!=None:
                    has = True
                    left = min(i,left)
                    right = max(i,right)
            if right-left+1>maxWidth and has:
                maxWidth = right-left
                maxd = d
        
        if depth==0:
            pdb.set_trace()
            print(maxd)
        return maxWidth+1

# class Solution:
#     def __init__(self):
#         self.width = {}
        
#     def widthOfBinaryTree(self, root: TreeNode, depth=0) -> int:
#         if root==None:
#             return 0
#         if root.val==None:
#             print("waka")
#         try:
#             self.width[depth].append(root.val)
#         except:
#             self.width[depth]=[root.val]
#         self.widthOfBinaryTree(root.left,depth+1)
#         self.widthOfBinaryTree(root.right,depth+1)
        
#         maxWidth = 0
#         for bar in self.width.values():
#             left, right = 1000000, -1000000
#             for i in range(len(bar)):
#                 if bar[i]!=None:
#                     left = min(i,left)
#                     right = max(i,right)
#             maxWidth = max(maxWidth,right-left+1)
        
#         return maxWidth

# class Solution:
#     def __init__(self):
#         self.width = {}
        
#     def widthOfBinaryTree(self, root: TreeNode, depth=0) -> int:
#         if root==None:
#             return 0
#         try:
#             self.width[depth]+=1
#         except:
#             self.width[depth]=1
#         self.widthOfBinaryTree(root.left,depth+1)
#         self.widthOfBinaryTree(root.right,depth+1)
#         return max(self.width.values())

x = TreeNode(val= 1, left= TreeNode(val= 1, left= TreeNode(val= 1, left= TreeNode(val= 1, left= None, right= None), right= None), right= None), right= TreeNode(val= 1, left= None, right= TreeNode(val= 1, left= None, right= TreeNode(val= 1, left= None, right= None))))
a = Solution()
a.widthOfBinaryTree(x)