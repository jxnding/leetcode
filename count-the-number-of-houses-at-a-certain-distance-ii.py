from collections import deque
from typing import List
class Node:
    def __init__(self, val=0, others=[]):
        self.val = val
        self.others = others
    
    def __str__(self):
        return 'Node: '+str(self.val)
    
    def __repr__(self):
        return 'Node: '+str(self.val)
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        def bfs(root, n):
            # nonlocal n,x,y
            # print('wtf',x)
            ans = [0 for _ in range(n)]
            visited = set([root])
            queue = deque([(root,0)])
            while len(queue)>0:
                curr, dist = queue.popleft()
                if curr not in visited and dist>0: ans[dist-1] += 1#??
                visited.add(curr) #??
                # print('dist',root,curr,dist)
                # print(visited)
                for nnode in curr.others:
                    if nnode not in visited:
                        visited.add(curr)
                        queue.append((nnode,dist+1))
            # print('ansbfs:',ans)
            return ans
        ## remember to decrement by 1!
        x -= 1
        y -= 1
        ## Construct a chromosome graph (X shaped)
        graph = []
        for i in range(n):
            graph.append(Node(i))
        # add edges
        for i in range(n):
            neighbors = []
            if i>0:
                neighbors.append(graph[i-1])
            if i<n-1:
                neighbors.append(graph[i+1])
            graph[i].others = neighbors
        # add x <=> y
        if x!=y:
            graph[x].others.append(graph[y])
            graph[y].others.append(graph[x])
        # remove "top" node's in-edges, if applicable
        # if (x-y) % 2==0 and x!=y:
        #     top = (x+y)//2
        #     print(top)
        #     print(graph[top-1].others)
        #     print('before',top-1, graph[top-1].others)
        #     graph[top-1].others.remove(graph[top])
        #     graph[top+1].others.remove(graph[top])
        #     print('after',top-1, graph[top-1].others)
        
        ## BFS for every node, storing the results
        ans = [0 for _ in range(n)]
        for i in range(n):
            currAns = bfs(graph[i], n)
            for j in range(len(currAns)):
                ans[j] += currAns[j]
        return ans
            


        # ## remember to decrement by 1!
        # x -= 1
        # y -= 1
        # # left side, right side, cycle L, cycle R
        # # left side: [1, x]
        # # right side: [y, n]
        # # cycle L: (x+1, x+y/2] including top when counting from left side
        # # cycle R: [x+y/2, y) including top when counting from right side
        # L = [x for x in range(n)]
        # for i in range(len(L)):
        #     if l <= x:
        #         continue
        #     elif l <= (x+y)//2:
        #     elif l < y:
        #     else:
        #         L[i] = i-(x-y)+1
        # for i in range(len(R)):

x = Solution()
print(x.countOfPairs(1038,1038,831))