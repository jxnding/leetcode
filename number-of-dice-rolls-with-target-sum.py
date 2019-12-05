class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10**9+7
        dd = [[0 for i in range(target+1)] for i in range(d+1)]
        dd[0][0]=1
        for i in range(1, d+1):
            for j in range(1, target+1):
                for k in range(1, min(f,j)+1): #assume new die is 1, 2,... can't be bigger than feature(not valid solution)
                    dd[i][j] += dd[i-1][j-k]%mod
        return dd[d][target]%mod
#### 18, 100 Python3
#### TODO

#Below doesn't work...
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 10**9+7
        dd = [[0 for i in range(target)] for i in range(d)]
        dd[0][0]=1
        for i in range( d):
            for j in range( target):
                for k in range( min(f,j)): #assume new die is 1, 2,... can't be bigger than feature(not valid solution)
                    dd[i][j] += dd[i-1][j-k]%mod
        return dd[d-1][target-1]%mod