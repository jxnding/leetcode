# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ## Special properties:
        # Root node has <= 2 neighbors
        # Leaf nodes have 1 neighbor

        ## DP: + self is required, otherwise it'll be noncontiguous

        ## DP
        # Store max ending at current node
        
        ## Questions
        # does in/pre/postorder matter?
        # def traverse(curr, prevMax):
        #     if curr.left:
        #         maxLeft = traverse(curr.left, curr.maxEnd)
        #         curr.maxEnd = max(curr.maxEnd, maxLeft + curr.val)
        #     curr.maxEnd = max(curr.val, curr.val + prevMax)
        #     if curr.right:
        #         maxRight = traverse(curr.right, curr.maxEnd)
        #         curr.maxEnd = max(curr.maxEnd, maxRight + curr.val)
        #     nonlocal ans
        #     ans = max(ans, curr.maxEnd)
        #     return curr.maxEnd
        def traverse(curr):
            if curr is None:
                return 0
            
            maxLeft = traverse(curr.left)
            maxRight = traverse(curr.right)

            maxEnd = max(maxLeft + curr.val, maxRight + curr.val) # max ending at me
            maxEnd = max(maxEnd, curr.val) # can take myself only
            nonlocal ans
            ans = max(ans, maxEnd)
            ans = max(ans, maxLeft + maxRight + curr.val) #max doing through me
            return maxEnd
        
        ans = -(2*30)
        traverse(root)
        return ans
        # root.maxEnd = root.val
            
#### Gemini better style below 
def traverse(curr):
    if curr is None:
        return 0
    
    # If a subtree sum is negative, we treat it as 0 (we "ignore" it)
    maxLeft = max(traverse(curr.left), 0)
    maxRight = max(traverse(curr.right), 0)

    # The max path 'peaking' at this node
    current_path_sum = curr.val + maxLeft + maxRight
    
    nonlocal ans
    ans = max(ans, current_path_sum)
    
    # Return the max path that can extend to the parent
    return curr.val + max(maxLeft, maxRight)