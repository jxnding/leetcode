import math, pdb
class Solution:
    def generateMatrix(self, n):
        ans = [[0 for i in range(n)] for i in range(n)]
        i, j = 0, 0
        direction = 0
        counter = 1
        
        dcounter = 0
        dmax = n-1
        while counter<=n**2:
            ans[i][j]=counter
            dcounter+=1
            if direction==0:
                j+=1
            elif direction==1:
                i+=1
            elif direction==2:
                j-=1
            elif direction==3:
                i-=1
            if dcounter==math.ceil(dmax):
                if direction==3: #need to decrease our length
                    dmax-=2
                    i+=1    
                    j+=1
                dcounter=0
                direction=(direction+1)%4 #new direction
            counter+=1
        # pdb.set_trace()
        return ans
print(Solution().generateMatrix(3))