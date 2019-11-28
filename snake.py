class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        b = []
        if len(board)%2==0:
            flipped = True
        else:
            flipped = False
        for row in board:
            if flipped:
                b=row[::-1]+b
            else:
                b=row+b
            flipped = not flipped
        b = [0]+b

        for i in range(len(b)):
            if b[i]==-1:
                b[i]=i

        d = [2**32-1]*len(b)
        d[1] = 0
        for i in range(1,len(board)**2):
            for j in range(i+1,min(i+6, len(board)**2)+1 ):
                d[b[j]]=min(d[b[j]],d[i]+1)

        if d[len(board)**2]==(2**32-1):
            return -1
        return d[len(board)**2]

def snakesAndLadders(self, board):
    b = []
    if len(board)%2==0:
        flipped = True
    else:
        flipped = False
    for row in board:
        if flipped:
            b=row[::-1]+b
        else:
            b=row+b
        flipped = not flipped
    b = [0]+b
    for i in range(len(b)):
        if b[i]==-1:
            b[i]=i
    d = [2**32-1]*len(b)
    d[1] = 0
    for i in range(1,len(board)**2):
        for j in range(i+1,min(i+6, len(board)**2)+1 ):
            d[b[j]]=min(d[b[j]],d[i]+1)
    pdb.set_trace()
    if d[len(board)**2]==(2**32-1):
        return -1
    return d[len(board)**2]
