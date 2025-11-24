from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Build graph
        Find a source vertex (if none, return impossible)
        BFS/DFS from there (actually... maybe BFS is better)

        O(V + E) space, O(V^2 + E) time

        ^^ Actually above is wrong?
        It needs to be a DAG, any cycles will make it impossible.

        3ms, 77.06% | 19.64MB, 26.62%
        """
        
        # ### Build graph
        # graph = {} # dict of sets
        # preqs = {} # dict of sets
        # for p in prerequisites:
        #     start, end = p[1], p[0]
        #     if start in graph:
        #         graph[start].add(end)
        #     else:
        #         graph[start] = set([end])
            
        #     if end in preqs:
        #         preqs[end].add(start)
        #     else:
        #         preqs[end] = set([start])
        
        # sources = []
        # for i in range(numCourses):
        #     if i not in preqs:
        #         sources.append(i)
        # if len(sources) == 0: return []
        
        # ### BFS but with a prereq check
        # visited = set()
        # path = [] # could use a stableset and combine visited & path
        # q = deque(sources)
        # while len(q) > 0:
        #     curr = q.popleft()

        #     visited.add(curr)
        #     path.append(curr)
        #     for neighbor in graph.get(curr, []):
        #         if neighbor not in visited and preqs[neighbor].issubset(visited):
        #             q.append(neighbor)
        # if len(path) == numCourses:
        #     return path
        # return [] #we couldn't visit whole graph

        """
        Optimize the preqs check
        Let's use preqs as a "shadow graph" and delete edges when we visit them
        Oh wait, we will need to know where we came from (NVM, that is totally wrong!)
            So basically the whole prevs logic is wrong? Instead of removing edges when I visit a class, I should remove edges that are neighbors of the class I visited (basically 1 step earlier), is that right?

        O(V + E) space, O(V + E)runtime

        11ms, 9.10% | 19.67MB, 26.62%
        """
        # ### Build graph
        # graph = {} # dict of sets
        # preqs = {} # dict of sets
        # for p in prerequisites:
        #     start, end = p[1], p[0]
        #     if start in graph:
        #         graph[start].add(end)
        #     else:
        #         graph[start] = set([end])
            
        #     if end in preqs:
        #         preqs[end].add(start)
        #     else:
        #         preqs[end] = set([start])
        
        # sources = []
        # for i in range(numCourses):
        #     if i not in preqs:
        #         sources.append(i)
        # if len(sources) == 0: return []
        
        # ### BFS but with a prereq check
        # visited = set()
        # path = [] # could use a stableset and combine visited & path
        # q = deque(sources)
        # while len(q) > 0:
        #     curr = q.popleft()

        #     visited.add(curr)
        #     path.append(curr)
        #     # remove preqs
        #     for neighbor in graph.get(curr, []):
        #         preqs[neighbor].remove(curr)    
            
        #     # BFS
        #     for neighbor in graph.get(curr, []):
        #         if neighbor not in visited and len(preqs[neighbor])==0:
        #             q.append(neighbor)
        # if len(path) == numCourses:
        #     return path
        # return [] #we couldn't visit whole graph

        """
        Optimize the preqs check to just be a list

        O(V + E) space, O(V + E)runtime

        11ms, 9.10% | 19.51MB, 31.57%
        """
        ### Build graph
        graph = {} # dict of sets
        preqs = {} # dict of sets
        for p in prerequisites:
            start, end = p[1], p[0]
            if start in graph:
                graph[start].add(end)
            else:
                graph[start] = set([end])
            
            if end in preqs:
                preqs[end].add(start)
            else:
                preqs[end] = set([start])
        
        sources = []
        remainingPreqs = [0] * numCourses
        for i in range(numCourses):
            if i not in preqs:
                sources.append(i)
            else:
                remainingPreqs[i] = len(preqs[i])
        if len(sources) == 0: return []
        
        ### BFS but with a prereq check
        visited = set()
        path = [] # could use a stableset and combine visited & path
        q = deque(sources)
        while len(q) > 0:
            curr = q.popleft()

            visited.add(curr)
            path.append(curr)

            # remove preqs
            for neighbor in graph.get(curr, []):
                remainingPreqs[neighbor] -= 1

            for neighbor in graph.get(curr, []):
                if neighbor not in visited and remainingPreqs[neighbor]==0:
                    q.append(neighbor)
        if len(path) == numCourses:
            return path
        return [] #we couldn't visit whole graph