class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        paths = []
        num = 1
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i]==1: num=0
            paths.append(num)
        for i in range(1,len(obstacleGrid)):
            if obstacleGrid[i][0]==1: paths[0]=0
            for j in range(1,len(obstacleGrid[0])):
                paths[j]+=paths[j-1]
                if obstacleGrid[i][j]==1:
                    paths[j]=0
        return paths[-1]
#### O(n^2), O(n); 97, 100 Python3
