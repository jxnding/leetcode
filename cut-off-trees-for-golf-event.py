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
