class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if points==[] or points==None: return 0
        if len(points)==1: return 1
        
        lines = set()
        for i in range(len(points)):
            for j in range(i):
                s, e = points[i], points[j]
                if s[0]-e[0]==0: lines.add(('inf',0,s[0],s[1])) #vertical lines
                else:
                    x = (s[1]-e[1])
                    y = (s[0]-e[0])
                    lines.add((y, x, s[0], s[1]))
        lines = list(lines)
        lineNumber = [0 for _ in range(len(lines))]
        for p in points:
            for i, l in enumerate(lines): #test []
                if l[0]=='inf': #vertical
                    if p[0]==l[2]: lineNumber[i]+=1
                else:
                    if p[0]==l[2] and p[1]==l[3]: lineNumber[i]+=1
                    elif p[0]==l[2]: pass
                    elif (p[1]-l[3])/(p[0]-l[2])==l[1]/l[0]: lineNumber[i]+=1
        return max(lineNumber)
#### O(n^3), O(n^2); 8, 42 Python3
#### TODO: O(n^2) solution