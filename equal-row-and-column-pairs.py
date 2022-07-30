class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        myDict = {}
        for i in range(len(grid)):
            row = hash(RollingHashList(grid[i]))
            myDict[row] = myDict.get(row, 0) + 1
        for j in range(len(grid)):
            column = hash(RollingHashList([grid[n][j] for n in range(len(grid))]))
            if column in myDict: 
                ans += myDict[column]
        return ans
    
class RollingHashList:
    def __init__(self, inputList: List[List[int]]):
        self.list = inputList
        
    def __hash__(self):
        hashAns = 0
        for n in self.list:
            # Make sure the hash function is NOT communicative!!
            hashAns *= hash(n)
            hashAns += hash(n)
        return hashAns
    
    def __str__(self):
        return str(self.list)