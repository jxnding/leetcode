class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        # def bfs(start):
        #     visited = set()
        #     visited.add(start)
        #     q = []
        #     q.append(start)
        #     while len(q)>0:
        #         v = q.pop()
        #         if 
        #random
        def randomColor():
            r = random.random()
            if r<.25:
                return 1
            elif r<.5:
                return 2
            elif r<.75:
                return 3
            else:
                return 4
        flower = [0]*N
        for i in range(N):
            flower[i]=randomColor()
        #edges
        # edge = {}
        # for e in paths:
        #     if e[0] in edge:
        #         edge[e].append(e[1])
        #     else:
        #         edge[e]=[e[1]]
        #     if e[1] in edge:
        #         edge[e].append(e[0])
        #     else:
        #         edge[e]=[e[0]]
        
        while True:
            valid = True
            for e in paths:
                if flower[e[0]-1]==flower[e[1]-1]:
                    valid = False
                    flower[e[0]-1]=randomColor()
            if valid:
                return flower