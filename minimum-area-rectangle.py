# Solution 3, I believe this is O(n^2) and already optimal, but they say time limit exceeded
import sys
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # create set for O(1) search
        pset = set()
        for p in points:
            pset.add((p[0],p[1]))

        ans = sys.maxsize
        # double loop through points to find diagonal points
        for a in points:
            for b in points:
                if a[0]!=b[0] and a[1]!=b[1]: #only diagonals
                    if (a[0],b[1]) in pset and (b[0], a[1]) in pset: #valid rectangle
                        ans = min(ans, abs(b[1]-a[1])*abs(b[0]-a[0]))

        if ans==sys.maxsize: #no valid rectangles
            return 0
        return ans
# Solution 1
import sys
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        ans = sys.maxsize

        #create sets
        x = set()
        y = set()
        for n in points:
            x.add(n[0])
            y.add(n[1])

        #delete orphan points
        for i in range(len(points)-1,-1,-1):
            if points[i][0] not in x:
                del points[i]
            elif points[i][1] not in y:
                del points[i]

        for i in range(len(points)-1):
            for j in range(i+1,len(points)):
                a, b = points[i], points[j]
                if a[0]!=b[0] and a[1]!=b[1]: #only diagonals
                    if [a[0],b[1]] in points and [b[0],a[1]] in points: #valid rectangle
                        ans = min(abs(b[1]-a[1])*abs(b[0]-a[0]), ans)
        if ans==sys.maxsize:
            return 0
        return ans

# Solution 2, very naive
import sys
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        ans = sys.maxsize

        for a in points:
            for b in points:
                if a[0]!=b[0] and a[1]!=b[1]: #diagonal
                    if [a[0],b[1]] in points and [b[0],a[1]] in points:
                        ans = min(ans, abs(b[0]-a[0])*abs(b[1]-a[1]))
        if ans==sys.maxsize:
            return 0
        return ans
