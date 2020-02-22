class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def bs(i):
            l, r = 0, len(grid[i])
            while l<r:
                mid = (l+r)//2
                if grid[i][mid] < 0:
                    r = mid
                else:
                    l = mid + 1
            return len(grid[i])-l
        total = 0
        for i in range(len(grid)):
            total += bs(i)
        return total
#### O(n log n), O(1); 61, 100 Python3
#### TODO: I don't understand how I'm not overcounting:
# [[4,3,2],[0,-1,-1],[0,-1,-1]]

# class Solution:
#     def countNegatives(self, grid) -> int:
#         total = 0
#         last = -1
#         for i in range(len(grid)-1,-1,-1):
#             for j in range(len(grid[i])-1,last,-1):
#                 if grid[i][j]<0: total+=1
#                 else: 
#                     last=j
#                     break
#         return total
#### O(n^2), O(1); 83, 100 Python3