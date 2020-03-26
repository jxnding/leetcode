import numpy as np
class Solution:
    def maxArea(self, height):
        rightMax = [0]*len(height)
        max_val = height[-1]
        for i in range(len(height)-1,-1,-1):
            max_val = max(max_val, height[i])
            rightMax[i] = max_val
            
        max_val = height[0]
        leftMax = [0]*len(height)
        for i in range(len(height)):
            max_val = max(max_val, height[i])
            leftMax[i] = max_val
        
        print(rightMax)
        print(leftMax)
        
        ans = [[0 for _ in range(len(height))] for _ in range(len(height))]
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                ans[i][j] = (j-i)*min(height[i],height[j])
        n = len(height)
        max_visited = 0
        current = 0
        l, r = n//2-1, n//2
        while l>0 and r<n-1:
            print(l,r)
            current = (l-r)*min(height[l],height[r])
            max_visited = max(max_visited, current)
            lr_max, ll_max = 0, 0
            if l>0:
                lr_max = (leftMax[l-1]-height[r])*(r-0)
                ll_max = (leftMax[l-1]-height[l])*(l-0)
            rr_max, rl_max = 0,0
            if r<n-1:
                rr_max = (rightMax[r+1]-height[r])*(n-r)
                rl_max = (rightMax[r+1]-height[l])*(n-l)
            potential_max = [lr_max, ll_max, rr_max, rl_max]
            if max(potential_max)>max_visited:
                index = potential_max.index(max(potential_max))
                if index==0:
                    l = l-1
                elif index==1:
                    r = l
                    l = l-1
                elif index==2:
                    l = r
                    r = r+1
                else:
                    r = r+1
            else:
                break
        return max_visited
x=[1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(x))