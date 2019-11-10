class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1, numRows+1):
            row = []
            for j in range(i):
                val = None
                if j==0 or j==i-1:
                    val = 1
                else:
                    val = ans[i-2][j-1]+ans[i-2][j] #starting at 1 instead of 0, need extra offset
                row.append(val)
            ans.append(row)
        return ans