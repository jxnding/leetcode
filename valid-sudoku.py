class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkSquare(x,y):
            square = set()
            for i in range(x,x+3):
                for j in range(y,y+3):
                    if board[i][j]=='.':
                        continue
                    if board[i][j] in square:
                        return False
                    else:
                        square.add(board[i][j])
            return True
                    
        # Check rows
        for i in range(len(board)):
            row = set()
            for j in range(len(board)):
                if board[i][j]=='.':
                    continue
                if board[i][j] in row:
                    return False
                else:
                    row.add(board[i][j])
        #Check columns
        for j in range(len(board)):
            row = set()
            for i in range(len(board)):
                if board[i][j]=='.':
                    continue
                if board[i][j] in row:
                    return False
                else:
                    row.add(board[i][j])
        #Check squares
        for i in range(0,len(board),3):
            for j in range(0,len(board),3):
                if not checkSquare(i,j):
                    return False
        return True

#### O(n^2) runtime, O(n) space?
#### Clapped in 12 min, second try