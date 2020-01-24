#### A* below, doesn't work
import queue
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def neighbor(pos):
            i, j = pos[0], pos[1]
            neighbors = []
            if i>0: neighbors.append((i-1,j))
            if j>0: neighbors.append((i,j-1))
            if i<len(forest)-1: neighbors.append((i+1,j))
            if j<len(forest[0])-1: neighbors.append((i,j+1)) 
            return neighbors
        
        def astar(start, goal):
            def estimate(start, goal):
                return abs(start[0]-goal[0])+abs(goal[1]-start[1])
            visited = set()
            openSet = queue.PriorityQueue()
            openSet.put( (0,start) )
            
            while not openSet.empty():
                currDist, curr = openSet.get()
                if curr==goal:
                    return currDist, curr
                visited.add(curr)
                
                for n in neighbor(curr):
                    if n not in visited:
                        if forest[n[0]][n[1]]==0:
                            visited.add(n)
                        else:
                            visited.add(n)
                            openSet.put( (currDist+1+estimate(n, goal), n) )
            return -1, (-1,-1)
        
        # Get trees
        trees = []
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j]>1: trees.append( (i, j) )
        # Sort trees
        trees.sort(key=lambda x:forest[x[0]][x[1]])
        # BFS across trees
        ans, pos = 0, (0,0)
        for i, j in trees:
            dist, pos = astar(pos, (i,j))
            if dist==-1: return -1
            ans += dist

        return ans
#### BFS solution below (TLE)
import queue
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def neighbor(pos):
            i, j = pos[0], pos[1]
            neighbors = []
            if i>0: neighbors.append((i-1,j))
            if j>0: neighbors.append((i,j-1))
            if i<len(forest)-1: neighbors.append((i+1,j))
            if j<len(forest[0])-1: neighbors.append((i,j+1)) 
            return neighbors
        
        def bfs(start, goal):
            visited = set()
            openSet = queue.Queue()
            openSet.put( (start,0) )
            
            while not openSet.empty():
                curr, currDist = openSet.get()
                if forest[curr[0]][curr[1]]==goal:
                    return currDist, curr
                visited.add(curr)
                
                for n in neighbor(curr):
                    if n not in visited:
                        if forest[n[0]][n[1]]==0:
                            visited.add(n)
                        else:
                            visited.add(n)
                            openSet.put( (n, currDist+1) )
            return -1, (-1,-1)
        
        # Get trees
        trees = set(forest[i][j] for i in range(len(forest)) for j in range(len(forest[0])) )
        if 0 in trees: trees.remove(0)
        if 1 in trees: trees.remove(1)
        # Sort trees
        trees = list(trees)
        trees.sort()
        # BFS across trees
        ans, pos = 0, (0,0)
        for i in trees:
            dist, pos = bfs(pos, i)
            if dist==-1: return -1
            ans += dist

        return ans
#### 8/9 below
# My solution (doesn't work yet)
# Review: BFS vs Dijkstra

from collections import deque

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def bfs(start, end):
            nonlocal g
            q = deque([start])
            visited = set([start])
            d = {start:0}

            while q:
                curr = q.popleft()
                visited.add(curr)
                for n in g[curr]:
                    if n not in visited:
                        alt = d[curr] + 1
                        try:
                            if d[n]>alt:
                                d[n] = alt
                        except:
                            d[n] = alt
                        q.append(n)
            try:
                return d[end]
            except:
                return -1

        #create graph as dictionary AND dictionary of values
        g = {}
        ind = {}
        for x in range(len(forest)):
            for y in range(len(forest[x])):
                neighbors = []
                if(x>0 and forest[x-1][y]!=0):
                    neighbors.append((x-1,y))
                if(y>0 and forest[x][y-1]!=0):
                    neighbors.append((x,y-1))
                if(x<len(forest)-1 and forest[x+1][y]!=0):
                    neighbors.append((x+1,y))
                if(y<len(forest[x])-1 and forest[x][y+1]!=0):
                    neighbors.append((x,y+1))
                g[(x,y)] = neighbors
                ind[forest[x][y]] = (x,y)
                # if 0<forest[x][y]<start:
                #     start = forest[x][y]

        #sort trees
        trees = list(ind.keys())
        trees.sort()
        if trees[0]==0:
            del trees[0]
        start=trees[0]

        # start search
        dist = 0
        curr = ind[start]
        for i in range(1,len(trees)):
            nxt = ind[trees[i]]
            result = bfs(curr,nxt)
            if result==-1:
                return -1
            dist+=result
            curr = nxt

        return dist





test = [ [1,2,3], [0,0,4], [7,6,5]]
cutOffTree(0, test)

# You are asked to cut off trees in a forest for a golf event. The forest is represented as a non-negative 2D map, in this map:
#
# 0 represents the obstacle can't be reached.
# 1 represents the ground can be walked through.
# The place with number bigger than 1 represents a tree can be walked through, and this positive number represents the tree's height.
#
#
# You are asked to cut off all the trees in this forest in the order of tree's height - always cut off the tree with lowest height first. And after cutting, the original place has the tree will become a grass (value 1).
#
# You will start from the point (0, 0) and you should output the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.
#
# You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.
#
# Example 1:
#
# Input:
# [
#  [1,2,3],
#  [0,0,4],
#  [7,6,5]
# ]
# Output: 6
#
#
# Example 2:
#
# Input:
# [
#  [1,2,3],
#  [0,0,0],
#  [7,6,5]
# ]
# Output: -1
#
#
# Example 3:
#
# Input:
# [
#  [2,3,4],
#  [0,0,5],
#  [8,7,6]
# ]
# Output: 6
# Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
#
#
# Hint: size of the given matrix will not exceed 50x50.
