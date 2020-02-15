class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # get edges
        edges = {}
        for u, v, w in times:
            if u in edges: edges[u].append((v, w))
            else: edges[u] = [(v, w)]
        # DFS with priority
        import heapq
        pq=[(0,K)]
        heapq.heapify(pq)
        visited = set()
        total = 0
        while pq:
            # Get current and check visited
            weight, curr = heapq.heappop(pq)
            if curr in visited: continue
            visited.add(curr)
            total += weight
            # Decrement other current edges
            for i, (w, v) in enumerate(pq):
                pq[i] = (w-weight, v)
            # Add new edges
            if curr in edges:
                for v, w in edges[curr]:
                    if v not in visited:
                        heapq.heappush(pq,(w,v))
        # check completeness
        if len(visited)==N: return total
        return -1
#### O(n^3), O(n^2); 25, 69 Python3
#### TODO Runtime

#### 5, 69 Python3
# class Solution:
#     def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
#         # get edges
#         edges = {}
#         for u, v, w in times:
#             if u in edges: edges[u].append((v, w))
#             else: edges[u] = [(v, w)]
#         # DFS with priority
#         from queue import PriorityQueue
#         pq = PriorityQueue()
#         pq.put((0,K))
#         visited = set()
#         total = 0
#         while not pq.empty():
#             weight, curr = pq.get()
#             if curr in visited: continue
#             pql = []
#             while not pq.empty():
#                 a, b = pq.get()
#                 pql.append((a-weight, b))
#             pq = PriorityQueue()
#             for w, v in pql:
#                 pq.put((w,v))
#             visited.add(curr)
#             total += weight
#             if curr in edges:
#                 for v, w in edges[curr]:
#                     if v not in visited:
#                         pq.put((w,v))
#         # check completeness
#         if len(visited)==N: return total
#         return -1

#### Horizon based way, doesn't work
# class Solution:
#     def networkDelayTime(self, times, N: int, K: int) -> int:
#         # get edges
#         edges = {}
#         for u, v, w in times:
#             if u in edges: edges[u].append((v, w))
#             else: edges[u] = [(v, w)]
        
#         visited = set()
#         stack = [K]
#         horizon = []
#         time = 0
#         while stack:
#             print(visited)
#             # Get current node
#             curr = stack.pop()
#             if curr in visited: continue
#             visited.add(curr)
#             # Add to horizon
#             if curr in edges:
#                 horizon += edges[curr]
#             horizon.sort(key=lambda x:x[1])
#             # Min edge
#             if len(horizon)>0:
#                 new_node, weight = horizon[0]
#                 del horizon[0]
#                 stack.append(new_node)
#                 time += weight
#                 # Decrease horizon
#                 deleted = []
#                 for i in range(len(horizon)):
#                     if horizon[i][0] in visited: continue
#                     horizon[i] = (horizon[i][0], horizon[i][1]-weight)
#                     if horizon[i][1]==0:
#                         stack.append(horizon[i][0])
#                         deleted.append(i)
#                 for i in range(len(deleted)-1,-1,-1):
#                     del horizon[deleted[i]]
#         if len(visited)==N: return time
#         return -1