import pdb
class Solution:
    def criticalConnections(self, n, connections):
        def dfs(start):
            def deleteCycle(start, end):
                v = start
                u = parent[v]
                conn[v].remove(u)
                conn[u].remove(v)
                if u!=end:
                    deleteCycle(u, end)
            visited = set()
            parent = [None]*n
            open = set()
            open.add(start)
            while open:
                curr = open.pop()
                for neighbor in conn[curr]:
                    if neighbor not in visited:
                        parent[neighbor]=curr
                        open.add(neighbor)
                    else:
                        #delete next edge
                        conn[neighbor].remove(curr)
                        conn[curr].remove(neighbor)
                        #delete previous edges
                        deleteCycle(curr, neighbor)
                visited.add(curr)
            return len(visited)
        # def dfs(start):
        #     nonlocal visited
        #     visited.add(start)
        #     for neighbor in conn[start]:
        #         if neighbor not in visited:
        #             dfs(neighbor)

        # Build edges
        conn = {}
        for i in range(n):
            conn[i] = set()
        for edge in connections:
            conn[edge[0]].add(edge[1])
            conn[edge[1]].add(edge[0]) #Bidirectional
        
        visited = set()
        # Search for critical connections
        # critical = []
        # for edge in connections:
        #     prevTotal = dfs(edge[0])
        #     conn[edge[0]].remove(edge[1])
        #     conn[edge[1]].remove(edge[0])
        #     removedTotal = dfs(edge[0])
            
        #     if removedTotal<prevTotal:
        #         critical.append(edge)
            
        #     conn[edge[0]].add(edge[1])
        #     conn[edge[1]].add(edge[0])
        dfs(0)
        print(visited)
        return critical
        
        
a1 = [[0,1],[1,2],[2,0],[1,3]]
x1 = a1
print(Solution().criticalConnections(len(x1), x1))


###################


# class Solution:
#     def criticalConnections(self, n, connections):
#         def dfs2(start):
#             visited = set()
#             open = set()
#             open.add(start)
#             while open:
#                 curr = open.pop()
#                 if curr not in visited:
#                     for neighbor in conn[curr]:
#                         open.add(neighbor)
#                     visited.add(curr)
#             return len(visited)
        
#         def dfs(start):
#             nonlocal visited
#             visited.add(start)
#             for neighbor in conn[start]:
#                 if neighbor not in visited:
#                     dfs(neighbor)

#         # Build edges
#         conn = {}
#         for i in range(n):
#             conn[i] = set()
#         for edge in connections:
#             conn[edge[0]].add(edge[1])
#             conn[edge[1]].add(edge[0]) #Bidirectional
            
#         # Search for critical connections
#         # critical = []
#         # for edge in connections:
#         #     prevTotal = dfs(edge[0])
#         #     conn[edge[0]].remove(edge[1])
#         #     conn[edge[1]].remove(edge[0])
#         #     removedTotal = dfs(edge[0])
            
#         #     if removedTotal<prevTotal:
#         #         critical.append(edge)
            
#         #     conn[edge[0]].add(edge[1])
#         #     conn[edge[1]].add(edge[0])
#         print(dfs(0))
#         return critical