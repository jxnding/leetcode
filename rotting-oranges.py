class Solution:
    def orangesRotting(self, grid):
        def infect(i, j, g):
            if i>0 and g[i-1][j]==1:
                g[i-1][j]=2
            if j>0 and g[i][j-1]==1:
                g[i][j-1]=2
            if i<len(g)-1 and g[i+1][j]==1:
                g[i+1][j]=2
            if j<len(g[i])-1 and g[i][j+1]==1:
                g[i][j+1]=2
            return g
        def fresh(grid):
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j]==1:
                        return True
            return False
        g = [[grid[i][j] for j in range(len(grid[i]))] for i in range(len(grid))]
        c = 0
        while True:
            print(g)
            if not fresh(g):
                return c
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j]==2: #infect nearby
                        g=infect(i,j,g)
                    grid = g
            c+=1
print(Solution().orangesRotting(
[[2,1,1],[1,1,0],[0,1,1]]))

# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         def infect(i, j):
#             if i>0 and grid[i-1][j]==1:
#                 grid[i-1][j]=2
#             if j>0 and grid[i][j-1]==1:
#                 grid[i][j-1]=2
#             if i<len(grid)-1 and grid[i+1][j]==1:
#                 grid[i+1][j]=2
#             if j<len(grid[i])-1 and grid[i][j+1]==1:
#                 grid[i][j+1]=2
#         def fresh():
#             for i in range(len(grid)):
#                 for j in range(len(grid[i])):
#                     if grid[i][j]==1:
#                         return True
#             return False
#         c = 0
#         while True:
#             if not fresh():
#                 return c
#             for i in range(len(grid)):
#                 for j in range(len(grid[i])):
#                     if grid[i][j]==2: #infect nearby
#                         infect(i,j)
#             c+=1