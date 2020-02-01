class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        def minNeighbors(i, j, direction):
            if direction==0: #top left
                if i==0 and j==0:
                    return 100000
                elif i==0:
                    return TL[i][j-1]
                elif j==0:
                    return TL[i-1][j]
                else:
                    return min(TL[i-1][j],TL[i][j-1])
            else:
                if i==len(matrix)-1 and j==len(matrix[0])-1:
                    return 100000
                elif i==len(matrix)-1:
                    return TL[i][j+1]
                elif j==len(matrix[0])-1:
                    return TL[i+1][j]
                else:
                    return min(TL[i+1][j],TL[i][j+1])
            
        TL = [[100000 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0: 
                    TL[i][j]=0
                else: 
                    TL[i][j]=minNeighbors(i, j, 0)+1
                    
        # BR = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[i])-1,-1,-1):
                if matrix[i][j]==0: 
                    TL[i][j]=0
                else: 
                    TL[i][j]=min(TL[i][j], minNeighbors(i, j, 1)+1)
        return TL
#### O(m * n), O(m * n); 86, 33 in Python3 
#### I did well! Thought of DP solution in 15 min!
#### TODO: Why is the BFS solution O(m * n) too?

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        d = [[10000 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0: 
                    d[i][j]=0
                else:
                    if i==0 and j==0: pass
                    elif i==0: d[i][j]=d[i][j-1]+1
                    elif j==0: d[i][j]=d[i-1][j]+1
                    else: d[i][j]=min(d[i-1][j],d[i][j-1])+1

        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                if matrix[i][j]==0: 
                    d[i][j]=0
                else:
                    if i==len(matrix)-1 and j==len(matrix[0])-1: pass
                    #previous solution might be OK
                    elif i==len(matrix)-1:
                        d[i][j]=min(d[i][j],d[i][j+1]+1)
                    elif j==len(matrix[0])-1:
                        d[i][j]=min(d[i][j],d[i+1][j]+1)
                    else:
                        d[i][j]=min(d[i][j],d[i+1][j]+1,d[i][j+1]+1)
        
        return d
#### O(n^2), O(n^2); 93, 33 Python3
