class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def simulate():
            new_rotten = []
            for i, j in rotten:
                neighbors = []
                if i > 0: neighbors.append((i-1,j))
                if i < len(grid)-1: neighbors.append((i+1,j))
                if j > 0: neighbors.append((i,j-1))
                if j < len(grid[0])-1: neighbors.append((i,j+1))
                for x, y in neighbors:
                    if grid[x][y]==1:
                        grid[x][y]=2
                        new_rotten.append((x,y))
            return new_rotten
        
        # initialize rotten oranges
        rotten = []
        num_oranges = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2: 
                    rotten.append((i, j))
                    num_oranges += 1
                if grid[i][j] == 1:
                    num_oranges += 1
            
        i = 0
        while True:
            # simulate
            new_rotten = simulate()
            # no more spread
            if len(new_rotten) == 0: break
            rotten += new_rotten
            i += 1
        # check end
        if len(rotten) == num_oranges: return i
        else: return -1

#### O(n), O(n); Python3 27, 100
#### https://leetcode.com/problems/rotting-oranges/discuss/238540/python-simple-bfs-solution
#### ^ has interesting matrix edge checking

#### Previous
# class Solution:
#     def orangesRotting(self, grid):
#         def infect(i, j, g):
#             if i>0 and g[i-1][j]==1:
#                 g[i-1][j]=2
#             if j>0 and g[i][j-1]==1:
#                 g[i][j-1]=2
#             if i<len(g)-1 and g[i+1][j]==1:
#                 g[i+1][j]=2
#             if j<len(g[i])-1 and g[i][j+1]==1:
#                 g[i][j+1]=2
#             return g
#         def fresh(grid):
#             for i in range(len(grid)):
#                 for j in range(len(grid[i])):
#                     if grid[i][j]==1:
#                         return True
#             return False
#         g = [[grid[i][j] for j in range(len(grid[i]))] for i in range(len(grid))]
#         c = 0
#         while True:
#             print(g)
#             if not fresh(g):
#                 return c
#             for i in range(len(grid)):
#                 for j in range(len(grid[i])):
#                     if grid[i][j]==2: #infect nearby
#                         g=infect(i,j,g)
#                     grid = g
#             c+=1
# print(Solution().orangesRotting(
# [[2,1,1],[1,1,0],[0,1,1]]))