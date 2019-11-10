
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        d = [[0 for x in range(len(grid[0]))] for x in range(len(grid))]
        # Base cases
        d[0][0]=grid[0][0]
        for i in range(1, len(grid)):
            d[i][0]=d[i-1][0]+grid[i][0]
        for i in range(1, len(grid[0])):
            d[0][i]=d[0][i-1]+grid[0][i]
        
        for i in range(1,len(grid)):
            for j in range(1,len(grid[i])):
                d[i][j]=min(d[i-1][j],d[i][j-1])+grid[i][j]
        return d[len(grid)-1][len(grid[0])-1]